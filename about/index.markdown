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

<h2>A new aesthetic paradigm</h2>

<p>Sometime during the 1520s, a new aesthetic paradigm for sacred European art music took hold.</p>

<p>Musical sources from this decade evince a decisive stylistic change: in place of what might be described as a contrastive aesthetic preferred by earlier composers, with individual lines coming and going, we now find nearly pervasive sonic saturation–that is, music for five or six independent voices with relatively few rests.</p>

<p>This new style, although easy enough to lay out in general terms, is not so easy to analyze. Making matters still more difficult is that scholars have long been unsure exactly how, when, and where these stylistic changes occurred, owing to limited information about composer biographies and a fuzzy understanding of seminal musical sources from the 1520s. As a result, historians have tended to tell an oversimplified story that prioritizes the major composers of the early sixteenth century, or those of the mid sixteenth century, at the expense of those in between.</p> 

<p>Complicating matters further: more works from during the 1520s survive than from any previous decade in Western music history. Indeed, more music survives than any individual scholar can hope to control.</p>

<h2>Meeting the challenge</h2>

<p>The 1520s Project aims to meet this challenge head on by making the repertoire of the early sixteenth century available for performance, study, and analysis. Founded in 2019 by <a href="https://benjaminory.com" target="_blank">Benjamin Ory</a>, the project offers high-quality digital editions of the music in four data types: as PDFs, as Sibelius files, as MusicXML files, and as Humdrum files. At present, the corpus features <span id="work-count"></span> scores and roughly <span id="note-count"></span> notes, making it the largest online database of music from the period in the world. The figure below shows the distribution of works by date of the first surviving source.</p>

<div id="years-plot"></div>

<p>The project takes advantage of <a href="/documentation" target="_blank">editorial and encoding standards</a> developed by the <a href="https://josquin.stanford.edu" target="_blank">Josquin Research Project</a> (JRP) over the past decade. This standardization enables the data from both projects to be shared; such interoperability is especially useful with respect to composers active right around 1520, such as Jean Mouton, Noel Bauldeweyn, or Jean Richafort, whose music is shared between projects.</p>

<h2>Editorial process</h2>

<p class="tight">To upload music, Ory:</p>
  <ul class="tight-list">
    <li>enters the music into Sibelius, using facsimiles and modern editions. Each note is checked for accuracy. Mensuration signs and section headings are added as appropriate.</li>
    <li>listens to the file, adjusting editorial accidentals (<em>musica ficta</em>) as appropriate.</li>
    <li>exports the file as a MusicXML file.</li>
    <li>translates the file into Humdrum syntax and adjusts metadata and mensuration signs.</li>
    <li>generates graphical scores using the <a href="https://verovio.humdrum.org" target="_blank">Verovio Humdrum Viewer</a>.</li>
    <li>updates the metadata on the <a href="https://docs.google.com/spreadsheets/d/1rVevNfKXd0g4NWOZdm2dG9sbQgOh5nOr_5G_2nizAgY/edit?usp=sharing" target="_blank">Google Sheet</a>.</li>
    <li>populates the relevant files in the <a href="https://github.com/benory/1520s-project" target="_blank">Github repository</a>.</li>
    <li>pushes the update to the website.</li>
  </ul>

<p>Do you see an mistake in a score? Do you disagree with our editorial choices? Would you like a particular score to be texted? <a href="mailto:The1520sProject@gmail.com">Let us know</a>.</p><br>

<h2>People</h2>

<div class="team-container">
    <div class="team-member">
        <img src="/images/headshots/Ory.jpg" alt="Benajmin Ory">
        <div class="bio">
            <h3>Benjamin Ory</h3>
            <p><strong>Director</strong></p>
            <p><a href="https://benjaminory.com" target="_blank">Benjamin Ory</a> is a Fonds Wetenschappelijk Onderzoek Junior Postdoctoral Fellow at Katholieke Universiteit Leuven. He received his PhD in musicology from Stanford University in 2022, and has since served as a Digital Humanities Fellow at Harvard University’s Villa I Tatti, as visiting assistant professor in musicology at Williams College, and as a postdoctoral fellow at Stanford. He is a co-director of <a href="https://renaissancemapping.org" target="_blank">Mapping the Musical Renaissance</a>. His research focuses on sixteenth-century polyphony as well as the early history of Renaissance musicology, with articles in the <a href="https://doi.org/10.1525/jams.2025.78.2.477" target="_blank"><i>Journal of the American Musicological Society</i></a> and the <a href="https://doi.org/10.1525/jm.2025.42.4.452" target="_blank"><i>Journal of Musicology</i></a>.</p>
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
    <div class="team-member">
        <img src="/images/headshots/Umbreit.jpg" alt="Janosch Umbreit">
        <div class="bio">
            <h3>Janosch Umbreit</h3>
            <p><b>Team Member</b></p>
            <p>Janosch Umbreit studied musicology, digital humanities, and English literature at the University of Regensburg, where he also worked as a research assistant for the Deutsche Forschungsgemeinschaft-funded research project <a href="https://orgelpredigt.ur.de/" target="_blank">Orgelpredigtdrucke</a>. He is currently part of the Specialized Information Service for Musicology (<a href="https://www.musiconn.de/en/" target="_blank">musiconn</a>) at the Bavarian State Library.</p><br>
            <p><a href="https://1520s-project.org/browse/?q=Umbreit" target="_blank" class="see-scores">See scores edited by Umbreit.</a></p>
        </div>
    </div>
    <div class="team-member">
        <img src="/images/headshots/Blistain.jpg" alt="Max Blistain">
        <div class="bio">
            <h3>Max Blistain</h3>
            <p><b>Team Member</b></p>
            <p>Max Blistain studied piano at the Royal Conservatory of Mons, Belgium. He is a piano teacher, accompanist and concert performer, mainly playing with his trio Star Vinsky, and he is studying musicology at the Free University of Brussels. Passionate about the heritage of his native region, his research focuses on Charles Chastelain (ca. 1490-1578), provost and musician at the Collégiale-Saint-Vincent in Soignies. He also conducts a choir to revive the Chastelain's works.</p><br>
            <p><a href="https://1520s-project.org/browse/?q=Blistain" target="_blank" class="see-scores">See scores edited by Blistain.</a></p>
        </div>
    </div>
