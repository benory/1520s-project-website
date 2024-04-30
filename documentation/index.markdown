---
layout: default
---

<style>
	#paragraph {
		padding-left: 30px;
	}
</style>

### Table of contents
- [Download The 1520s Project's data](#download-data)
- [Musical documentation and editorial standards](#editorial-standards)
	- [Instrument names](#instrument-names)
	- [Sections](#sections)
	- [Note values and Mensurstriche](#notes)
	- [Mensuration signs](#mensuration-signs)
	- [Terminal notes and fermatas](#final-notes)
	- [Editorial accidentals](#editorial-accidentals)
- [Technical documentation](#technical-documentation)
	- [Filenames](#filenames)
	- [Score preparation](#score-preparation)
	- [Encoded information](#encoded-information)
	- [Source metadata](#source-metadata)

<br>

## Download The 1520s Project's data {#download-data}

<div id="paragraph"><li><a href="https://github.com/benory/1520s-project-scores">The project's Github repository</a> hosts Sibelius files, MusicXML files, Humdrum files, and PDFs.</li></div>

<br>

## Musical documentation and editorial standards {#editorial-standards}

<div id="paragraph">The 1520s Project provides high quality data with consistent editorial standards between scores. These editorial standards are similar to those used by the <a href="https://josquin.stanford.edu/">Josquin Research Project</a>.</div>

<br>

#### Instrument names {#instrument-names}

<div id="paragraph">Early sixteenth-century musical sources use interchangeable names for voices, such as Superius, Cantus, and Discantus; Tenor II, Quintus, and Sextus. Different sources for a given piece may use different names for the same music. <br><br> For consistency, this project exclusively uses superius, altus, tenor, and bassus. When there are more than four voices, the project will assign the most logical voice, followed by a roman numeral (i.e., Tenor II).</div>

<br>

#### Sections {#sections}

<div id="paragraph">Each section in a piece is separated by a double bar, or at the end of the piece, a final barline. The start of each section of a piece should have a section label (for instance, "Secunda pars: Ave solem genuisti").</div>

<br>

#### Note values and Mensurstriche {#notes}

<div id="paragraph">All scores appear on The 1520s Project with unreduced note values (in other words, a breve is equal to a double whole note; a minim, a half note).<br><br><i>Mensurstriche</i>, a scholarly practice that allows note values to cross over a modern bar line without using a tie, is avoided as this format is not easily readable for computers.</div>

<br>

#### Mensuration signs {#mensuration-signs}

<div id="paragraph">Where possible, scores use the mensuration signs found in the earliest source for a given piece. <br><br> Note: the Music Encoding Initiative (MEI) has not yet made it possible to reproduce all original mensuration signs, especially those with a sign numerator and numerical demoninator (e.g., Cut-C over 3).

</div>

<br>

#### Terminal notes and fermatas {#terminal-notes}

<div id="paragraph">Terminal notes are defined as the last note in a given voice prior to a double barline or the end of a given work. They are displayed as longs regardless of their actual durations.<br><br> Fermatas on terminal notes are removed, as terminal longs represent an indefinite value. The placement of fermatas elsewhere follows the musical sources.</div>

<br>

#### Editorial accidentals {#editorial-accidentals}

<div id="paragraph">Editorial accidentals, often known as <i>musica ficta</i>, are suggested by this project under two circumstances:<br><br>
<li>Avoiding harmonic tritones</li> <br><ul>In the following example, taken from the bassus of Noel Bauldeweyn's <a href="https://1520s-project.org/work/?id=Bau3001"><i>En douleur en tristesse</i></a>, a tritone in m. 14 is avoided by adding a flat to the e. A second tritone with the stepwise motion in m. 15 is avoided by adding a second flat. <br><img src="/images/Bau3001_ficta_example.png" alt="Bauldeweyn ficta example"></ul>

<li>Inflecting at cadences</li> <br><ul>Editorial accidentals are added when moving from an imperfect consonance to a perfect consonance (in this repertoire, almost always sixth-to-octave motion). In early sixteenth-century music, this sixth-to-octave motion is usually preceded by a seven-to-six suspension in the top voice. See mm. 59–62 of Nicolas Champion's <a href="https://1520s-project.org/work/?id=Bau3001"><i>De profundis clamavi</i></a>, which features a seven-to-six suspension followed by movement to an octave: <br><br><img src="/images/Cha2001_ficta_example.png" alt="Champion ficta example"><br><br>

This project further argues that cadences not only have a contrapuntal element, but also function as part of a rhetorical gesture: to be classified as a cadence, these contrapuntal elements must occur where one or both of the voices end a text phrase. Usually——but not always——one or both of the voices will rest following the cadence.</ul>

Users can see the scores without <i>ficta</i> by toggling on/off the suggested editorial accidentals using the "Hide/Show Editorial Accidentals" button. They can also download the scores to tailor the music to their own preferences.</div>

<br><br>

## Technical documentation {#technical-documentation} 

#### Filenames {#filenames}

<div id="paragraph">Each piece is assigned a three-letter composer code, <a href="https://wiki.ccarh.org/wiki/Josquin_Project_encoding_standards#Composer_codes">assigned in close coordination with the Josquin Research Project</a>. Each work is assigned a four-digit number. The first digit indicates the genre (1 for a mass; 2 for a motet; 3 for a secular work). The last two or three digits are an enumeration of the works in the given genre——typically, moving from the first circulating work by a composer to the last. For example, Wil2001 would be the first circulating motet (or one of the first) by Adrian Willaert. <br><br>

If a piece, such as a mass, consists of multiple parts, each section additionally has a letter. For instance, Wil1001a is the Kyrie from Willaert's <i>Missa Mente tota</i>; Will1001b is the Gloria.<br><br>

In the case of collaborations with existing editions, the first two digits reflect the volume in the series. For example, this project incorporates scores from the <a href="https://senflonline-eng.com/new-senfl-edition/"><i>New Senfl Edition</i></a>. In this case, Snf0101 is the first work in the first volume of the <i>New Senfl Edition</i>. Following the NSE's numbering, Snf0238 is no. 38 in the overall series, found in the second volume.</div>

<br>

#### Score preparation {#score-preparation}

<div id="paragraph"> Each score is imported into Sibelius and then is prepared in the following ways:
<div id="paragraph"> 
	<li>Any <i>Mensurstriche</i> is removed.</li>
	<li>Adjust instrument names.</li>
	<li>Editorial accidentals are adjusted and placed in parentheses.</li>
	<li>Metadata (title, subtitles for sections, composer, encoder) is added to the score.</li>
	<li>The staff size is changed to 5.5 mm.</li>
	<li>System brackets are removed.</li>
	<li>Final notes and fermatas are adjusted</li>
	<li>Information about canonic material is given</li>
</div><br>

Ory then listens carefully to each score for adjusts editorial accidentals and mistakes. Scores are then exported to MusicXML files and converted using the <a href="https://extras.humdrum.org/man/xml2hum/">musicxml2hum command</a> in the Humdrum Extras toolkit.

</div>

<br>

#### Encoded information {#encoded-information}

<div id="paragraph"> Information encoded in humdrum scores:
<div id="paragraph"> 
	<li>id: the ID for the work</li>
	<li>AGN: the genre</li>
	<li>voices: the number of voices</li>
	<li>COM: the composer </li>
	<li>OTL: the title of the work</li>
	<li>ENC: the encoder</li>
	<li>END: the date of the encoding</li>
</div><br>

For scores coming from existing published editions:
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

#### Source metadata {#source-metadata}

<div id="paragraph">The metadata for each piece includes the (probable) earliest source in the transmission and its dating. External inks are provided to either <a href="https://www.diamm.ac.uk/">DIAMM</a> or <a href="https://rism.online/">RISM</a>.</div>