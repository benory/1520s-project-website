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

<div class="browse-data-wrapper">
  <div class="browse-box">
    <h4>Browse scores</h4>
    <div class="search-container">
      <input type="text" id="input" placeholder="Search the project">
      <span onclick="UserSearch()" class="button" id="inputbutton">Enter</span>
    </div>
  </div>
  <div class="data-box">
    <h4>Project data</h4>
    <ul>
      <li><b>Number of works:</b> <span id="work-count"></span></li>
      <li><b>Number of notes:</b> <span id="note-count"></span></li>
      <li>
        <b>By genre:</b> 
        <span class="count-box">
          <span id="mass-count"></span> mass movements<br>
          <span id="motet-count"></span> motets<br>
          <span id="secular-count"></span> secular works
        </span>
      </li>
    </ul>
  </div>
</div>

<div id="composer-plot"></div>

<div class="most-recent-header"><h4>Recently added works</h4></div>
<div data-count="10" id="most-recent"><a href="recently_added">More works added by date</a></div>