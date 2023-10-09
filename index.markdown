---
# Feel free to add content and custom Front Matter to this file.
# To modify the layout, see https://jekyllrb.com/docs/themes/#overriding-theme-defaults

layout: page
---

<script src="https://cdn.jsdelivr.net/npm/vega@5.25.0"></script>
<script src="https://cdn.jsdelivr.net/npm/vega-lite@5.15.1"></script>
<script src="https://cdn.jsdelivr.net/npm/vega-embed@6.22.2"></script>

{% include_relative styles-local.html %}
{% include_relative scripts-local.html %}

![1520s Project banner](/images/1520s_banner.png)

The 1520s Project is an open-source repository of more than <span id="roundwork-count"></span> scores of European polyphonic music, ca. 1510–1540. It seeks to address how, when, and where a radically new style of polyphonic music emerged in the 1520s. Read [about the project](about) or [browse the project's scores](browse). <br><br>

<input type="text" id="input" placeholder="Search the project"><span onclick="UserSearch()" class="button" id="inputbutton">Enter</span>

#### Project data
+ Number of works: <span id="work-count"></span>
+ Number of notes: <span id="note-count"></span>
+ By genre: <span id="mass-count"></span> mass movements, <span id="motet-count"></span> motets, <span id="secular-count"></span> secular works

<div data-threshold="10" id="composer-plot"></div>

#### Recently added works
<div data-count="10" id="most-recent"></div>

For complementary repertoire spanning ca. 1420–1520, see the [Josquin Research Project](http://josquin.stanford.edu){:target="_blank"}. For more information on the collaboration between the projects, see [about this project](about).