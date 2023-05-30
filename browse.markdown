---
layout: page
title: browse
permalink: /browse/
---

<div id="search-interface"></div>

<div id="list"></div>

<style>
	h1 { font-size: 40px; }
	th { text-align: left; }
	table.browse { min-width: 1000px; }
	table.browse { margin-left: auto; margin-right: auto; } /* center table */
	table.browse { border-collapse: collapse; } /* don't put gaps between cells */
	table.browse th { background:skyblue; }
	table.browse td, table.browse th { padding-left: 10px; padding-top: 5px; }
	table.browse tr:hover { background:#ff000011; }
	a { text-decoration: none; }
	#search-interface { margin-bottom: 30px; }
</style>

<script>
// vim: ts=3:nowrap

let METADATA = [];
let INDEX_id          = "ID";
let INDEX_composer    = "Composer";
let INDEX_title       = "Title";
let INDEX_genre       = "Genre";
let INDEX_voice       = "Voices";
let INDEX_firstsourcedate = "Date of First Source";

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
	let headings = [INDEX_id, INDEX_composer, INDEX_title, INDEX_genre, INDEX_voice, INDEX_firstsourcedate];
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
			let value = entry[headings[i]];
			output += "<td>";
			output += value;
			output += "</td>";
		}
		output += "</tr>\n";
	}
	return output;
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

	let voiceField = searchInterface.querySelector("select.voice");
	if (!voiceField) {
		console.log("Problem finding voice-count field in search interface");
		return;
	}
	let voiceQuery = voiceField.value;

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

	displayBrowseTable(data);
}

</script>