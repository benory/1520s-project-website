---
layout: work
---

{% include_relative styles-local.html %}
{% assign error_report = site.error_report %}

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
    <div id="audiobutton-container" hidden>
        <button type="button" id="audiobutton-toggle" class="audio-toggle" aria-label="Play" title="Play" data-playing="false" onclick="togglePlayPauseOfAudio()">
            <svg class="audio-icon audio-icon-play" viewBox="0 0 20 20" aria-hidden="true" focusable="false"><path d="M6 3.5L16 10L6 16.5Z" /></svg>
            <svg class="audio-icon audio-icon-pause" viewBox="0 0 20 20" aria-hidden="true" focusable="false"><rect x="4" y="3.5" width="4" height="13" rx="1" /><rect x="12" y="3.5" width="4" height="13" rx="1" /></svg>
        </button>
    </div>
    <div id="accidentalSelect">
        <button type="button" id="editorial-accidentals" class="accidentals-switch" role="switch" aria-checked="true" onclick="this.getAttribute('aria-checked') === 'true' ? displayNoAccidentals() : displayAccidentals()">
            <span class="switch-track" aria-hidden="true"></span>Editorial accidentals
        </button>
    </div>
    <button type="button" id="activity" hidden data-analysis-group="activity" class="analysis-toggle button" aria-expanded="false" aria-controls="activity-display"><svg class="toolbar-icon" viewBox="0 0 24 24" aria-hidden="true"><path d="M4 18V12M9 18V6M14 18V9M19 18V3"/></svg>Activity plots</button>
    <button type="button" id="prange" hidden data-analysis-group="vocal-ranges" class="analysis-toggle button" aria-expanded="false" aria-controls="prange-display"><svg class="toolbar-icon" viewBox="0 0 24 24" aria-hidden="true"><path d="M6 5v14M3 5h6M3 19h6M17 8v8M14 8h6M14 16h6"/></svg>Vocal ranges</button>
    <button type="button" id="autocadence-filter" class="filter-toggle button" aria-pressed="false" onclick="toggleAutocadenceFilter()"><svg class="toolbar-icon" viewBox="0 0 24 24" aria-hidden="true"><path d="M13 17l4-3 4 3-4 3-4-3M17 14V2M4 8v12M8 6v12M2 12l8-2M2 17l8-2"/></svg>Cadence finder</button>
    <button type="button" id="error-report-open" class="button error-report-open" aria-haspopup="dialog" aria-controls="error-report-modal"><svg class="toolbar-icon" viewBox="0 0 24 24" aria-hidden="true"><path d="M5 21V4m0 1c5-4 9 4 14 0v10c-5 4-9-4-14 0"/></svg>Report an error</button>
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

<div class="work-credit-row">
    <div id="score-credit" class="work-score-credit"></div>
    <button type="button" id="citation-open" class="citation-open" aria-haspopup="dialog" aria-controls="citation-dialog" hidden>
        <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path d="M7 4h12a3 3 0 0 1 3 3v2h-5V7a3 3 0 0 1 3-3M7 4a3 3 0 0 0-3 3v10H2v2a3 3 0 0 0 3 3h12a3 3 0 0 0 3-3v-2h-4M20 9v8M4 17h12v2a3 3 0 0 1-3 3M8 9h5M8 13h5" /></svg>
        <span><strong>Cite</strong> this work</span>
    </button>
</div>

<dialog id="citation-dialog" class="citation-dialog" aria-labelledby="citation-heading">
    <div class="error-report-header">
        <h2 id="citation-heading">Suggested citation</h2>
        <button type="button" id="citation-close" class="error-report-close" aria-label="Close citation">&times;</button>
    </div>
    <div class="citation-format-control">
        <select id="citation-format" class="button" aria-label="Citation format">
            <option value="note" selected>Chicago footnote format</option>
            <option value="bibliography">Chicago bibliography format</option>
        </select>
    </div>
    <p id="citation-text" class="citation-text"></p>
    <div class="citation-actions">
    <button type="button" id="citation-copy" class="button">
        <svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><rect x="8" y="8" width="12" height="13" rx="2"/><path d="M16 8V5a2 2 0 0 0-2-2H5a2 2 0 0 0-2 2v9a2 2 0 0 0 2 2h3"/></svg>
        Copy citation
    </button>
    <p id="citation-status" class="citation-status" role="status"></p>
    </div>
</dialog>

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
{% include_relative citation.html %}
{% include styles/svgdefs.html %}
