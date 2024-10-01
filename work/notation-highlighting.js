
// vim: ts=3:nowrap

let QEVENTS   = [];
let LASTTIME  = -1;
let REFRESH   = null;


//////////////////////////////
//
// initializeTimemap -- Sets up a repeating interval using setInterval() 
//     to regularly check the current playback time (audio.currentTime) 
//     and map it to corresponding note events in the notation using the 
//     checkTimeMap() function.
//
//     The REFRESH interval checks every 20ms if the audio is paused, and
//     if not, it updates the note highlighting based on the currentTime
//     of the audio.
//

function initializeTimemap() {
	if (typeof REFRESH === "undefined") {
		console.warn("REFRESH is undefined");
		return;
	}
	let increment = 20;
	REFRESH = setInterval(function() {
		if (DATA1520.audio && DATA1520.audio.paused) {
			clearInterval(REFRESH);
			return;
		}
		let currentTime = DATA1520.audio.currentTime;
		//console.warn(DATA1520.workid);
		checkTimeMap(DATA1520.timemap, QEVENTS, currentTime, increment/1000.0 * 2);
	}, increment);
}



//////////////////////////////
//
// checkTimeMap --
//

function checkTimeMap(timemap, events, currenttime, increment) {
	let target = null;
	let diff;
	for (let i=0; i<timemap.length; i++) {
		if (Math.abs(timemap[i].tstamp - currenttime) < increment) {
			target = timemap[i];
		}
	}
	if (!target) {
		return;
	}
	if (target.tstamp == LASTTIME) {
		return;
	}
	LASTTIME = target.tstamp;
	CheckEventMap(target.qstamp, events);
}



//////////////////////////////
//
// CheckEventMap --
//

function CheckEventMap(etime, events) {
	for (let i=0; i<events.length; i++) {
		if (Math.abs(etime - events[i].qstamp) < 0.01) {
			ProcessNoteEvents(events[i]);
		}
	}
}



//////////////////////////////
//
// ProcessNoteEvents --
//

function ProcessNoteEvents(event) {
	let ons = event.on;
	let offs = event.off;
	for (let i=0; i<ons.length; i++) {
		// have to re-find on page in case the image has changed:
		let xon = document.querySelector("#" + ons[i].id);
		xon.classList.add("highlight");
	}
	for (let i=0; i<offs.length; i++) {
		// have to re-find on page in case the image has changed:
		let xoff = document.querySelector("#" + offs[i].id);
		xoff.classList.remove("highlight");
	}
}



//////////////////////////////
//
// unhighlightAllNotesInSvg --
//

function unhighlightAllNotesInSvg() {
	let notes = document.querySelectorAll(".verovio-svg g.note");
	for (let i=0; i<notes.length; i++) {
		notes[i].classList.remove("highlight");
	}
}



//////////////////////////////
//
// prepareQEvents -- Scans the SVG to prepare a list of note events 
//    (QEVENTS), where each note has a corresponding qstamp 
//    (quarter note timing) that matches the audio timemap.
//

function prepareQEvents(target) {
	if (typeof target === "string") {
		target = document.querySelector(".verovio-svg svg");
	}
	let svgnotes = target.querySelectorAll("g[id^='note-']");
	let qpre = {};
	let matches;
	let ques;
	let obj;
	for (let i=0; i<svgnotes.length; i++) {
		if (matches = svgnotes[i].className.baseVal.match(/qon-([^\s]+)/)) {
			ques = getQstampFloat(matches[1]);
			if (!qpre[ques]) {
				qpre[ques] = {qstamp: ques, on:[], off:[]};
			}
			qpre[ques].on.push(svgnotes[i]);
		}
		if (matches = svgnotes[i].className.baseVal.match(/qoff-([^\s]+)/)) {
			ques = getQstampFloat(matches[1]);
			if (!qpre[ques]) {
				qpre[ques] = {qstamp: ques, on:[], off:[]};
			}
			qpre[ques].off.push(svgnotes[i]);
		}
	}
	QEVENTS = [];
	for (let qst in qpre) {
		QEVENTS.push(qpre[qst])
	}
	QEVENTS.sort(function(a, b) {
		return a.qstamp - b.qstamp;
	});
}



//////////////////////////////
//
// getQstampFloat --
//

function getQstampFloat(str) {
	let ques = -1;
	if (str.match(/d/)) {
		ques = parseFloat(str.replace(/d/, "."));
	} else if (str.match(/_/)) {
		let matches = str.match(/(\d+)_(\d+)/);
		if (matches) {
			ques = parseInt(matches[1]) / parseInt(matches[2]);
		}
	} else if (str.match(/^\d+$/)) {
		ques = parseInt(str);
	}
	return ques;
}



