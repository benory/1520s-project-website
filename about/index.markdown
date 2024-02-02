---
layout: page
title: about
---

<script src="https://cdn.jsdelivr.net/npm/vega@5.25.0"></script>
<script src="https://cdn.jsdelivr.net/npm/vega-lite@5.15.1"></script>
<script src="https://cdn.jsdelivr.net/npm/vega-embed@6.22.2"></script>

{% include_relative styles-local.html %}
{% include_relative scripts-local.html %}

## A new aesthetic paradigm

Sometime during the 1520s, a new aesthetic paradigm for sacred European art music took hold. 

Musical sources from this decade evince a decisive stylistic change: in place of what might be described as a contrastive aesthetic preferred by earlier composers, with individual lines coming and going, we now find nearly pervasive sonic saturation–that is, music for five or six independent voices with relatively few rests. 

This new style, although easy enough to lay out in general terms, is not so easy to analyze. Making matters still more difficult is that scholars have long been unsure exactly how, when, and where these stylistic changes occurred, owing to limited information about composer biographies and a fuzzy understanding of seminal musical sources from the 1520s. As a result, historians have tended to tell an oversimplified story that prioritizes the major composers of the early sixteenth century, or those of the mid sixteenth century, at the expense of those in between. 

Complicating matters further: more works from during the 1520s survive than from any previous decade in Western music history. Indeed, more music survives than any individual scholar can hope to control.

## Meeting the challenge

The 1520s Project aims to meet this challenge head on by making the repertoire of the early sixteenth century available for performance, study, and analysis. Founded in 2019 by [Benjamin Ory](https://benjaminory.com){:target="_blank"}, the project offers high-quality digital editions of the music in four data types: as PDFs, as Sibelius files, as MusicXML files, and as Humdrum files. At present, the corpus features <span id="work-count"></span> scores and roughly <span id="note-count"></span> notes, making it the largest online database of music from the period in the world. The figure below shows the distribution of works by date of the first surviving source.

<div id="years-plot"></div>

The project takes advantage of [editorial and encoding standards](https://wiki.ccarh.org/wiki/Josquin_Project_encoding_standards){:target="_blank"} developed by the [Josquin Research Project](https://josquin.stanford.edu){:target="_blank"} (JRP) over the past decade. This standardization enables the data from both projects to be shared; such interoperability is especially useful with respect to composers active right around 1520, such as Jean Mouton, Noel Bauldeweyn, or Jean Richafort.

## Editorial process

To upload music, Ory:
+ enters the music into Sibelius, using facsimiles and modern editions. Each note is checked for accuracy. Mensuration signs and section headings are added as appropriate.
+ listens to the file, adjusting editorial accidentals (_musica ficta_) as appropriate.
+ exports the file as a MusicXML file.
+ translates the file into Humdrum syntax and adjusts metadata and mensuration signs.
+ generates graphical scores using the [Verovio Humdrum Viewer](https://verovio.humdrum.org){:target="_blank"}.
+ updates the metadata to the [Google Sheet](https://docs.google.com/spreadsheets/d/1rVevNfKXd0g4NWOZdm2dG9sbQgOh5nOr_5G_2nizAgY/edit?usp=sharing){:target="_blank"}.
+ populates the relevant files in the [Github repository](https://github.com/benory/1520s-project){:target="_blank"}.

Do you see an mistake in a score? Do you disagree with the proposed editorial accidentals? Please feel free to email Ory with an [error report](mailto:The1520sProject@gmail.com).

Would you like a particular score to be texted? [Let us know.](mailto:The1520sProject@gmail.com)

## Collaborations

### New Senfl Edition

Thanks to Stefan Gasch, Birgit Lodes, and the [New Senfl Edition](https://senflonline-eng.com/new-senfl-edition/) at the Universität für Musik und darstellende Kunst Wien for generously agreeing to contribute their scores to this project. See the [currently available pieces](/browse/?q=senfl), each of which links to the New Senfl Edition's critical commentary.

[![Senfl Banner](/images/Senfl_banner.png)](https://senflonline-eng.com/new-senfl-edition/)

## Support

This project has been generously supported by the [Stanford Center for Spatial and Textual Analysis](https://cesta.stanford.edu){:target="_blank"}, as part of a [Stanford Vice Provost and Dean of Research Propel Grant](https://propelgrants.stanford.edu){:target="_blank"}, and by the [Stanford Center for Computer Assisted Research in the Humanities](http://www.ccarh.org){:target="_blank"}.

[![CESTA logo](CESTA_logo.png)](https://cesta.stanford.edu/){:target="_blank"} [![CCARH logo](CCARH_logo.png)](http://www.ccarh.org/){:target="_blank"}[![Propel Grant logo](Propel_logo.png)](https://propelgrants.stanford.edu){:target="_blank"}

## People

Benjamin Ory, Project Director ([benjaminory@gmail.com](mailto:benjaminory@gmail.com))

Craig Sapp, Technical Director ([craigsapp@stanford.edu](mailto:craigsapp@stanford.edu))