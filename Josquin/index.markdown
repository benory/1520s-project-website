---
# Feel free to add content and custom Front Matter to this file.
# To modify the layout, see https://jekyllrb.com/docs/themes/#overriding-theme-defaults

layout: page
permalink: /Josquin/
nav: false

---

{% include_relative styles-local.html %}
{% include_relative scripts-local.html %}
{% include styles/styles-common.css.html %}

<div class="section-header page-title"><h4>Josquin Attributions by the Numbers</h4></div>

<div class="josquin-introduction">
<p>This page serves as an appendix to the article "Josquin Attributions by the Numbers," which will be published in the volume <i>Josquin in Focus</i>. The assembled data set accounts for 2,600 individual appearances of works in some 708 sources ca. 1471–1660, where for any given work at least one source attributes it to the composer Josquin des Prez. A majority of attributions to the composer circulate during this project's period of focus: three-quarters of Josquin attributions postdate his death in 1521; nearly sixty percent appear ca. 1520–60.</p>
<p>Data is drawn from the <i>New Josquin Edition</i> (NJE) and the tiered works list published by Jesse Rodin and Joshua Rifkin in "The Josquin Canon at 500 with an Appendix Produced in Collaboration with Joshua Rifkin," <i>Early Music</i> 49 (2021): 473–97. Thanks to Brett Kostrzewski for his assistance in checking source dates and origins.</p>
</div>

<p class="dataset-download"><a class="dataset-download-button" href="/Josquin/Josquin.csv" download>Download the dataset as a CSV file</a><span>(last updated {{ site.data.Josquin.csv_metadata.last_updated }}).</span></p>

<div id="search-interface" class="catalogue-toolbar">
  <div class="row">
    <div class="left-group">
      <input type="text" id="input" aria-label="Search Josquin attributions" onkeyup="FreeTextSearch()" placeholder="Search source, date, composer...">
      <div class="search-meta">
        <span id="search-count"></span>
      </div>
    </div>
    <div class="right-group">
      <div id="dropdowns">
        <div class="top-line">
          <div id="source-type-container">
            <select id="filter-source-type" onchange="FreeTextSearch()">
              <option value="">All source types</option>
            </select>
          </div>
          <div id="attribution-category-container">
            <select id="filter-attribution-category" onchange="FreeTextSearch()">
              <option value="">All attribution categories</option>
            </select>
          </div>
        </div>
        <div class="bottom-line">
          <div id="source-genre-container">
            <select id="filter-source-genre" onchange="FreeTextSearch()">
              <option value="">All genres</option>
            </select>
          </div>
          <div id="josquin-attribution-container">
            <select id="filter-josquin" onchange="FreeTextSearch()">
              <option value="">Attributed to Josquin?</option>
            </select>
          </div>
        </div>
      </div>
    </div>
  </div>
  <details class="attribution-key" id="attribution-key">
    <summary>On attribution categories</summary>
    <div class="attribution-key-content">
      <dl>
        <div><dt>1 <span>(I)</span></dt><dd><strong>The core group.</strong> Works securely attributed to Josquin.</dd></div>
        <div><dt>2 <span>(II)</span></dt><dd><strong>Provisional acceptance.</strong> A combination of source and stylistic evidence supports provisional acceptance.</dd></div>
        <div><dt>3 <span>(III)</span></dt><dd><strong>Problematic.</strong> Works for which Josquin's authorship ranges from unlikely to possible.</dd></div>
        <div><dt>4a <span>(IVa)</span></dt><dd><strong>No convincing argument at present</strong> for Josquin's authorship.</dd></div>
        <div><dt>4b <span>(IVb)</span></dt><dd><strong>Another named composer.</strong> Works almost certainly by another named composer.</dd></div>
      </dl>
      <p>Categories follow the appendix to Jesse Rodin's <a href="https://academic.oup.com/em/article/49/4/473/6507395" target="_blank" rel="noopener">“The Josquin Canon at 500”</a> (2021), pp. 482–97.</p>
    </div>
  </details>
</div>

<div id="list"></div>

{% include_relative table-enhancements.html %}
