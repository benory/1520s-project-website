function initializeMusicalSearch({api, sitekey, workPath, assetBase, works, composers, assets}) {
  const form = document.getElementById('musical-search-form');
  const status = document.getElementById('search-status');
  const submit = form.querySelector('[type="submit"]');
  const verification = document.getElementById('musical-search-verification');
  const results = document.getElementById('musical-search-results');
  const resultsTitle = document.getElementById('musical-search-results-title');
  const list = document.getElementById('musical-search-matches');
  const pagination = document.getElementById('musical-search-pages');
  const previous = document.getElementById('musical-search-previous');
  const next = document.getElementById('musical-search-next');
  const fields = ['pitch', 'interval', 'rhythm', 'composer', 'genre', 'voice'];
  const workById = new Map(works.map(work => [work.ID, work]));
  const pageSize = 20;
  let token = '';
  let widget;
  let pending = false;
  let matches = [];
  let page = 1;

  const collator = new Intl.Collator('en', {numeric: true});
  const distinct = key => [...new Set(works.map(work => work[key]).filter(Boolean))].sort(collator.compare);
  for (const {ID, Composer} of [...composers].sort((a, b) => collator.compare(a.Composer, b.Composer))) {
    if (works.some(work => work.Composer === Composer)) form.elements.composer.add(new Option(Composer, ID));
  }
  for (const genre of distinct('Genre')) {
    form.elements.genre.add(new Option(genre[0].toUpperCase() + genre.slice(1), genre));
  }
  for (const voice of distinct('Voices')) {
    form.elements.voice.add(new Option(voice.replace('-', '–'), voice));
  }

  const sharedQuery = new URLSearchParams(location.search);
  for (const name of fields) {
    const input = form.elements.namedItem(name);
    if (sharedQuery.has(name)) input.value = sharedQuery.get(name);
  }

  function link(href, label) {
    const anchor = document.createElement('a');
    anchor.href = href;
    anchor.textContent = label;
    return anchor;
  }

  function scoreLinks(match) {
    const links = document.createElement('div');
    links.className = 'musical-search-score-links';
    const endpoint = new URL(api);
    for (const [edition, field, label, highlightLabel] of [
      ['no_edit', 'highlightPdf', 'PDF', 'Highlighted PDF'],
      ['edit', 'highlightPdfEdited', 'PDF with editorial accidentals', 'Highlighted PDF with editorial accidentals']
    ]) {
      const name = match.id + '-' + edition + '.pdf';
      const key = Object.hasOwn(assets.pdfs, name) ? assets.pdfs[name] : assets.generatedPdfs?.[match.id]?.[edition];
      if (key === null) continue;
      if (key) links.append(link(assetBase.replace(/\/$/, '') + '/' + key, label));
      if (typeof match[field] !== 'string') continue;
      let url;
      try { url = new URL(match[field], endpoint); } catch { continue; }
      if (url.origin === endpoint.origin && url.pathname === '/api/highlight-pdf' && url.searchParams.get('ticket')) {
        links.append(link(url.href, highlightLabel));
      }
    }
    for (const anchor of links.children) {
      anchor.target = '_blank';
      anchor.rel = 'noopener noreferrer';
    }
    return links;
  }

  function renderMatches() {
    const pages = Math.ceil(matches.length / pageSize);
    previous.disabled = page <= 1;
    next.disabled = page >= pages;
    pagination.hidden = pages < 2;
    document.getElementById('musical-search-page').textContent = 'Page ' + page + ' of ' + pages;
    list.replaceChildren();
    for (const match of matches.slice((page - 1) * pageSize, page * pageSize)) {
      const work = workById.get(match.id);
      const row = document.createElement('li');
      const heading = document.createElement('h3');
      const title = [work.Title, work.Subtitle].filter(Boolean).join(', ') || match.id;
      heading.append(link(workPath + '?id=' + encodeURIComponent(match.id), title));
      const details = document.createElement('p');
      details.className = 'musical-search-match-details';
      const measures = [...new Set(match.loc.flatMap(part =>
        part.loc.map(point => point.match(/=(\d+)/)?.[1]).filter(Boolean)))].sort(collator.compare);
      const location = measures.length ? (measures.length === 1 ? 'm. ' : 'mm. ') + measures.join(', ') : '';
      details.textContent = [work.Composer, count(match.count, 'match', 'matches'), location].filter(Boolean).join(' · ');
      row.append(heading, details, scoreLinks(match));
      list.append(row);
    }
  }

  function count(n, singular, plural) {
    return n.toLocaleString() + ' ' + (n === 1 ? singular : plural);
  }

  function showResults(payload) {
    matches = payload.locations.filter(match => workById.has(match.id));
    const matchCount = matches.reduce((sum, match) => sum + match.count, 0);
    const workCount = new Set(matches.map(match => match.id.replace(/(?<=\d)[a-z](?:\.[A-Za-z0-9]+)?$/, ''))).size;
    document.getElementById('musical-search-count').textContent = matchCount
      ? count(matchCount, 'match', 'matches') + ' in ' + count(workCount, 'work', 'works')
      : 'No matches found.';
    document.getElementById('musical-search-share').replaceChildren();
    page = 1;
    results.hidden = false;
    renderMatches();
    resultsTitle.focus();
  }

  async function runSearch(event) {
    event.preventDefault();
    if (pending) return;
    const query = new URLSearchParams();
    for (const name of fields) {
      const value = form.elements.namedItem(name).value.trim();
      if (value) query.set(name, value);
    }
    if (!fields.slice(0, 3).some(name => query.has(name))) {
      status.textContent = 'Enter a pitch, interval, or rhythm pattern.';
      return;
    }
    if (!token) {
      status.textContent = 'Please complete verification before searching.';
      return;
    }

    const url = new URL(location.href);
    url.search = query.toString();
    history.replaceState(null, '', url);
    const body = new URLSearchParams(query);
    body.set('a', 'search');
    body.set('cf-turnstile-response', token);
    token = '';
    pending = submit.disabled = true;
    results.hidden = true;
    status.textContent = 'Searching…';
    const controller = new AbortController();
    const timer = setTimeout(() => controller.abort(), 125000);
    let errorMessage = '';
    try {
      const response = await fetch(api, {
        method: 'POST', body, signal: controller.signal, cache: 'no-store', credentials: 'omit'
      });
      const payload = await response.json();
      if (!response.ok) throw new Error(payload.error || 'Search is temporarily unavailable.');
      if (!Array.isArray(payload.locations)) throw new Error('Search returned an unexpected response.');
      if (payload.locations.some(match => match.corpus !== '1520s')) {
        throw new Error('Search returned results from an unexpected corpus.');
      }
      showResults(payload);
    } catch (error) {
      errorMessage = error.name === 'AbortError' ? 'Search took too long. Please narrow the query.'
        : error instanceof TypeError || error instanceof SyntaxError ? 'Search is temporarily unavailable.'
        : error.message;
    } finally {
      clearTimeout(timer);
      pending = submit.disabled = false;
      window.turnstile.reset(widget);
      status.textContent = errorMessage;
    }
  }

  form.addEventListener('submit', runSearch);
  for (const [button, step] of [[previous, -1], [next, 1]]) {
    button.addEventListener('click', () => {
      page += step;
      renderMatches();
      resultsTitle.focus();
    });
  }
  document.getElementById('musical-search-copy').addEventListener('click', async () => {
    const shareStatus = document.getElementById('musical-search-share');
    try {
      await navigator.clipboard.writeText(location.href);
      shareStatus.textContent = 'Search link copied.';
    } catch {
      const shareLink = document.createElement('input');
      shareLink.value = location.href;
      shareLink.readOnly = true;
      shareLink.setAttribute('aria-label', 'Search link');
      shareStatus.replaceChildren('Copy this search link ', shareLink);
      shareLink.focus();
      shareLink.select();
    }
  });

  function renderVerification() {
    widget = window.turnstile.render(verification, {
      sitekey, action: '1520s-search', appearance: 'always', 'response-field': false,
      size: verification.clientWidth < 300 ? 'compact' : 'normal',
      callback(value) {
        token = value;
        if (status.textContent === 'Please complete verification before searching.') status.textContent = '';
      },
      'expired-callback'() {
        token = '';
        if (!pending) status.textContent = 'Verification expired. Please verify again.';
      },
      'error-callback'() {
        token = '';
        if (!pending) status.textContent = 'Verification failed. Please reload to try again.';
        return true;
      }
    });
  }
  if (window.turnstile) {
    renderVerification();
  } else {
    const script = document.createElement('script');
    script.src = 'https://challenges.cloudflare.com/turnstile/v0/api.js?render=explicit';
    script.async = true;
    script.onload = renderVerification;
    script.onerror = () => { status.textContent = 'Verification could not load. Please reload to try again.'; };
    document.head.append(script);
  }
}
