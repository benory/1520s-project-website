---
layout: work
---

{% include_relative styles-local.html %}
{% assign error_report = site.error_report %}
{% if error_report.turnstile_sitekey %}
<script src="https://challenges.cloudflare.com/turnstile/v0/api.js" async defer></script>
{% endif %}

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
    <button type="button" id="autocadence-filter" class="filter-toggle button" aria-pressed="false" onclick="toggleAutocadenceFilter()">Automatic Cadence Finder</button>
    <button type="button" id="error-report-open" class="button error-report-open" aria-haspopup="dialog" aria-controls="error-report-modal">Report an error</button>
</div>

<div id="error-report-modal" class="error-report-modal hidden" role="dialog" aria-modal="true" aria-labelledby="error-report-title" aria-describedby="error-report-intro">
    <div class="error-report-backdrop" data-error-report-close></div>
    <div class="error-report-dialog" tabindex="-1">
        <div class="error-report-header">
            <h2 id="error-report-title">Report an error</h2>
            <button type="button" class="error-report-close" aria-label="Close error report form" data-error-report-close>&times;</button>
        </div>
        <p id="error-report-intro" class="error-report-intro">Use this form to report a problem with this work's score, metadata, audio, downloads, or page display. Fields marked * are required.</p>

        <form
            id="error-report-form"
            class="error-report-form"
            action="{{ error_report.worker_url | escape }}"
            method="POST"
            novalidate
        >
            <input type="hidden" name="category" value="Error report">

            <div class="error-report-field error-report-target-field">
                <span class="error-report-label">Work or page being reported</span>
                <p id="error_report_target_display" class="error-report-target-display"></p>
                <input
                    id="error_report_target"
                    name="target"
                    type="hidden"
                    value=""
                >
            </div>

            <div class="error-report-field">
                <label for="error_report_description">Description *</label>
                <textarea
                    id="error_report_description"
                    name="description"
                    rows="5"
                    required
                    placeholder="Describe the problem..."
                ></textarea>
            </div>

            <div class="error-report-field">
                <label for="error_report_email">Email address *</label>
                <input
                    id="error_report_email"
                    name="email"
                    type="email"
                    required
                    autocomplete="email"
                    placeholder="you@example.com"
                >
            </div>

            {% if error_report.turnstile_sitekey %}
            <div class="error-report-field error-report-field--turnstile">
                <div
                    class="cf-turnstile"
                    data-sitekey="{{ error_report.turnstile_sitekey | escape }}"
                ></div>
            </div>
            {% else %}
            <div class="error-report-config-note" role="note">Cloudflare Turnstile will appear here after the site key is configured.</div>
            {% endif %}

            <input id="error_report_user_agent" type="hidden" name="user_agent" value="">

            <div class="error-report-actions">
                <button type="button" class="button error-report-cancel" data-error-report-close>Cancel</button>
                <button type="submit" class="button error-report-submit">Submit report</button>
            </div>

            <div id="error-report-status" class="error-report-status" aria-live="polite"></div>
        </form>

        <div id="error-report-success" class="error-report-success hidden" tabindex="-1">
            <p id="error-report-success-message" class="error-report-success-message">Thank you for your report.</p>
            <p class="error-report-success-instruction">Please close this popup to return to the work page.</p>
        </div>
    </div>
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
