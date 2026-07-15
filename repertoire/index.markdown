---
layout: page
title: repertoire
order: 2

---

{% include_relative styles-local.html %}
{% include_relative scripts-local.html %}
{% include styles/styles-common.css.html %}

<div class="section-header"><h4>Repertoire</h4></div>

<div id="search-interface" class="catalogue-toolbar">
  <div class="row">
    <div class="left-group">
      <input type="text" id="input" aria-label="Search repertoire" onkeyup="FreeTextSearch()" placeholder="Search title, composer, source...">
      <div class="search-meta">
        <span id="search-count"></span>
      </div>
    </div>
    <div class="right-group">
      <div id="dropdowns">
        <div class="top-line">
          <div id="composer-container"></div>
          <div id="year-container"></div>
          <div id="genre-container"></div>
          <div id="voice-container"></div>
        </div>
        <div class="bottom-line">
          <div id="source-container"></div>
          <div id="mensuration-container"></div>
          <div id="texted-container"></div>
        </div>
      </div>
      <div id="mensuration-selected-container"></div>
    </div>
  </div>
</div>
<div id="list"></div>
