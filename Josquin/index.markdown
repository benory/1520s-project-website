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

<div class="page-wrapper">
<div class="page-header">
  <h1>Josquin Attribution Table</h1>
</div>

<div class="description">This page serves as an appendix to the article "Josquin Attributions by the Numbers," which will be published in the volume <i>Josquin: A New Approach</i>. The assembled data set accounts for 2,593 individual appearances of works in some 708 sources ca. 1471–1660, where for any given work at least one source attributes it to Josquin.<br><br>

Data is drawn from the <i>New Josquin Edition</i> and from the tiered works list published by Jesse Rodin and Joshua Rifkin in "The Josquin Canon at 500 with an Appendix Produced in Collaboration with Joshua Rifkin," <i>Early Music</i> 49 (2021): 473–97.<br><br>

<a href="/Josquin/Josquin.csv" download>Download the dataset as a CSV file</a> (last updated {{ site.time | date: "%d %B %Y" }}).</div>

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
</div>