---
layout: page
title: browse
permalink: /browse/
---

<div id="search-interface"></div>

<div id="list"></div>

<style>
	body {font: 400 12px/1.25 -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif,"Apple Color Emoji","Segoe UI Emoji","Segoe UI Symbol"}
	h1 { font-size: 40px; }
	th { text-align: left; }
	table.browse { min-width: 1000px; white-space: nowrap;}
	table.browse { margin-left: auto; margin-right: auto; } /* center table */
	table.browse { border-collapse: collapse; } /* don't put gaps between cells */
	table.browse th { background:skyblue; }
	table.browse td, table.browse th { padding-left: 2px; padding-top: 2px; padding: 2px}
	table.browse tr:hover { background:#ff000011; }
	a { text-decoration: none; }
	#search-interface { margin-bottom: 30px; }
	.wrapper {margin-left: 10px;}
</style>

<script>
// vim: ts=3:nowrap

let METADATA = [];
let INDEX_id         	  = "ID";
let INDEX_composer    	  = "Composer";
let INDEX_title       	  = "Title";
let INDEX_genre      	  = "Genre";
let INDEX_voice      	  = "Voices";
let INDEX_firstsourcedate = "First Source Date";
let INDEX_firstsource 	  = "First Source";
let INDEX_RISMlink 	  	  = "RISM Source Link";
let INDEX_DIAMMlink	  	  = "DIAMM source link";

document.addEventListener("DOMContentLoaded", function () {
	var id = "AKfycbybB9k5Omv7Fv_e5qpLyjPXwZgJbRxSk4Fn9ZgXp3Nl7sR9JTSac-yauOKKK4aldNo48Q";
	var url = `https://script.google.com/macros/s/${id}/exec`;

	fetch(url)
	.then((response) => response.json())
	.then((data) => {
		METADATA = data;
		buildSearchInterface(data, "#search-interface");
		displayBrowseTable(data, "#list"); 
	})
	.catch((error) => console.error("Error downloading metadata: ", error));

});


//////////////////////////////
//
// buildSearchInterface --
//

function buildSearchInterface(data, selector) {
	if (!selector) {
		selector = "#search-interface";
	}
	let element = document.querySelector(selector);
	if (!element) {
		console.error(`Error: cannot find ${selector} element to create search interface`);
		return;
	}
	let output = "";
	output += buildComposerSelect(data);
	output += buildVoiceSelect(data);
	output += buildYearSelect(data);
	output += buildGenreSelect(data);
	output += buildSourceSelect(data);
	element.innerHTML = output;
}



//////////////////////////////
//
// displayBrowseTable --
//

function displayBrowseTable(data, selector) {
	if (!selector) {
		selector = "#list";
	}
	let element = document.querySelector(selector);
	if (!element) {
		console.error(`Error: cannot find ${selector} element to display work table`);
		return;
	}
	let headings = [INDEX_composer, INDEX_title, INDEX_genre, INDEX_voice, INDEX_firstsource, INDEX_firstsourcedate];
	let contents = "";
	contents += "<table class='browse'>\n";
	contents += "<thead>\n";
	contents += makeTableHeader(headings);
	contents += "</thead>\n";
	contents += "<tbody>\n";
	contents += makeTableBody(headings, data);
	contents += "</tbody>\n";
	contents += "</table>\n";
	element.innerHTML = contents;
}

//////////////////////////////
//
// makeTableHeader -- Generate HTML content for browse table header.
//

function makeTableHeader(headings) {
	let output = `<th>${headings.join("</th><th>")}</th>\n`;
	return output;
}



//////////////////////////////
//
// makeTableBody -- Generate HTML content for browse table's body.
//

function makeTableBody(headings, data) {
	let output = "";
	for (let i=0; i<data.length; i++) {
		let entry = data[i];
		output += "<tr>";
				for (let i=0; i<headings.length; i++) {
			let value = "";
			if (typeof entry[headings[i]] !== "undefined") {
				value = entry[headings[i]];
			}
			output += "<td>";
			if (headings[i] == INDEX_title) {
				let title = getTitle(entry);
				output += title;
			}
			else if (headings[i] == INDEX_firstsource) {
				let url = getSource(entry);
				let sourcevalue = value;
				output += `<a target="_blank" href="${url}">${sourcevalue}</a>`;
			}
			else {
				output += value;
			}
			output += "</td>";
		}
		output += "</tr>\n";
	}
	return output;
}

//////////////////////////////
//
// getTitle -- Generate Title + Subtitle 
//

function getTitle(entry) {
	console.warn(entry);
	let title = "";
	if (typeof entry["Title"] !== "undefined") {
		title = entry["Title"];
	}
	let subtitle = "";
	if (typeof entry["Subtitle"] !== "undefined") {
		subtitle = entry["Subtitle"];
	}
	if (!subtitle.match(/^\s*$/)) {
		if (!title.match(/^\s*$/)) {
			return `${title}, ${subtitle}`;
		} else {
			return `${subtitle}`;
		}
	}
	if (title.match(/^\s*$/)) {
		return "";
	} else {
		return title;
	}
}


//////////////////////////////
//
// getSource -- Generate a source link based on "DIAMM Source Link" or "RISM Source Link".
//

function getSource(entry) {
	let diammurl = "";
	if (typeof entry["DIAMM Source Link"] !== "undefined") {
		diammurl = entry["DIAMM Source Link"];
	}
	if (!diammurl.match(/^https?:\/\/.*diamm\.ac\.uk\//)) {
		if (diammurl) {
			console.warn("DIAMM URL is invalid:", diammurl);
		}
		diammurl = "";
	}

	let rismurl = "";
	if (typeof entry["RISM Source Link"] !== "undefined") {
		rismurl = entry["RISM Source Link"];
	}
	if (!rismurl.match(/^https?:\/\/opac\.rism\.info\//)) {
		if (rismurl) {
			console.warn("RISM URL is invalid:", rismurl);
		}
		rismurl = "";
	}

	if (!diammurl && !rismurl) {
		console.error("Cannot find DIAMM or RISM source link in", entry);
		return "";
	}


	if (diammurl) {
		let text = "DIAMM";
		let matches = diammurl.match(/diamm\.ac\.uk\/sources\/(.*?)\//);
		if (matches) {
			text += ` ${matches[1]}`;
		}
		return diammurl;
	}

	if (rismurl) {
		let text = "RISM";
		let matches = rismurl.match(/opac\.rism\.info\/search\?.*id=(\d+)/);
		if (matches) {
			text += ` ${matches[1]}`;
		}
		return rismurl;
	}

	return "";
}

//////////////////////////////
//
// buildComposerSelect --
//

function buildComposerSelect(data) {
	let counter = {};
	let sum = data.length;
	for (let i=0; i<sum; i++) {
		let entry = data[i];
		let composer = entry[INDEX_composer];
		if (!composer) {
			console.error("WARNING: ", entry, " DOES NOT HAVE A COMPOSER");
			continue;
		}
		counter[composer] = (counter[composer] === undefined) ? 1 : counter[composer] + 1;
	}

	let clist = Object.keys(counter).sort();
	let composerCount = clist.length;
	let output = "<select class='composer' onchange='doSearch()'>\n";
	output += `<option value="">Any composers [${composerCount}]</option>`;
	for (let i=0; i<clist.length; i++) {
		let name = clist[i];
		let count = counter[clist[i]];
		output += `<option value="${name}">${name} (${count})</option>`;
	}
	output += "</select>\n";
	return output;
}


//////////////////////////////
//
// buildGenreSelect --
//

function buildGenreSelect(data) {
	let counter = {};
	let sum = data.length;
	for (let i=0; i<sum; i++) {
		let entry = data[i];
		let genre = entry[INDEX_genre];
		if (!genre) {
			console.error("WARNING: ", entry, " DOES NOT HAVE A GENRE");
			continue;
		}
		counter[genre] = (counter[genre] === undefined) ? 1 : counter[genre] + 1;
	}

	let glist = Object.keys(counter).sort();
	let genreCount = glist.length;
	let output = "<select class='genre' onchange='doSearch()'>\n";
	output += `<option value="">Any genre [${genreCount}]</option>`;
	for (let i=0; i<glist.length; i++) {
		let name = glist[i];
		let count = counter[glist[i]];
		output += `<option value="${name}">${name} (${count})</option>`;
	}
	output += "</select>\n";
	return output;
}


//////////////////////////////
//
// buildSourceSelect --
//

function buildSourceSelect(data) {
	let counter = {};
	let sum = data.length;
	for (let i=0; i<sum; i++) {
		let entry = data[i];
		let source = entry[INDEX_firstsource];
		if (!source) {
			console.error("WARNING: ", entry, " DOES NOT HAVE A SOURCE");
			continue;
		}
		counter[source] = (counter[source] === undefined) ? 1 : counter[source] + 1;
	}

	let slist = Object.keys(counter).sort();
	let sourceCount = slist.length;
	let output = "<select class='source' onchange='doSearch()'>\n";
	output += `<option value="">Earliest source [${sourceCount}]</option>`;
	for (let i=0; i<slist.length; i++) {
		let name = slist[i];
		let count = counter[slist[i]];
		output += `<option value="${name}">${name} (${count})</option>`;
	}
	output += "</select>\n";
	return output;
}


//////////////////////////////
//
// buildVoiceSelect --
//

function buildVoiceSelect(data) {
	let counter = {};
	let fileCount = data.length;
	for (let i=0; i<fileCount; i++) {
		let entry = data[i];
		let voice = entry[INDEX_voice];
		if (!voice) {
			console.error("WARNING: ", entry, " DOES NOT HAVE A VOICE COUNT");
			continue;
		}
		counter[voice] = (counter[voice] === undefined) ? 1 : counter[voice] + 1;
	}

	let vlist = Object.keys(counter).sort();
	let output = "<select class='voice' onchange='doSearch()'>\n";
	output += `<option value="">Any voice count</option>`;
	for (let i=0; i<vlist.length; i++) {
		let vcount = vlist[i];
		output += `<option value="${vcount}">${vcount}</option>`;
	}
	output += "</select>\n";
	return output;
}


//////////////////////////////
//
// buildYearSelect --
//

function buildYearSelect(data) {
	let counter = {};
	let fileCount = data.length;
	for (let i=0; i<fileCount; i++) {
		let entry = data[i];
		let year = entry[INDEX_firstsourcedate];
		if (!year) {
			console.error("WARNING: ", entry, " DOES NOT HAVE A YEAR");
			continue;
		}
		counter[year] = (counter[year] === undefined) ? 1 : counter[year] + 1;
	}

	let ylist = Object.keys(counter).sort();
	let output = "<select class='year' onchange='doSearch()'>\n";
	output += `<option value="">Any year</option>`;
	for (let i=0; i<ylist.length; i++) {
		let ycount = ylist[i];
		output += `<option value="${ycount}">${ycount}</option>`;
	}
	output += "</select>\n";
	return output;
}


//////////////////////////////
//
// doSearch --
//

function doSearch(data) {
	if (!data) {
		data = METADATA;
	}

	let searchInterface = document.querySelector("#search-interface");
	if (!searchInterface) {
		console.log("Problem finding search interface");
		return;
	}

	let composerField = searchInterface.querySelector("select.composer");
	if (!composerField) {
		console.log("Problem finding composer field in search interface");
		return;
	}
	let composerQuery = composerField.value;

	let genreField = searchInterface.querySelector("select.genre");
	if (!genreField) {
		console.log("Problem finding composer field in search interface");
		return;
	}
	let genreQuery = genreField.value;

	let sourceField = searchInterface.querySelector("select.source");
	if (!sourceField) {
		console.log("Problem finding source field in search interface");
		return;
	}
	let sourceQuery = sourceField.value;

	let voiceField = searchInterface.querySelector("select.voice");
	if (!voiceField) {
		console.log("Problem finding voice-count field in search interface");
		return;
	}
	let voiceQuery = voiceField.value;

	let yearField = searchInterface.querySelector("select.year");
	if (!yearField) {
		console.log("Problem finding year field in search interface");
		return;
	}
	let yearQuery = yearField.value;

	if (composerQuery) {
		let tempdata = [];
		for (let i=0; i<data.length; i++) {
			let entry = data[i];
			let composer = entry[INDEX_composer];
			if (composer === composerQuery) {
				tempdata.push(entry);
			}
		}
		data = tempdata;
	}

	if (genreQuery) {
		let tempdata = [];
		for (let i=0; i<data.length; i++) {
			let entry = data[i];
			let genre = entry[INDEX_genre];
			if (genre === genreQuery) {
				tempdata.push(entry);
			}
		}
		data = tempdata;
	}

	if (sourceQuery) {
		let tempdata = [];
		for (let i=0; i<data.length; i++) {
			let entry = data[i];
			let source = entry[INDEX_firstsource];
			if (source === sourceQuery) {
				tempdata.push(entry);
			}
		}
		data = tempdata;
	}

	if (voiceQuery !== "") {
		let tempdata = [];
		for (let i=0; i<data.length; i++) {
			let entry = data[i];
			let voice = entry[INDEX_voice];
			if (voice == voiceQuery) {
				tempdata.push(entry);
			}
		}
		data = tempdata;
	}

	if (yearQuery !== "") {
		let tempdata = [];
		for (let i=0; i<data.length; i++) {
			let entry = data[i];
			let year = entry[INDEX_firstsourcedate];
			if (year == yearQuery) {
				tempdata.push(entry);
			}
		}
		data = tempdata;
	}

	displayBrowseTable(data);
}

</script>