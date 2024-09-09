---
layout: page
title: documentation
order: 2
---

<style>
	#paragraph {
		padding-left: 30px;
	}

	h1 {
		font-size: 45px;
	}

	h2 {
		font-size: 32px;
		font-weight: bold;
	}

	h3 {
		font-size: 24px;
		font-weight: bold;
	}

	h4 {
		font-size: 20px;
	}

</style>

#### Table of contents
- [Musical documentation](#music-documentation)
	- [Attributions](#attributions)
	- [Voice names](#voice-names)
	- [Sections](#sections)
	- [Note values and Mensurstriche](#notes)
	- [Mensuration signs](#mensuration-signs)
	- [Terminal notes and fermatas](#terminal-notes)
	- [Editorial accidentals](#editorial-accidentals)
- [Technical documentation](#technical-documentation)
	- [Filenames](#filenames)
	- [Score preparation](#score-preparation)
	- [Encoded information](#encoded-information)
	- [Source metadata](#source-metadata)
	- [Website](#website)
		- [JavaScript tools](#javascript-tools)
	- [Data server](#data-server)
- [Download project data](#download-data)


<br>

## Musical documentation {#music-documentation}

<div id="paragraph">The 1520s Project provides high quality data with consistent editorial standards between scores. Shared editorial standards with the <a href="https://josquin.stanford.edu/">Josquin Research Project</a> enable rigorous comparisons and analysis of the musical data.</div>

<br>

### Attributions {#attributions}

<div id="paragraph">
	Most musical works in the early sixteenth century can be securely attributed to a single composer. For a small group of pieces, sorting out attributions presents additional complications:<br><br>
	<div id="paragraph"><ol><b>Secure attributions</b> are listed under the composer's name.</ol>
	<ol><b>Plausible attributions</b> need to be carefully considered but given the information available, lack sufficient strengh to assign authorship. <br><br><ol>A test case might be the attributions to Lupus Hellinck for the motet <a href="https://1520s-project.org/work/?id=Ric2016"><i>Jerusalem surge</i></a>, believed to be by Jean Richafort. On the whole, the sources favor Richafort, but an early Pierre Attaingnant print, constituting a separate branch of transmission, attributes the motet to Lupus. The attributions to Lupus are therefore plausible.</ol></ol>
	<ol><b>Improbable attributions</b> cannot be ruled out but are unlikely to be correct.<br><br><ol>A five- or six-voice imitative chanson in a mid-sixteenth-century style and attributed in a late sixteenth-century source to Jean Mouton for the first time——some forty years after Mouton's death——is unlikely to be accurate.</ol></ol>
	<ol><b>Implausible attributions</b> are all but impossible.<br><br><ol>One example: Jachet of Mantua's <a href="https://1520s-project.org/work/?id=Jom2014"><i>Omnes sancti tui quesumus</i></a> is attributed to Adrian Willaert in a single source geographically distant from Willaert with no clear connection to Willaert. Attributions to Jachet, by contrast, appear in an overwhelming number of sources closer to the composer, including in a number of single-author prints of his motets. The attribution to Willaert is therefore implausible.</ol></ol>
	</div>
</div>
<div id="paragraph">
	This project only considers attributions in sixteenth-century sources. Implied attributions on the basis of so-called <i>Nestertheorie</i> are not adopted. Where modern scholarship has attributed works to a given composer without a sixteenth-century attribution, these pieces are "linked" to the composer. This means: results of a search for the composer Philippe Verdelot will include anonymous madrigals in the Newberry Partbooks long assumed to be by Verdelot, but for which no sixteenth-century concordance attributes the work to the Florentine composer.
</div>

<br>


### Voice names {#voice-names}

<div id="paragraph">Early sixteenth-century musical sources often use interchangeable names for voices, such as Superius, Cantus, and Discantus for the top voice in a given texture; or Tenor II, Quintus, and Sextus for a middle voice. And different sources for a given piece might use different names for the same musical line. To maintain consistent nomenclature, this project uses four voice designations only: superius, altus, tenor, and bassus. When a piece uses more than four voices, the project assigns the most logical voice on the basis of range, followed by a roman numeral (for instance, Tenor II).</div>

<br>

### Sections {#sections}

<div id="paragraph">Each section in a piece is separated by a double bar, or at the end of the piece, a final barline. The start of each section of a piece has a section label (for instance, "Secunda pars: Ave solem genuisti").</div>

<br>

### Note values and Mensurstriche {#notes}

<div id="paragraph">All scores appear in unreduced note values. This means that a breve is equal to a double whole note; a minim as a half note, etc.<br><br><i>Mensurstriche</i>, an editorial practice that allows note values to cross over a modern bar line without using a tie, is avoided. Programs such as Finale and Sibelius cannot properly render <i>Mensurstriche</i>, and so any workarounds used in these programs by scholars are lost when exporting to MusicXML.</div>

<br>

### Mensuration signs {#mensuration-signs}

<div id="paragraph">Where possible, scores use the mensuration signs found in the earliest source for a given piece. <br><br><b>Note:</b> the Music Encoding Initiative (MEI) has not yet made it possible to reproduce all original mensuration signs, such as those with a sign numerator and numerical demoninator (e.g., Cut-C over 3). Existing scores will be updated as these signs become available.

</div>

<br>

### Terminal notes and fermatas {#terminal-notes}

<div id="paragraph">Terminal notes are defined as the last note in a given voice prior to a double barline or the end of a given work. They are displayed as longs regardless of their actual durations. Medial cadences are followed by double barlines; terminal cadences are followed by a final barline. <br><br> Fermatas on terminal notes are removed, since terminal longs represent an indefinite value. The placement of fermatas elsewhere follows the musical sources.</div>

<br>

### Editorial accidentals {#editorial-accidentals}

<div id="paragraph">
	Editorial accidentals are not strictly part of the musical text, but instead must be realized by performers. <b>All analyses by The 1520s Project depend on the version of the score without editorial accidentals.</b> Editorial accidentals are displayed on scores in order to:<br><br>
	<ul><b>1) avoid melodic tritones</b><br>
		<ul>In the following example, taken from the bassus of Noel Bauldeweyn's <a href="https://1520s-project.org/work/?id=Bau3001"><i>En douleur en tristesse</i></a>, a tritone in m. 14 is avoided by flatting the E following the B-flat. A second tritone produced by stepwise motion in m. 15 can be sidestepped through the addition of a second flat. <br><img src="/images/Bau3001_ficta_example.png" alt="Bauldeweyn editorial accidentals example">
		</ul>
	</ul>

<ul><b>2) inflect cadences</b><br><ul>Editorial accidentals are added when moving from an imperfect consonance to a perfect consonance. In this repertoire, cadences often (but not always) feature sixth-to-octave motion preceded by a seven-to-six suspension in the top voice. See, for instance, mm. 59–62 of Nicolas Champion's <a href="https://1520s-project.org/work/?id=Bau3001"><i>De profundis clamavi</i></a>, in which a seven-to-six suspension is followed by movement to an octave: <br><br><img src="/images/Cha2001_ficta_example.png" alt="Champion editorial accidentals example"></ul></ul>

This project views cadences as having both a contrapuntal and a rhetorical component. In order to be classified as a cadence, the required contrapuntal elements must coincide with one or both of the voices ending a line of text. Usually——although by ca. 1530 not always——one or both of the voices will rest following the cadence.<br><br>

Users can see scores without editorial accidentals by toggling on/off the suggested editorial accidentals using the "Hide/Show Editorial Accidentals" button. They can download the scores to adapt the accidentals to their own preferences.
</div>

<br><br>

## Technical documentation {#technical-documentation} 

### Filenames {#filenames}

<div id="paragraph">

<b>Composer codes and numbering</b><br>

<ul>Each piece is assigned a three-letter composer code <a href="https://wiki.ccarh.org/wiki/Josquin_Project_encoding_standards#Composer_codes" target="_blank"> in close coordination with the Josquin Research Project</a>. Each work is then assigned a four-digit number. The first digit indicates the genre (1 for a mass; 2 for a motet; 3 for a secular work). The last two or three digits are an enumeration of the works in the given genre, typically moving from the first circulating work by a composer to the last. For example, Wil2001 is the first circulating motet (or one of the first) by the composer Adrian Willaert. <br><br>

If a piece, such as a mass, consists of multiple parts, the filename for each section additionally assumes a letter. For instance, Wil1001a is the Kyrie from Willaert's <i>Missa Mente tota</i>; Wil1001b is the Gloria from the same mass.<br><br>

Where this project collaborates with existing editions, the first two digits reflect the volume in the series. For example, The 1520s Project incorporates scores from the <a href="https://senflonline-eng.com/new-senfl-edition/" target="_blank"><i>New Senfl Edition</i></a>. In this case, Snf0101 is the first work in the first volume of the <i>New Senfl Edition</i>. Following the NSE's numbering, Snf0238 is no. 38 in the overall series and is in the second volume.</ul>

<b>Work name</b><br>

<ul>After the composer code and number, the filename continues with a dash, followed by the name of the work, using only the characters A-Z, a-z, and 0-9, with underscores separating individual words, then (if applicable) followed by a dash and then the section name. For example, the Kyrie of Willaert's <i>Missa Mente tota</i> would be Wil1001a-Missa_Mente_tota-Kyrie. All special characters (e.g., apostrophes and accents) are removed.</ul>

<b>Unique sources</b><br>

<ul>If a piece survives uniquely in one source (<i>unicum</i>), these naming conventions are followed by two dashes (--) and then the name of the source, written in an easy-to-read shorthand. For instance, Maistre Jan's <i>Vox de celis</i> is <i>unicum</i> in the manuscript I-Bc Q.19, better known as Bologna Q19. The filename is therefore Jan2002-Vox_de_celis--Bologna_Q19. The shorthand consists of the source location followed by a short version of the source signature, separated by an underscore.</ul>
</div><br>

### Score preparation {#score-preparation}

<div id="paragraph"> Each score is prepared in Sibelius by adjusting the following elements:
<div id="paragraph"> 
	<li>Any <i>Mensurstriche</i> is removed.</li>
	<li>Instrument names are corrected.</li>
	<li>Editorial accidentals are adjusted and placed in parentheses.</li>
	<li>Metadata (title, subtitles for sections, composer, encoder) is added to the score.</li>
	<li>The staff size is changed to 5.5 mm.</li>
	<li>System brackets are removed.</li>
	<li>Final notes and fermatas are formatted</li>
	<li>Information about canonic material is given</li>
</div><br>

Scores are then exported to MusicXML files and converted using the <a href="https://extras.humdrum.org/man/xml2hum/" target="_blank">musicxml2hum command</a> in the Humdrum Extras toolkit.

</div>

<br>

### Encoded information {#encoded-information}

<div id="paragraph"> A range of information is encoded in the humdrum files:
<div id="paragraph"> 
	<li>id: the ID for the work</li>
	<li>AGN: the genre</li>
	<li>voices: the number of voices</li>
	<li>COM: the composer </li>
	<li>OTL: the title of the work</li>
	<li>OPR: the title of the parent work</li>
	<li>ENC: the encoder</li>
	<li>END: the date of the encoding</li>
</div><br>

Scores coming from published editions have additional categories of information:
<div id="paragraph"> 
	<li>PTL: the title of the edition</li>
	<li>PPR: publisher of the edition</li>
	<li>PC#: the edition's series</li>
	<li>PDT: the year of the edition</li>
	<li>PED: the editors</li>
	<li>YEC: copyright information</li>
	<li>EED: the electornic encoder of the edition</li>
	<li>EEV: the date of the encoding</li>
</div>
</div>

<br>

### Source metadata {#source-metadata}

<div id="paragraph">Metadata for each piece includes the (probable) earliest source in the piece's transmission and its dating. External links are provided to <a href="https://www.diamm.ac.uk/" target="_blank">DIAMM</a> or <a href="https://rism.online/" target="_blank">RISM</a> as appropriate. Names of manuscript sources on the browse page and on individual work pages follow RISM nomenclature. </div>

<br>

### Website {#website}

<div id="paragraph">Files for the website for The 1520s Project are hosted on GitHub at <br>
	<ul><a href="https://github.com/benory/1520s-project-website" target="_blank">https://github.com/benory/1520s-project-website</a></ul>
</div>
<div id="paragraph">The website is served through <a href="https://pages.github.com" target="_blank">GitHub pages</a> and uses the markdown language <a href="https://jekyllrb.com" target="_blank">Jekyll</a>.</div><br>

#### JavaScript tools {#javascript-tools}

<div id="paragraph">
	<ul><b>Humdrum Notation Plugin</b>
		<ul>The <a href="https://plugin.humdrum.org/" target="_blank">Humdrum Notation Plugin</a> is an interface that simplifies working with the JavaScript toolkit version of Verovio.</ul>
	</ul>
	<ul><b>Vega-Lite</b>
		<ul><a href="https://vega.github.io/vega-lite/" target="_blank">Vega-Lite</a> is a visualization grammar for statistical graphics, which functions similar to ggplot. The 1520s Project uses Vega-Lite for histograms and bar charts.</ul>
	</ul>
	<ul><b>Verovio</b>
		<ul><a href="https://www.verovio.org/index.xhtml" target="_blank">Verovio</a> is an SVG music notation renderer developed primarily by Laurent Pugin. The humlib library is embedded within Verovio and is used to process and analyze the Humdrum scores for the website as well as convert the scores into MEI for rendering in Verovio.</ul>
	</ul>
	<ul><b>Verovio Humdrum Viewer</b>
		<ul><a href="https://verovio.humdrum.org/" target="_blank">Verovio Humdrum Viewer</a> is an online Humdrum file notation editor and renderer created by Craig Sapp. It is used for the final preparation of the scores and for various analyses not yet implemented on the project website.</ul>
	</ul>
</div>
<br>

## Data server {#data-server}

<div id="paragraph"> Scores uploaded to GitHub are processed using a <a href="https://data.1520s-project.org" target="_blank">data server</a> created by Sapp and hosted at Stanford University. The data server supports The 1520s Project, the Josquin Research Project, and the <a href="http://tassomusic.org" target="_blank">Tasso in Music Project</a>. Below is a screenshot of The 1520s Project's data server API webpage:<br><br><a href="https://data.1520s-project.org" target="_blank"><img src="/images/data_server.png" alt="data server"></a></div><br>

<div id="paragraph"> The data server creates alternate digital score formats and analyses that are inconvenient to process within the web browser. The Humdrum files in The 1520s Project's score repository are first copied onto the server. The server then generates derivative digital scores that exactly match the Humdrum files (MusicXML, MEI, MIDI, MP3, etc), renders data visualizations such as activity plots and keyscape plots, and builds the timemap required for MP3 playback highlighting. All files created by the data server (including more than are shown on this website) are freely available for download and use. Users also have the ability to incorporate this project's data on their own websites using Verovio, and to embed generated analyses within their own projects.</div>
<br>

## Download project data {#download-data}

<a href="https://github.com/benory/1520s-project-scores" target="_blank">The project's GitHub repository</a>, which hosts Sibelius files, MusicXML files, Humdrum files, and PDFs, can be cloned in terminal by using the following command:

    git clone https://github.com/benory/1520s-project-scores.git

<b>Note:</b> the Sibelius and MusicXML files on the project's GitHub repository are pre-corrected version of the Humdrum files (the data server provides post-corrected MusicXML files that are derived from the corrected Humdrum files).

Metadata used to search on the [browse page](https://1520s-project.org/browse/), as well as display additional information about scores on the work pages, is available as a set of JSON files used by the website:
<div id="paragraph"> 
	<li><a href="https://raw.githubusercontent.com/benory/1520s-project-website/main/_includes/metadata/works.json" target="_blank">Works</a> (metadata about the works/mass sections used for searches on the browse page)</li>
	<li><a href="https://raw.githubusercontent.com/benory/1520s-project-website/main/_includes/metadata/composers.json" target="_blank">Composers</a> (metadata and links for composers used on the browse and work pages)</li>
	<li><a href="https://raw.githubusercontent.com/benory/1520s-project-website/main/_includes/metadata/modern_editions.json" target="_blank">Modern Editions</a> (information about modern editions for works used on the workpages)</li>
	<li><a href="https://raw.githubusercontent.com/benory/1520s-project-website/main/_includes/metadata/statistics.json" target="_blank">Statistics</a> (number of works by year, compiled for use on the browse page)</li>
</div>

<br>