---
layout: page
title: browse scores
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

<input type="text" id="input" onkeyup="FreeTextSearch()" placeholder="Enter title, composer, source, or date"><span id="search-count"></span>

<div id="search-interface"></div>

<div id="list"></div>



