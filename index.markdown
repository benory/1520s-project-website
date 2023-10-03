---
# Feel free to add content and custom Front Matter to this file.
# To modify the layout, see https://jekyllrb.com/docs/themes/#overriding-theme-defaults

layout: page
---
<style>
	main.page-content {padding: 0px;}
	table.most-recent {text-align: left;}
	table.most-recent {font: 400 14px/1 -apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif,"Apple Color Emoji","Segoe UI Emoji","Segoe UI Symbol"}
	table.most-recent { border-collapse: collapse; }
	table.most-recent { padding-left: 2px; padding-top: 2px; padding: 2px}
</style>

![1520s Project banner](/images/1520s_banner.png)

The 1520s Project is an open-source repository of more than 250 scores of European polyphonic music from ca. 1510 through ca. 1530. It seeks to address how, when, and where a radically new style of polyphonic music emerged in the 1520s. Read [about the project](about) or [browse the project's scores](browse). <br><br>


#### Project data
+ Number of works: <span id="work-count"></span>
+ Number of notes: <span id="note-count"></span>
+ By genre: 24 mass movements, 182 motets, 54 secular works

![Project summary](/images/project_summary.svg)

#### Recently added works
<div data-count="10" id="most-recent"></div>

For complementary repertoire spanning ca. 1420–1520, see the [Josquin Research Project](http://josquin.stanford.edu){:target="_blank"}. For more information on the overlap between the projects, see [about this project](about).

<script>
// vim: ts=3

document.addEventListener("DOMContentLoaded", fillMostRecentList);

//////////////////////////////
//
// fillMostRecentList --
//

function fillMostRecentList() {
	let mid = "AKfycbwuHJlO-idyGmlaHBhNshmSCtiOau1QsXwN3K7PHyJDZ47qvPMEvv-uACFzJCBLB7iWXw";
	let metadata = `https://script.google.com/macros/s/${mid}/exec`;
	fetch(metadata)
		.then(response => {
			if (!response.ok) {
				throw new Error(`HTTP error! Status: ${response.status}`);
			}
			return response.json();
		})
		.then(data => {
			displayMostRecent(data);
			fillInCensusData(data);
		})
		.catch(error => {
			console.error("Fetch error: ", error);
		});
}



//////////////////////////////
//
// fillInCensusData --
//

function fillInCensusData(data) {
	let workCount = 0;
	let noteCount = 0;
	for (let i=0; i<data.length; i++) {
		let count = data[i]["Note Count"];
		if (count) {
			noteCount += parseInt(count);
			workCount++;
		}
	}

	let noteElement = document.querySelector("#note-count");
	if (noteElement) {
		noteElement.innerHTML = formatBigNumber(noteCount);
	}

	let workElement = document.querySelector("#work-count");
	if (workElement) {
		workElement.innerHTML = workCount;
	}

}


//////////////////////////////
//
// formatBigNumber -- avoid using commas to make Europeans happier
//

function formatBigNumber(number) {
	return number.toString().replace(/(\d)(?=(\d{3})+$)/g, '$1 ');
}


//////////////////////////////
//
// displayMostRecent --
//

function displayMostRecent(metadata) {
	metadata.sort(compareByDateAdded);

	let element = document.querySelector("#most-recent");
	if (!element) {
		console.error("Cannot find #most-recent.");
		return;
	}
	let count = element.dataset.count;
	if (count < 1) {
		count = 10;
	}
	if (count > 50) {
		count = 50;
	}

	let output = "<table class='most-recent'>";
	output += "<tr><th>Date Added</th><th>Composer</th><th>Work</th></tr>";
	for (let i=0; i<count; i++) {
		let entry = metadata[i];
		let date = entry["Date Added"];
		let scoreURL = getScoreURL(entry);
		output += "<tr>";
		output += `<td>${entry["Date Added"]}</td>`;
		output += `<td>${stylizeComposer(entry.Composer)}</td>`;
		if (!entry.Subtitle) {
			output += `<td><a target="_blank" href=${scoreURL}>${entry.Title}</a></td>`;
		} else {
			output += `<td><a target="_blank" href=${scoreURL}>${entry.Title} <i>${entry.Subtitle}</i></a></td>`;
		}
		output += "</tr>";
	}
	output += "</table>";
	element.innerHTML = output;
}



//////////////////////////////
//
// stylizeComposer -- Make "first last" from "last, first".
//

function stylizeComposer(name) {
	let matches = name.match(/^\s*([^,]+)\s*,\s*([^,]+)\s*$/);
	if (!matches) {
		return name;
	} else {
		return `<span class="first-name">${matches[2]}</span> <span class="last-name">${matches[1]}</span>`;
	}
}



//////////////////////////////
//
// compareByDateAdded -- For sorting metadata entries by "Date Added".
//

function compareByDateAdded(a, b) {
  // Handle null or empty dates by placing them at the end
  if (!a["Date Added"] && !b["Date Added"]) return 0;
  if (!a["Date Added"]) return 1;
  if (!b["Date Added"]) return -1;

  // Convert date strings to Date objects for comparison
  const dateA = new Date(a["Date Added"]);
  const dateB = new Date(b["Date Added"]);

  // Compare the dates
  if (dateA < dateB) return 1;
  if (dateA > dateB) return -1;
  return 0;
}

//////////////////////////////
//
// getScoreURL -- Generate URL
//

function getScoreURL(entry) {
	let ID = "";
	if (typeof entry["ID"] !== "undefined") {
		ID = entry["ID"];
		let url = `"/work?id=${ID}"`;
		return url;
	}
	return "";
}

</script>