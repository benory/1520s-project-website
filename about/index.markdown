---
layout: page
title: about
order: 1

---

<script async src="https://www.googletagmanager.com/gtag/js?id=G-38882FHV3H"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());

  gtag('config', 'G-38882FHV3H');
</script>

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

Would you like a particular score to be texted? [Let us know.](mailto:The1520sProject@gmail.com)<br><br>

## People

<div class="team-container">
    <div class="team-member">
        <img src="/images/headshots/Ory.jpg" alt="Benajmin Ory">
        <div class="bio">
            <h3>Benjamin Ory</h3>
            <p><strong>Director</strong></p>
            <p><a href="https://benjaminory.com" target="_blank">Benjamin Ory</a> is a Fonds Wetenschappelijk Onderzoek Junior Postdoctoral Fellow at Katholieke Universiteit Leuven. He received his PhD in musicology from Stanford University in 2022, and has since served as a Digital Humanities Fellow at Harvard University’s Villa I Tatti, as visiting assistant professor in musicology at Williams College, and as a postdoctoral fellow at Stanford. He is a co-director of <a href="https://renaissancemapping.org" target="_blank">Mapping the Musical Renaissance</a>. His research focuses on sixteenth-century polyphony as well as the early history of Renaissance musicology, with forthcoming articles in the <i>Journal of the American Musicological Society</i> and the <i>Journal of Musicology</i>.</p>
        </div>
    </div>
    <div class="team-member">
        <img src="/images/headshots/Sapp.jpg" alt="Craig Sapp">
        <div class="bio">
            <h3>Craig Sapp</h3>
            <p><b>Technical Director</b></p>
            <p>Craig Sapp is a world expert in computer-based musical analysis who develops transformative digital-humanities projects in collaboration with colleagues and students. As consulting professor at Stanford University, Sapp teaches courses in computational music theory and digital musicology. He serves as technical director of not only the <a href="https://josquin.stanford.edu" target="_blank">Josquin Research Project</a>, but also the NEH-funded <a href="https://www.tassomusic.org/" target="_blank">Tasso in Music Project</a>, and as technical lead for the <a href="https://chopin.musicsources.pl/en/" target="_blank">Chopin Heritage in Open Access project</a> (2016–20), the <a href="https://polish.musicsources.pl/pl" target="_blank">Polish Music in Open Access project</a> (2019–22), and the <a href="https://polyrhythm.humdrum.org" target="_blank">Polyrhythm Project</a> (2018–present). He served as a consultant for the <a href="https://gaspar-van-weerbeke.eu" target="_blank">Gaspar Online Edition</a> (2021–22).</p>
        </div>
    </div>
    <div class="team-member">
        <img src="/images/headshots/Rodin.jpg" alt="Jesse Rodin">
        <div class="bio">
            <h3>Jesse Rodin</h3>
            <p><b>Collaborator</b></p>
            <p>Jesse Rodin is the Osgood Hooker Professor of Fine Arts (Department of Music) at Stanford University. He has published many books and articles on Renaissance music, including, most recently, the monograph <a href="https://www.cambridge.org/us/universitypress/subjects/music/medieval-and-renaissance-music/art-counterpoint-du-fay-josquin" target="_blank">The Art of Counterpoint from Du Fay to Josquin</a> (Cambridge University Press, 2024). Rodin directs the vocal ensemble <a href="https://cutcircle.org/" target="_blank">Cut Circle</a> as well as the <a href="https://josquin.stanford.edu/" target="_blank">Josquin Research Project</a>, a tool for exploring a large musical corpus. He is the recipient of awards and fellowships from organizations such as the American Council of Learned Societies, the American Musicological Society, and the Guggenheim Foundation.</p>
        </div>
    </div>
</div>

### Advisory Board

<div id="paragraph">Philippe Canguilhem (Centre d'études supérieures de la Renaissance, Université de Tours)<br>
Antonio Chemotti (Katholieke Universiteit Leuven) <br>
Julie Cumming (McGill University) <br>
Karen Desmond (Maynooth University) <br>
Richard Freedman (Haverford College) <br>
Ichiro Fujinaga (McGill University) <br>
Sean Gallagher (New England Conservatory) <br>
Nori Jacoby (Cornell University) <br>
Marcin Konik (Fryderyk Chopin Institute, Warsaw) <br> 
Laurent Pugin (Universität Bern/Répertoire International des Sources Musicales)<br>
Jamie Reuland (Princeton University) <br>
Emiliano Ricciardi (University of Massachusetts, Amherst) <br>
Joshua Rifkin (Boston University, emeritus) <br>
Katelijne Schiltz (Universität Regensburg) <br>
Philippe Vendrix (Centre d'études supérieures de la Renaissance, Université de Tours) <br>
Giovanni Zanovello (Indiana University) <br>
Emily Zazulia (University of California, Berkeley)

</div><br>

## Support

This project has been generously supported by [Villa I Tatti](https://itatti.harvard.edu/){:target="_blank"}, Harvard's Center for Italian Renaissance Studies, as part of a [Stanford Vice Provost and Dean of Research Propel Grant](https://propelgrants.stanford.edu){:target="_blank"}, by the [Stanford Center for Spatial and Textual Analysis](https://cesta.stanford.edu){:target="_blank"}, and by the [Stanford Center for Computer Assisted Research in the Humanities](http://www.ccarh.org){:target="_blank"}.

[![i Tatti logo](ITatti_logo.png)](https://itatti.harvard.edu/){:target="_blank"} [![CESTA logo](CESTA_logo.png)](https://cesta.stanford.edu/){:target="_blank"}[![CCARH logo](CCARH_logo.png)](http://www.ccarh.org/){:target="_blank"}[![Propel Grant logo](Propel_logo.png)](https://propelgrants.stanford.edu){:target="_blank"}<br><br>

## Collaborations

<div id="paragraph"><h3>New Senfl Edition</h3>
  <div id="paragraph"> Thanks to Stefan Gasch, Birgit Lodes, and the <a href="https://senflonline-eng.com/new-senfl-edition/" target="_blank">New Senfl Edition</a> at the Universität für Musik und darstellende Kunst Wien for generously agreeing to contribute their scores to this project. See the <a href="https://1520s-project.org/browse/?q=senfl" target="_blank">available pieces</a>, each of which links to the New Senfl Edition's critical commentary.</div>
  <a href="https://senflonline-eng.com/new-senfl-edition/"><img src="/images/Senfl_banner.png" alt="Senfl Banner"></a>
</div>