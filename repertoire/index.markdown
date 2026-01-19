---
layout: page
title: repertoire
order: 3

---

<script async src="https://www.googletagmanager.com/gtag/js?id=G-38882FHV3H"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());

  gtag('config', 'G-38882FHV3H');
</script>

{% include_relative styles-local.html %}
{% include_relative scripts-local.html %}
{% include styles/most_recent_table.css.html %}

<div class="section-header"><h4>Repertoire</h4></div>

<div class="browse-page">
  <div class="page-wrapper">
    <div id="search-interface">
      <div class="top-row">
        <div class="left-search-group">
          <input type="text" id="input" onkeyup="FreeTextSearch()" placeholder="Enter title, composer, etc.">
          <span id="search-count"></span>
        </div>
        <div class="top-section">
          <div id="top-dropdowns">
            <div class="top-line">
              <div id="composer-container"></div>
              <div id="genre-container"></div>
              <div id="year-container"></div>
            </div>
            <div class="bottom-line">
              <div id="voice-container"></div>
              <div id="source-container"></div>
            </div>
          </div>
          <div class="mensuration-right"></div>
        </div>
      </div>
    </div>
    <div id="list"></div>
  </div>
</div>