---
layout: work
vim:    ts=3:nowrap
---

{% include_relative styles-local.html %}

<!-- AUDIO NEEDS TO BE IN A CONTAINER FOR SOME REASON (something is trying to replace it plus siblings, erasing other conetent below -->
<span><audio id="audio"></span>

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

<br>

<div id="external-info"></div>

<div id="analysis-plots">
	<div id="activity-merged-notitle-display" class="analysis-plot hidden"></div>
	<div id="activity-separate-notitle-display" class="analysis-plot hidden"></div>
	<div id="prange-duration-display" class="analysis-plot hidden"></div>   
</div>

<div id="button-container" class="button-container">
    <span id="audiobutton" data-id="" style="cursor:hand; cursor:pointer;" onclick="DATA1520.audio.play();" href="" class="play">play</span>
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



