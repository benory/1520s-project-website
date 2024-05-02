---
layout: default

---

<style>
	#paragraph {
		padding-left: 30px;
	}
</style>

# documentation

### Table of contents
- [Musical documentation](#music-documentation)
	- [Attributions](#attributions)
	- [Instrument names](#instrument-names)
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
		- [Javascript tools](#javascript-tools)
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
	<ol><b>Improbable attributions</b> cannot be ruled out but are unlikely to be correct.<br><br><ol>For instance, a five- or six-voice imitative chanson attributed in a late sixteenth-century source to Jean Mouton for the first time——some forty years after Mouton's death——is on the whole unlikely to be accurate.</ol>
	</ol>
	<ol><b>Implausible attributions</b> are all but impossible.<br><br><ol>One example: the attribution of Jachet of Mantua's <a href="https://1520s-project.org/work/?id=Jom2014"><i>Omnes sancti tui quesumus</i></a> to Adrian Willaert in a single source geographically distant from Willaert. Attributions to Jachet, by contrast, appear in an overwhelming number of sources closer to the composer, including in a number of single-author prints of his motets.</ol>
	</ol>
	</div>
</div>
<div id="paragraph">
	This project only considers attributions in sixteenth-century sources. Implied attributions on the basis of so-called <i>Nestertheorie</i> are not adopted. <br><br>Where modern scholarship has attributed works to a given composer without a sixteenth-century attribution, these pieces are "linked" to the composer. This means that results of a search for the composer Philippe Verdelot will include anonymous madrigals in the Newberry Partbooks long assumed to be by Verdelot, but for which no sixteenth-century concordance attributes the work to the Florentine composer.
</div>

<br>


### Instrument names {#instrument-names}

<div id="paragraph">Early sixteenth-century musical sources often use interchangeable names for voices, such as Superius, Cantus, and Discantus for the top voice in a given texture; or Tenor II, Quintus, and Sextus for a middle voice. And different sources for a given piece might use different names for the same musical line. <br><br> To maintain consistent nomenclature, this project uses four voice designations: superius, altus, tenor, and bassus. For dispositions in more than four voices, the project assigns the most logical voice, followed by a roman numeral (i.e., Tenor II).</div>

<br>

### Sections {#sections}

<div id="paragraph">Each section in a piece is separated by a double bar, or at the end of the piece, a final barline. The start of each section of a piece has a section label (for instance, "Secunda pars: Ave solem genuisti").</div>

<br>

### Note values and Mensurstriche {#notes}

<div id="paragraph">All scores appear in unreduced note values. This means that a breve is equal to a double whole note; a minim, a half note.<br><br><i>Mensurstriche</i>, a scholarly practice that allows note values to cross over a modern bar line without using a tie, is avoided. Programs such as Finale and Sibelius cannot properly render <i>Mensurstriche</i>, and so any workarounds used in these programs by scholars are lost when exporting to MusicXML.</div>

<br>

### Mensuration signs {#mensuration-signs}

<div id="paragraph">Where possible, scores use the mensuration signs found in the earliest source for a given piece. <br><br> Note: the Music Encoding Initiative (MEI) has not yet made it possible to reproduce all original mensuration signs, such as those with a sign numerator and numerical demoninator (e.g., Cut-C over 3).

</div>

<br>

### Terminal notes and fermatas {#terminal-notes}

<div id="paragraph">Terminal notes are defined as the last note in a given voice prior to a double barline or the end of a given work. They are displayed as longs regardless of their actual durations.<br><br> Fermatas on terminal notes are removed, since terminal longs represent an indefinite value. The placement of fermatas elsewhere follows the musical sources.</div>

<br>

### Editorial accidentals {#editorial-accidentals}

<div id="paragraph">
	Editorial accidentals, known as <i>musica ficta</i>, are suggested in order to:<br><br>
	<ul><b>avoid melodic tritones</b><br>
		<ul>In the following example, taken from the bassus of Noel Bauldeweyn's <a href="https://1520s-project.org/work/?id=Bau3001"><i>En douleur en tristesse</i></a>, a tritone in m. 14 is avoided by flatting the E following the B-flat. A second tritone produced by stepwise motion in m. 15 can be sidestepped through the addition of a second flat. <br><img src="/images/Bau3001_ficta_example.png" alt="Bauldeweyn ficta example">
		</ul>
	</ul>

<ul><b>inflect cadences</b><br><ul>Editorial accidentals are added when moving from an imperfect consonance to a perfect consonance. In this repertoire, this is almost always sixth-to-octave motion preceded by a seven-to-six suspension in the top voice. See, for instance, mm. 59–62 of Nicolas Champion's <a href="https://1520s-project.org/work/?id=Bau3001"><i>De profundis clamavi</i></a>, in which a seven-to-six suspension is followed by movement to an octave: <br><br><img src="/images/Cha2001_ficta_example.png" alt="Champion ficta example"></ul></ul>

This project argues that cadences not only have a contrapuntal element, but function as part of rhetorical gestures. To be classified as a cadence, these contrapuntal elements must occur where one or both of the voices end a text phrase. Usually——but by ca. 1530 not always——one or both of the voices will rest following the cadence.<br><br>

Users can see scores without <i>ficta</i> by toggling on/off the suggested editorial accidentals using the "Hide/Show Editorial Accidentals" button. They can download the scores to tailor the accidentals to their own preferences.
</div>

<br><br>

## Technical documentation {#technical-documentation} 

### Filenames {#filenames}

<div id="paragraph">

<b>Composer codes and numbering</b><br>

<ul>Each piece is assigned a three-letter composer code, <a href="https://wiki.ccarh.org/wiki/Josquin_Project_encoding_standards#Composer_codes">assigned in close coordination with the Josquin Research Project</a>. Each work is then assigned a four-digit number. The first digit indicates the genre (1 for a mass; 2 for a motet; 3 for a secular work). The last two or three digits are an enumeration of the works in the given genre——typically, moving from the first circulating work by a composer to the last. For example, Wil2001 is the first circulating motet (or one of the first) by the composer Adrian Willaert. <br><br>

If a piece, such as a mass, consists of multiple parts, each section additionally has a letter. For instance, Wil1001a is the Kyrie from Willaert's <i>Missa Mente tota</i>; Wil1001b is the Gloria.<br><br>

Where this project collaborates with existing editions, the first two digits reflect the volume in the series. For example, The 1520s Project incorporates scores from the <a href="https://senflonline-eng.com/new-senfl-edition/"><i>New Senfl Edition</i></a>. In this case, Snf0101 is the first work in the first volume of the <i>New Senfl Edition</i>. Following the NSE's numbering, Snf0238 is no. 38 in the overall series, found in the second volume.</ul>

<b>Work name</b><br>

<ul>After the composer code and number, the filename continues with a dash, followed by the name of the work, using only the characters A-Z and 0-9, with underscores separating individual words, then (if applicable) followed by a dash and then the section name. For example, the Kyrie of Willaert's <i>Missa Mente tota</i> would be Wil1001a-Missa_Mente_tota-Kyrie. All special characters (e.g., apostrophes and accents) are removed.</ul>

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

Scores are then exported to MusicXML files and converted using the <a href="https://extras.humdrum.org/man/xml2hum/">musicxml2hum command</a> in the Humdrum Extras toolkit.

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

Scores coming from published editions have these additional categories of information:
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

<div id="paragraph">The metadata for each piece includes the (probable) earliest source in the transmission and its dating. External links are provided to either <a href="https://www.diamm.ac.uk/">DIAMM</a> or <a href="https://rism.online/">RISM</a>. Names of sources on work pages follow RISM nomenclature. </div>

<br>

### Website {#website}

<div id="paragraph">Files for the website for The 1520s Project are hosted on github at <br>
	<ul><a href="https://github.com/benory/1520s-project-website">https://github.com/benory/1520s-project-website</a></ul>
</div>
<div id="paragraph">The website is served through <a href="https://pages.github.com">Github pages</a> and uses the markdown language <a href="https://jekyllrb.com">Jekyll</a>.</div><br>

#### Javascript tools {#javascript-tools}

<div id="paragraph">
	<ul><b>Vega-Lite</b>
		<ul><a href="https://vega.github.io/vega-lite/">Vega-Lite</a> is a visualization grammar for statistical graphics, which functions similar to ggplot. The 1520s Project uses Vega-Lite for histograms and bar charts.</ul>
	</ul>
	<ul><b>Verovio</b>
		<ul><a href="https://www.verovio.org/index.xhtml">Verovio</a> is an SVG music notation renderer developed primarily by Laurent Pugin. The humlib library is embedded within verovio and is used to process and analyze the Humdrum scores for the website as well as convert the scores into the MEI format for rendering in Verovio.</ul>
	</ul>
</div>
<br>

## Download project data {#download-data}

<a href="https://github.com/benory/1520s-project-scores">The project's Github repository</a>, which hosts Sibelius files, MusicXML files, Humdrum files, and PDFs, can be cloned in terminal by using the following command:

    git clone https://github.com/benory/1520s-project-scores.git

The metadata used to search on the [browse page](https://1520s-project.org/browse/), as well as dispaly additional information about scores on the work pages, is available [here](https://raw.githubusercontent.com/benory/1520s-project-website/main/_includes/metadata/works.json).

<br>