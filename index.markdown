---
layout: page
---

{% include_relative styles-local.html %}
{% include_relative scripts-local.html %}
{% include styles/styles-common.css.html %}

<section class="home-hero" aria-labelledby="home-hero-title">
  <div class="home-hero-copy">
    <h1 class="home-hero-title" id="home-hero-title">Explore and listen to European polyphonic music, <span class="home-date-range">ca. 1510–1540</span></h1>
  </div>
  <figure class="home-hero-artwork">
    <img src="{{ '/images/willaert-enixa-source.jpg' | relative_url }}" alt="Opening of Adrian Willaert’s Enixa est puerpera in Selectissimae necnon familiarissimae cantiones, Augsburg, 1540" width="1080" height="651" fetchpriority="high">
    <figcaption>The motet <em>Enixa est puerpera</em> by Adrian Willaert in <em>Selectissimae necnon familiarissimae cantiones</em> (Augsburg: Melchior Kriesstein, RISM 1540<sup>7</sup>)</figcaption>
  </figure>
  <section class="home-search" aria-labelledby="home-search-heading">
    <h2 id="home-search-heading">Search</h2>
    <form class="browse-box apple-search" action="{{ '/repertoire/' | relative_url }}" method="get" role="search">
      <div class="home-search-field">
        <input type="search" id="input" name="q" aria-label="Search composers, works, genres" placeholder="Search composers, works, genres…" autocomplete="off">
        <button type="submit">Search</button>
      </div>
      <div id="search-suggestions" class="search-suggestions hidden"></div>
    </form>
  </section>
</section>

<div class="homepage-grid">
  <section class="left-column" aria-labelledby="project-data-heading">
    <h2 id="project-data-heading">Project Data</h2>
    <div class="data-box apple-data">
      <div class="data-metrics">
        <div class="metric"><div class="metric-value" id="work-count"></div><div class="metric-label">Works</div></div>
        <div class="metric"><div class="metric-value" id="note-count"></div><div class="metric-label">Notes</div></div>
      </div>
      <div class="data-genres">
        <div class="genre-row"><span class="genre-count" id="mass-count"></span><span class="genre-label">Mass movements</span></div>
        <div class="genre-row"><span class="genre-count" id="motet-count"></span><span class="genre-label">Motets</span></div>
        <div class="genre-row"><span class="genre-count" id="secular-count"></span><span class="genre-label">Secular works</span></div>
      </div>
    </div>
  </section>
  <section class="right-column" aria-labelledby="composers-heading">
    <h2 id="composers-heading">Best-Represented Composers</h2>
    <div id="composer-plot"></div>
  </section>
</div>

<section class="home-recent" aria-labelledby="recent-works-heading">
  <h2 id="recent-works-heading">Recently added works</h2>
  <div data-count="10" id="general"></div>
  <a class="recent-works-more" href="{{ '/recently_added/' | relative_url }}">More works added by date <span aria-hidden="true">↗</span></a>
</section>
