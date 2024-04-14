
// vim: ts=3:nowrap

let TIMEMAP   = {};
let QEVENTS   = [];
let LASTTIME  = -1;
let REFRESH   = null;

//////////////////////////////
//
// InitializeTimemap --
//

function InitializeTimemap() {
	if (typeof REFRESH === "undefined") {
		console.warn("REFRESH is undefined");
		return;
	}
	let increment = 20;
	REFRESH = setInterval(function() {
		if (AUDIO && AUDIO.paused) {
			clearInterval(REFRESH);
			return;
		}
		if (!AUDIO) {
			clearInterval(REFRESH);
			return;
		}
		let currenttime = AUDIO.currentTime;
		//console.warn(TIMEMAP);
		//console.warn(ID1520s);
		CheckTimeMap(TIMEMAP[ID1520s], QEVENTS, currenttime, increment/1000.0 * 2);
	}, increment);
}

//////////////////////////////
//
// getTimemap --
//

function getTimemap(id) {
	if (!id) {
		id = ID;
	}
	if (TIMEMAP[id]) {
		return;
	}
	let request = new XMLHttpRequest();
	request.open("GET", `{{site.the1520sProject_data_url}}/${id}-timemap.json`);
	request.addEventListener("load", function() {
		try {
			TIMEMAP[id] = JSON.parse(this.responseText);
			interpolateIntegers(id);
		} catch (e) {
			console.error("Failed to parse JSON:", this.responseText);
			console.error("Error details:", e);
		}
	});
	request.send();
}


//////////////////////////////
//
// interpolateIntegers --
//

function interpolateIntegers(id) {
	timemap = TIMEMAP[id];
	if (timemap.length == 0) {
		return;
	}
	let newpoints = [];
	let byindex = {};
	for (let i=0; i<timemap.length; i++) {
		let qstamp = timemap[i].qstamp;
		byindex[qstamp] = {i: i, timemap: timemap[i]};
	}
	let maxval = timemap[timemap.length-1].qstamp;
	for (i=8; i<maxval; i+=8) {
		if (byindex[i]) {
			continue;
		}
		let newpoint;
		newpoint = interpolateTstamp(timemap, i);
		newpoints.push(newpoint);
		// console.log("MISSING: ", i, newpoint.tstamp);
	}
	TIMEMAP[id] = timemap.concat(newpoints);
}

//////////////////////////////
//
// interpolateTstamp --
//

function interpolateTstamp(timemap, qtime) {
	let i;
	let t1;
	let t2;
	let q1;
	let q2;
	for (i=0; i<timemap.length; i++) {
		if (timemap[i].qstamp < qtime) {
			continue;
		}
		if (i == 0) {
			console.log("STRANGE PROBLEM");
		}
		t1 = timemap[i-1].tstamp;
		t2 = timemap[i].tstamp;
		q1 = timemap[i-1].qstamp;
		q2 = timemap[i].qstamp;
		break;
	}
	if (!t2) {
			console.log("STRANGE PROBLEM 2");
	}
	let ttime = ((qtime-q1)/(q2-q1))*(t2-t1)+t1;
	let newpoint = { qstamp: qtime, tstamp: ttime};
	//console.log("NEWPOINT", newpoint);
	return newpoint;
}

//////////////////////////////
//
// CheckTimeMap --
//

function CheckTimeMap(timemap, events, currenttime, increment) {
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
	// console.log("TIMEENTRY", target);
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
		// ons[i].style.stroke = "red";
		// ons[i].style.fill = "red";
		// have to re-find on page in case the image has changed:
		let xon = document.querySelector("#" + ons[i].id);
		xon.style.fill = "red";
	}
	for (let i=0; i<offs.length; i++) {
		// have to re-find on page in case the image has changed:
		let xoff = document.querySelector("#" + offs[i].id);
		xoff.style.fill = "";
	}
}

//////////////////////////////
//
// prepareQEvents --
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




