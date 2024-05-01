---
layout: page
title: documentation

---

<style>
	#paragraph {
		padding-left: 30px;
	}
</style>

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
- [Download project data](#download-data)


<br>

## Musical documentation {#music-documentation}

<div id="paragraph">The 1520s Project provides high quality data with consistent editorial standards between scores. These editorial standards are similar to those used by the <a href="https://josquin.stanford.edu/">Josquin Research Project</a>.</div>

<br>

### Attributions {#attributions}

<div id="paragraph">
	Most musical works in the early sixteenth century can be securely attributed to a single composer. For a small group of pieces, sorting out attributions presents additional complications:<br><br>
	<div id="paragraph"><li><b>Secure attributions</b> are is listed under the composer's name.</li>
	<li><b>Plausible attributions</b> need to be carefully considered but lack sufficient information to assign authorship. One might think of these to be in the range of 30–50% likelihood.</li>
	<li><b>Improbable attributions</b> cannot be ruled out but are unlikely to be correct. They might have a 10–30% change of being correct.</li>
	<li><b>Implausible attributions</b> are all but impossible. They range from a 0% chance to roughly a 10% probability.</li></div>
</div>
<div id="paragraph"><br>
	This project only considers attributions in sixteenth-century sources. Implied attributions on the basis of so-called <i>Nestertheorie</i> are not considered. Where modern scholarship has attributed works to a given composer, but for which there is not a sixteenth-century attribution, these pieces are linked. For example, a search for the composer Philippe Verdelot will return results that include anonymous madrigals in the Newberry Partbooks long assumed to be by Verdelot, but for which no sixteenth-century concordance survives.
</div>

<br>


### Instrument names {#instrument-names}

<div id="paragraph">Early sixteenth-century musical sources often use interchangeable names for voices, such as Superius, Cantus, and Discantus for the top voice in a given texture; or Tenor II, Quintus, and Sextus for a middle voice. And different sources for a given piece might use different names for the same musical line. <br><br> To maintain consistent nomenclature, this project uses four voice designations: superius, altus, tenor, and bassus. For dispositions in more than four voices, the project assigns the most logical voice, followed by a roman numeral (i.e., Tenor II).</div>

<br>

### Sections {#sections}

<div id="paragraph">Each section in a piece is separated by a double bar, or at the end of the piece, a final barline. The start of each section of a piece has a section label (for instance, "Secunda pars: Ave solem genuisti").</div>

<br>

### Note values and Mensurstriche {#notes}

<div id="paragraph">All scores appear in unreduced note values. This means that a breve is equal to a double whole note; a minim, a half note.<br><br><i>Mensurstriche</i>, a scholarly practice that allows note values to cross over a modern bar line without using a tie, is avoided as this format creates challenges for computer-based analysis.</div>

<br>

### Mensuration signs {#mensuration-signs}

<div id="paragraph">Where possible, scores use the mensuration signs found in the earliest source for a given piece. <br><br> Note: the Music Encoding Initiative (MEI) has not yet made it possible to reproduce all original mensuration signs, such as those with a sign numerator and numerical demoninator (e.g., Cut-C over 3).

</div>

<br>

### Terminal notes and fermatas {#terminal-notes}

<div id="paragraph">Terminal notes are defined as the last note in a given voice prior to a double barline or the end of a given work. They are displayed as longs regardless of their actual durations.<br><br> Fermatas on terminal notes are removed, since terminal longs represent an indefinite value. The placement of fermatas elsewhere follows the musical sources.</div>

<br>

### Editorial accidentals {#editorial-accidentals}

<div id="paragraph">Editorial accidentals, known as <i>musica ficta</i>, are suggested under two circumstances:<br><br>
<li>To avoid harmonic tritones</li> <br><ul>In the following example, taken from the bassus of Noel Bauldeweyn's <a href="https://1520s-project.org/work/?id=Bau3001"><i>En douleur en tristesse</i></a>, a tritone in m. 14 is avoided by flatting the e following the b-flat. A second, problematic tritone produced by stepwise motion in m. 15 can be sidestepped by adding a second flat. <br><img src="/images/Bau3001_ficta_example.png" alt="Bauldeweyn ficta example"></ul>

<li>To inflect at cadences</li> <br><ul>Editorial accidentals are added when moving from an imperfect consonance to a perfect consonance. In this repertoire, this is almost always sixth-to-octave motion preceded by a seven-to-six suspension in the top voice. See, for instance, mm. 59–62 of Nicolas Champion's <a href="https://1520s-project.org/work/?id=Bau3001"><i>De profundis clamavi</i></a>, in which a seven-to-six suspension is followed by movement to an octave: <br><br><img src="/images/Cha2001_ficta_example.png" alt="Champion ficta example"></ul>

This project argues that cadences not only have a contrapuntal element, but function as part of rhetorical gestures. To be classified as a cadence, these contrapuntal elements must occur where one or both of the voices end a text phrase. Usually——but by ca. 1530 not always——one or both of the voices will rest following the cadence.<br><br>

Users can see scores without <i>ficta</i> by toggling on/off the suggested editorial accidentals using the "Hide/Show Editorial Accidentals" button. They can download the scores to tailor the accidentals to their own preferences.</div>

<br><br>

## Technical documentation {#technical-documentation} 

### Filenames {#filenames}

<div id="paragraph">Each piece is assigned a three-letter composer code, <a href="https://wiki.ccarh.org/wiki/Josquin_Project_encoding_standards#Composer_codes">assigned in close coordination with the Josquin Research Project</a>. Each work is then assigned a four-digit number. The first digit indicates the genre (1 for a mass; 2 for a motet; 3 for a secular work). The last two or three digits are an enumeration of the works in the given genre——typically, moving from the first circulating work by a composer to the last. For example, Wil2001 is the first circulating motet (or one of the first) by the composer Adrian Willaert. <br><br>

If a piece, such as a mass, consists of multiple parts, each section additionally has a letter. For instance, Wil1001a is the Kyrie from Willaert's <i>Missa Mente tota</i>; Will1001b is the Gloria.<br><br>

Where this project collaborates with existing editions, the first two digits reflect the volume in the series. For example, The 1520s Project incorporates scores from the <a href="https://senflonline-eng.com/new-senfl-edition/"><i>New Senfl Edition</i></a>. In this case, Snf0101 is the first work in the first volume of the <i>New Senfl Edition</i>. Following the NSE's numbering, Snf0238 is no. 38 in the overall series, found in the second volume.</div>

<br>

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

<div id="paragraph">The metadata for each piece includes the (probable) earliest source in the transmission and its dating. External links are provided to either <a href="https://www.diamm.ac.uk/">DIAMM</a> or <a href="https://rism.online/">RISM</a>.</div>

<br>

## Download project data {#download-data}

<a href="https://github.com/benory/1520s-project-scores">The project's Github repository</a>, which hosts Sibelius files, MusicXML files, Humdrum files, and PDFs, can be cloned in terminal by using the following command:

    git clone https://github.com/benory/1520s-project-scores.git

<br>