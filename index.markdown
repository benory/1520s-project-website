---
# Feel free to add content and custom Front Matter to this file.
# To modify the layout, see https://jekyllrb.com/docs/themes/#overriding-theme-defaults

layout: page
---

<script src="https://cdn.jsdelivr.net/npm/vega@5.25.0"></script>
<script src="https://cdn.jsdelivr.net/npm/vega-lite@5.15.1"></script>
<script src="https://cdn.jsdelivr.net/npm/vega-embed@6.22.2"></script>
<script async src="https://www.googletagmanager.com/gtag/js?id=G-38882FHV3H"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());

  gtag('config', 'G-38882FHV3H');
</script>


{% include_relative styles-local.html %}
{% include_relative scripts-local.html %}
{% include styles/styles-common.css.html %}

<div class="homepage-grid">

  <!-- LEFT COLUMN -->
  <div class="left-column">
    <div class="section-header"><h4>Browse</h4></div>
    <div class="browse-box apple-search">
      <input
        type="search"
        id="input"
        placeholder="Search composers, works, genres…"
        autocomplete="off"
      >
      <div id="search-suggestions"
           class="search-suggestions hidden"></div>
    </div>
    <div class="section-header"><h4>Project Data</h4></div>
    <div class="data-box apple-data">
      <div class="data-metrics">
        <div class="metric">
          <div class="metric-value" id="work-count"></div>
          <div class="metric-label">Works</div>
        </div>
        <div class="metric">
          <div class="metric-value" id="note-count"></div>
          <div class="metric-label">Notes</div>
        </div>
      </div>
      <div class="data-genres">
        <div class="genre-row">
          <span class="genre-count" id="mass-count"></span>
          <span class="genre-label">Mass movements</span>
        </div>
        <div class="genre-row">
          <span class="genre-count" id="motet-count"></span>
          <span class="genre-label">Motets</span>
        </div>
        <div class="genre-row">
          <span class="genre-count" id="secular-count"></span>
          <span class="genre-label">Secular works</span>
        </div>
      </div>
    </div>
  </div>

  <!-- RIGHT COLUMN -->
  <div class="right-column">
    <div class="section-header"><h4>Best-Represented Composers</h4></div>
    <div id="composer-plot"></div>
  </div>

</div>

<div class="section-header"><h4>Recently added works</h4></div>
<div data-count="10" id="most-recent"><a href="recently_added">More works added by date</a></div>