</div>

<h3>Advisory Board</h3>
<ul id="advisory-list">
  <li>Philippe Canguilhem (Centre d'études supérieures de la Renaissance, Université de Tours)</li>
  <li>Antonio Chemotti (Katholieke Universiteit Leuven)</li>
  <li>Julie Cumming (McGill University)</li>
  <li>Karen Desmond (Maynooth University)</li>
  <li>Richard Freedman (Haverford College)</li>
  <li>Ichiro Fujinaga (McGill University)</li>
  <li>Sean Gallagher (New England Conservatory)</li>
  <li>Nori Jacoby (Cornell University)</li>
  <li>Marcin Konik (Fryderyk Chopin Institute, Warsaw)</li>
  <li>Laurent Pugin (Universität Bern/Répertoire International des Sources Musicales)</li>
  <li>Jamie Reuland (Princeton University)</li>
  <li>Emiliano Ricciardi (University of Massachusetts, Amherst)</li>
  <li>Joshua Rifkin (Boston University, emeritus)</li>
  <li>Katelijne Schiltz (Universität Regensburg)</li>
  <li>Philippe Vendrix (Centre d'études supérieures de la Renaissance, Université de Tours)</li>
  <li>Giovanni Zanovello (Indiana University)</li>
  <li>Emily Zazulia (University of California, Berkeley)</li>
</ul>

<h2>Support</h2>

<div class="support-section">
  <p>
    This project has been generously supported by <a href="https://itatti.harvard.edu/" target="_blank">Villa I Tatti</a>, Harvard's Center for Italian Renaissance Studies, as part of a <a href="https://propelgrants.stanford.edu" target="_blank">Stanford Vice Provost and Dean of Research Propel Grant</a>, by the <a href="https://cesta.stanford.edu" target="_blank"> Stanford Center for Spatial and Textual Analysis</a>, and by the <a href="http://www.ccarh.org" target="_blank">Stanford Center for Computer Assisted Research in the Humanities</a>.
  </p>

  <div class="support-logos-top">
    <a href="https://itatti.harvard.edu/" target="_blank">
      <img src="ITatti_logo.png" alt="i Tatti logo" class="support-logo">
    </a>
    <a href="https://cesta.stanford.edu/" target="_blank">
      <img src="CESTA_logo.png" alt="CESTA logo" class="support-logo">
    </a>
  </div>
  <div class="support-logos-bottom">
    <a href="http://www.ccarh.org/" target="_blank">
      <img src="CCARH_logo.png" alt="CCARH logo" class="support-logo">
    </a>
    <a href="https://propelgrants.stanford.edu" target="_blank">
      <img src="Propel_logo.png" alt="Propel Grant logo" class="support-logo">
    </a>
  </div>
</div>

<h2>Collaborations</h2>

<div id="paragraph"><h3>New Senfl Edition</h3>
  <div id="paragraph"> Thanks to Stefan Gasch, Birgit Lodes, and the <a href="https://senflonline-eng.com/new-senfl-edition/" target="_blank">New Senfl Edition</a> at the Universität für Musik und darstellende Kunst Wien for generously agreeing to contribute their scores to this project. See the <a href="https://1520s-project.org/browse/?q=senfl" target="_blank">available pieces</a>, each of which links to the New Senfl Edition's critical commentary.</div>
  <a href="https://senflonline-eng.com/new-senfl-edition/"><img src="/images/Senfl_banner.png" alt="Senfl Banner"></a>
</div>

<h2>Data Donations</h2>

<div id="paragraph"> Thanks to Marnix van Berchum, David Burn, Theodor Dumitrescu, Rex Eakins, Simon Frisch, Lance Morrison, and Jessie Ann Owens for generously donating data to the project. <a href="mailto:The1520sProject@gmail.com">Let us know</a> if you'd like to contribute data of your own.</div>