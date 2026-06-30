---
layout: work
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

<div id="button-container" class="button-container">
    <div id="audiobutton-container">
        <span id="audiobutton-play" class="play" onclick="DATA1520.audio.play();">play</span>
        <span id="audiobutton-pause" class="pause hidden" onclick="DATA1520.audio.pause();">pause</span>
    </div>
    <div id="accidentalSelect">
       <button type="button" class="button hide" onclick="displayNoAccidentals()">Hide Editorial Accidentals</button>
       <button type="button" class="button show hidden" onclick="displayAccidentals()">Show Editorial Accidentals</button>
    </div>
    <button type="button" id="activity" data-analysis-group="activity" class="analysis-toggle button" aria-expanded="false" aria-controls="activity-display">Activity plots</button>
    <button type="button" id="prange" data-analysis-group="vocal-ranges" class="analysis-toggle button" aria-expanded="false" aria-controls="prange-display">Vocal ranges</button>
</div>

<div id="analysis-plots">
	<div id="activity-display" class="analysis-plot analysis-panel activity-analysis-plot hidden">
		<div class="work-activity-controls">
			<label class="work-range-mode-toggle">
				<span class="work-range-mode-label is-active" data-activity-label="merged">Combined</span>
				<input id="work-activity-mode" type="checkbox" aria-label="Switch activity plots between combined and by voice">
				<span class="work-range-mode-switch" aria-hidden="true"></span>
				<span class="work-range-mode-label" data-activity-label="separate">By voice</span>
			</label>
		</div>
		<div id="activity-merged-notitle-display" class="activity-plot"></div>
		<div id="activity-separate-notitle-display" class="activity-plot hidden"></div>
	</div>
	<div id="prange-display" class="analysis-plot analysis-panel range-analysis-plot hidden">
		<div class="work-range-controls">
			<label class="work-range-mode-toggle">
				<span class="work-range-mode-label is-active" data-range-label="attack">Note counts</span>
				<input id="work-range-mode" type="checkbox" aria-label="Switch vocal ranges between note counts and durations">
				<span class="work-range-mode-switch" aria-hidden="true"></span>
				<span class="work-range-mode-label" data-range-label="duration">Durations</span>
			</label>
		</div>
		<details class="analysis-help-note">
			<summary>About these plots</summary>
			<p>Large black noteheads mark each voice's lowest and highest pitches; the small white notehead marks the median, and gray noteheads mark final notes. <i>Note counts</i> weights pitches by attacks, while <i>Durations</i> weights them by total sounding duration. Flats appear in dark red/brown and sharps in blue. Hover over a histogram bar to see the count or duration it represents.</p>
		</details>
		<div id="prange-attack-display" class="range-plot"></div>
		<div id="prange-duration-display" class="range-plot hidden"></div>
	</div>
</div>

<script type="text/x-humdrum" id="my-score"></script>

<div id="work-footer"></div>

{% include_relative listeners.html %}
{% include_relative scripts-local.html %}
{% include styles/svgdefs.html %}
