---
# Feel free to add content and custom Front Matter to this file.
# To modify the layout, see https://jekyllrb.com/docs/themes/#overriding-theme-defaults

layout: page
permalink: /Josquin/
nav: false

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
{% include styles/styles-common.css.html %}

<div class="section-header"><h4>Josquin attributions by the numbers</h4></div>

<p>This page serves as an appendix to the article "Josquin Attributions by the Numbers," which will be published in the volume <i>Josquin: A New Approach</i>. The assembled data set accounts for 2,593 individual appearances of works in some 708 sources ca. 1471–1660, where for any given work at least one source attributes it to the composer Josquin des Prez. A majority of attributions to the composer circulate during this project's period of focus: three-quarters of Josquin attributions postdate his death in 1521; nearly sixty percent appear ca. 1520–60.</p>
<p>Data is drawn from the <i>New Josquin Edition</i> (NJE) and the tiered works list published by Jesse Rodin and Joshua Rifkin in "The Josquin Canon at 500 with an Appendix Produced in Collaboration with Joshua Rifkin," <i>Early Music</i> 49 (2021): 473–97. Thanks to Brett Kostrzewski for his assistance in checking source dates and origins.</p>

<a href="/Josquin/Josquin.csv" download>Download the dataset as a CSV file</a> (last updated {{ site.data.Josquin.csv_metadata.last_updated }}).

<div id="search-interface">
  <div id="search-top">
    <input type="text" id="input" onkeyup="FreeTextSearch()" placeholder="Enter source, date, composer">
    <span id="search-count"></span>
  </div>
  <div id="filter-bar">
    <div class="filter-group">
      <select id="filter-source-type" onchange="FreeTextSearch()">
        <option value="">Source Type</option>
      </select>
      <select id="filter-attribution-category" onchange="FreeTextSearch()">
        <option value="">Attribution Category</option>
      </select>
    </div>
    <div class="filter-group">
      <select id="filter-source-genre" onchange="FreeTextSearch()">
        <option value="">Genre</option>
      </select>
      <select id="filter-josquin" onchange="FreeTextSearch()">
        <option value="">Attributed to Josquin?</option>
      </select>
    </div>
  </div>
</div>

<div id="list"></div>