---
layout: work
vim:    ts=3:nowrap
---

{% include_relative styles-local.html %}

<script async src="https://www.googletagmanager.com/gtag/js?id=G-38882FHV3H"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());

  gtag('config', 'G-38882FHV3H');
</script>

<audio id="audio"></audio>

<table id="work-info">
   <thead>
       <tr>
           <th class="left-column">Left Column</th>
           <th class="middle-column">Middle Column</th>
           <th class="right-column">Right Column</th>
       </tr>
   </thead>
   <tbody id="work-info-body"></tbody>
</table>

<div id="external-info"></div>

<div id="analysis-plots">
	<div id="activity-merged-notitle-display" class="analysis-plot hidden"></div>
	<div id="activity-separate-notitle-display" class="analysis-plot hidden"></div>
	<div id="prange-duration-display" class="analysis-plot hidden"></div>   
</div>

<div id="button-container" class="button-container">
    <div id="audiobutton-container">
        <span id="audiobutton-play" class="play" onclick="DATA1520.audio.play();">play</span>
        <span id="audiobutton-pause" class="pause hidden" onclick="DATA1520.audio.pause();">pause</span>
    </div>
    <div id="accidentalSelect">
       <div class="button hide" onclick="displayNoAccidentals()">Hide Editorial Accidentals</div>
       <div class="button show hidden" onclick="displayAccidentals()">Show Editorial Accidentals</div>
    </div>
    <div id="activity-merged-notitle" data-ext="png" class="analysis-toggle button">Activity</div>
    <div id="activity-separate-notitle" data-ext="png" class="analysis-toggle button">Activity by voice</div>
    <div id="prange-duration" data-ext="svg" class="analysis-toggle button">Vocal ranges by note durations</div>
</div>

<script type="text/x-humdrum" id="my-score"></script>

<div id="work-footer"></div>

{% include_relative listeners.html %}
{% include_relative scripts-local.html %}
{% include styles/svgdefs.html %}



