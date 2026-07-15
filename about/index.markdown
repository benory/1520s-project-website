---
layout: page
title: about
order: 1

---

<script src="https://cdn.jsdelivr.net/npm/vega@5.25.0"></script>
<script src="https://cdn.jsdelivr.net/npm/vega-lite@5.15.1"></script>
<script src="https://cdn.jsdelivr.net/npm/vega-embed@6.22.2"></script>

{% include_relative styles-local.html %}
{% include_relative scripts-local.html %}
{% include styles/styles-common.css.html %}

<div class="section-header"><h4>about</h4></div>

<p>The 1520s Project is an open-access digital library of music from ca. 1510 to ca. 1540. Users can browse, search, analyze, listen to, and perform from a growing corpus of Renaissance scores centered on the decades around 1520.</p>

<p>The project partners with the <a href="https://www.josqu.in" target="_blank">Josquin Research Project</a>, which focuses primarily on music from ca. 1400 to ca. 1520. From 2025 to 2028 both projects are supported by a National Endowment for the Humanities <a href="https://www.neh.gov/grants/research/scholarly-editions-and-translations-grants" target="_blank">Scholarly Editions & Translations Grant</a>.</p>

<h2>Emergence of a New Style</h2>

<p>Sometime during the 1520s, sacred European polyphony underwent a decisive aesthetic transformation. In place of the more contrastive aesthetic favored by earlier composers, with individual voices coming and going, much of the sacred music from the decade is marked by near-pervasive sonic saturation&mdash;that is, five or six independent voices sounding with relatively few rests.</p>

<p>This style is easy to describe in general terms but difficult to analyze in detail. Scholars have long been uncertain about exactly how, when, and where these changes occurred, in part because composer biographies remain fragmentary and many of the decade’s most important sources are still poorly understood. As a result, historians have tended to tell an oversimplified story that privileges either the major composers of the early sixteenth century or those of the mid-sixteenth century, often at the expense of those in between.</p>

<p>The problem is also one of scale. More music survives from the 1520s than from any previous decade in Western music history. More music survives than any individual scholar can hope to control.</p>

<h2>Aims and Scope</h2>

<p>The 1520s Project responds to this challenge by making the repertory of the early sixteenth century available for performance, study, and analysis. Founded in 2019 by <a href="https://benjaminory.com" target="_blank">Benjamin Ory</a>, the project offers high-quality digital editions in four formats: PDF, Sibelius, MusicXML, and Humdrum.</p>

<p>At present, the corpus includes <span id="work-count"></span> scores and roughly <span id="note-count"></span> notes, making it the largest online database of music from the period. The figure below shows the distribution of works by date of first surviving source.</p>

<div class="section-header"><h4>Number of Works by Year of First Source</h4></div>
<div id="years-plot"></div>

<p>The project takes advantage of <a href="/documentation" target="_blank">editorial and encoding standards</a> developed by the <a href="https://josqu.in" target="_blank">Josquin Research Project</a> (JRP). These standards allow data from the two projects to be shared and compared, creating a larger, interoperable corpus of early sixteenth-century music. This is especially useful for composers active around 1520, such as Jean Mouton, Noel Bauldeweyn, and Jean Richafort, whose music appears in both projects.</p>

<h2>Editorial workflow</h2>

<ol class="process-steps">
  <li>
    <strong>Score preparation.</strong>
    Music is entered into Sibelius or MuseScore from facsimiles and modern editions. Each note is checked for accuracy, and mensuration signs and section headings are added as appropriate.
  </li>
  <li>
    <strong>Editorial review.</strong>
    Files are reviewed aurally, with editorial accidentals (<em>musica ficta</em>) adjusted as needed.
  </li>
  <li>
    <strong>Format conversion.</strong>
    Scores are exported as MusicXML and translated into Humdrum syntax, with metadata and mensuration signs refined.
  </li>
  <li>
    <strong>Rendering.</strong>
    Graphical scores are generated using <a href="https://verovio.humdrum.org" target="_blank">Verovio Humdrum Viewer</a>.
  </li>
  <li>
    <strong>Publication.</strong>
    Metadata is updated in the project’s <a href="https://docs.google.com/spreadsheets/d/1rVevNfKXd0g4NWOZdm2dG9sbQgOh5nOr_5G_2nizAgY/edit?usp=sharing" target="_blank">Google Sheet</a>,
    files are committed to the
    <a href="https://github.com/benory/1520s-project" target="_blank">GitHub repository</a>,
    and the update is published to the website.
  </li>
</ol>

<p>Do you see a mistake in a score? Do you disagree with our editorial choices? Would you like a particular score to be texted? <a href="mailto:The1520sProject@gmail.com">Let us know</a>.</p>

<h2>People</h2>

<div class="team-container">
    <div class="team-member">
        <img src="/images/headshots/Ory.jpg" alt="Benjamin Ory">
        <div class="bio">
            <h3>Benjamin Ory</h3>
            <p class="role">Director</p>
            <p><a href="https://benjaminory.com" target="_blank">Benjamin Ory</a> is a Fonds Wetenschappelijk Onderzoek Junior Postdoctoral Fellow at Katholieke Universiteit Leuven. He received his PhD in musicology from Stanford University in 2022, and has since served as a Digital Humanities Fellow at Harvard University’s Villa I Tatti, as visiting assistant professor in musicology at Williams College, and as a postdoctoral fellow at Stanford. He is a co-director of <a href="https://renaissancemapping.org" target="_blank">Mapping the Musical Renaissance</a>. His research focuses on sixteenth-century polyphony as well as the early history of Renaissance musicology, with articles in the <a href="https://doi.org/10.1525/jams.2025.78.2.477" target="_blank"><i>Journal of the American Musicological Society</i></a> and the <a href="https://doi.org/10.1525/jm.2025.42.4.452" target="_blank"><i>Journal of Musicology</i></a>.</p>
        </div>
    </div>
    <div class="team-member">
        <img src="/images/headshots/Sapp.jpg" alt="Craig Sapp">
        <div class="bio">
            <h3>Craig Sapp</h3>
            <p class="role">Technical Director</p>
            <p>Craig Sapp is a world expert in computer-based musical analysis who develops transformative digital-humanities projects in collaboration with colleagues and students. As consulting professor at Stanford University, Sapp teaches courses in computational music theory and digital musicology. He serves as technical director of not only the <a href="https://josquin.stanford.edu" target="_blank">Josquin Research Project</a>, but also the NEH-funded <a href="https://www.tassomusic.org/" target="_blank">Tasso in Music Project</a>, and as technical lead for the <a href="https://chopin.musicsources.pl/en/" target="_blank">Chopin Heritage in Open Access project</a> (2016–20), the <a href="https://polish.musicsources.pl/pl" target="_blank">Polish Music in Open Access project</a> (2019–22), and the <a href="https://polyrhythm.humdrum.org" target="_blank">Polyrhythm Project</a> (2018–present). He served as a consultant for the <a href="https://gaspar-van-weerbeke.eu" target="_blank">Gaspar Online Edition</a> (2021–22).</p>
        </div>
    </div>
    <div class="team-member">
        <img src="/images/headshots/Rodin.jpg" alt="Jesse Rodin">
        <div class="bio">
            <h3>Jesse Rodin</h3>
            <p class="role">Collaborator</p>
            <p>Jesse Rodin is the Osgood Hooker Professor of Fine Arts (Department of Music) at Stanford University. He has published many books and articles on Renaissance music, including, most recently, the monograph <a href="https://www.cambridge.org/us/universitypress/subjects/music/medieval-and-renaissance-music/art-counterpoint-du-fay-josquin" target="_blank"><i>The Art of Counterpoint from Du Fay to Josquin</i></a> (Cambridge University Press, 2024). Rodin directs the vocal ensemble <a href="https://cutcircle.org/" target="_blank">Cut Circle</a> as well as the <a href="https://josquin.stanford.edu/" target="_blank">Josquin Research Project</a>, a tool for exploring a large musical corpus. He is the recipient of awards and fellowships from organizations such as the American Council of Learned Societies, the American Musicological Society, and the Guggenheim Foundation.</p>
        </div>
    </div>
    <div class="team-member">
        <img src="/images/headshots/Sugg.jpg" alt="Maura Sugg">
        <div class="bio">
            <h3>Maura Sugg</h3>
            <p class="role">Team Member</p>
            <p>Maura Sugg recently completed her PhD in musicology at Case Western Reserve University. Her dissertation, "More Than Meets the Ear: Crafting and Embodying Post-Tridentine Catholicism in Tomás Luis de Victoria’s Imitation Masses,” explores how Victoria created layers of meaning for Catholic singers in the post-Tridentine period. She was a 2025–26 recipient of an American Musicological Society <a href="https://www.amsmusicology.org/funding/ams-50/" target="_blank">Alvin H. Johnson AMS 50 Dissertation Fellowship</a>. Her digital humanities experience includes work with the <a href="https://sites.google.com/haverford.edu/crim-project/home" target="_blank">CRIM (Citations: The Renaissance Imitation Mass) Project</a>.</p>
            <p><a href="https://1520s-project.org/repertoire/?q=Sugg" target="_blank" class="see-scores">See scores edited by Sugg.</a></p>
        </div>
    </div>
    <div class="team-member">
        <img src="/images/headshots/Umbreit.jpg" alt="Janosch Umbreit">
        <div class="bio">
            <h3>Janosch Umbreit</h3>
            <p class="role">Team Member</p>
            <p>Janosch Umbreit studied musicology, digital humanities, and English literature at the University of Regensburg, where he also worked as a research assistant for the Deutsche Forschungsgemeinschaft-funded research project <a href="https://orgelpredigt.ur.de/" target="_blank">Orgelpredigtdrucke</a>. He is currently part of the Specialized Information Service for Musicology (<a href="https://www.musiconn.de/en/" target="_blank">musiconn</a>) at the Bavarian State Library.</p>
            <p><a href="https://1520s-project.org/repertoire/?q=Umbreit" target="_blank" class="see-scores">See scores edited by Umbreit.</a></p>
        </div>
    </div>
    <div class="team-member">
        <img src="/images/headshots/Blistain.jpg" alt="Max Blistain">
        <div class="bio">
            <h3>Max Blistain</h3>
            <p class="role">Team Member</p>
            <p>Max Blistain studied piano at the Royal Conservatory of Mons, Belgium. He is a piano teacher, accompanist and concert performer, mainly playing with his trio Star Vinsky, and he is studying musicology at the Free University of Brussels. Passionate about the heritage of his native region, his research focuses on Charles Chastelain (ca. 1490-1578), provost and musician at the Collégiale-Saint-Vincent in Soignies. He also conducts a choir to revive Chastelain's works.</p>
            <p><a href="https://1520s-project.org/repertoire/?q=Blistain" target="_blank" class="see-scores">See scores edited by Blistain.</a></p>
        </div>
    </div>
    <div class="team-member">
        <img src="/images/headshots/Nivarlet.jpg" alt="David Nivarlet">
        <div class="bio">
            <h3>David Nivarlet</h3>
            <p class="role">Team Member</p>
            <p>David Nivarlet is a research assistant in early modern palaeography at CESR (University of Tours). His research focuses on HTR technology applied to fifteenth- and sixteenth-century civic archives. He previously interned at KBR (Royal Library of Belgium), where he contributed to the federal research project <a href="https://www.alamirefoundation.org/en/news/start-fed-twin-programma-from-script-to-sound/" target="_blank">From Script to Sound: Connecting Heritage and Art through Research and Technology</a>.</p>
            <p><a href="https://1520s-project.org/repertoire/?q=Nivarlet" target="_blank" class="see-scores">See scores edited by Nivarlet.</a></p>
        </div>
    </div>
</div>

<h2>Advisory Board</h2>
<ul id="advisory-list">
  <li>David Burn (Katholieke Universiteit Leuven)</li>
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
  <p>From 2025 to 2028 the project is supported by a National Endowment for the Humanities <a href="https://www.neh.gov/grants/research/scholarly-editions-and-translations-grants" target="_blank">Scholarly Editions & Translations Grant</a>.</p>
  
  <p>At earlier stages this project was made possible by <a href="https://itatti.harvard.edu/" target="_blank">Villa I Tatti</a>, Harvard's Center for Italian Renaissance Studies, as part of a <a href="https://propelgrants.stanford.edu" target="_blank">Stanford Vice Provost and Dean of Research Propel Grant</a>, by the <a href="https://cesta.stanford.edu" target="_blank"> Stanford Center for Spatial and Textual Analysis</a>, and by the <a href="http://www.ccarh.org" target="_blank">Stanford Center for Computer Assisted Research in the Humanities</a>.</p>

  <div class="support-logos-neh">
    <a href="https://www.neh.gov/" target="_blank">
      <img src="/images/NEH_logo.png" alt="National Endowment for the Humanities logo" class="support-logo support-logo-neh">
    </a>
    <a href="http://www.ccarh.org/" target="_blank">
      <img src="/images/CCARH_logo.png" alt="CCARH logo" class="support-logo support-logo-ccarh">
    </a>
    <a href="https://cesta.stanford.edu/" target="_blank">
      <img src="/images/CESTA_logo.png" alt="CESTA logo" class="support-logo">
    </a>
  </div>
  <div class="support-logos-secondary">
    <a href="https://itatti.harvard.edu/" target="_blank">
      <img src="/images/ITatti_logo.png" alt="i Tatti logo" class="support-logo">
    </a>
    <a href="https://propelgrants.stanford.edu" target="_blank">
      <img src="/images/Propel_logo.png" alt="Propel Grant logo" class="support-logo">
    </a>
  </div>
</div>

<h2>Project reviews</h2>

<figure class="scholarly-block review-block">
  <blockquote>
    <p>"The 1520s Project is another step ahead... the project features an exquisite and thorough treatment of the metadata and a sophisticated array of analytical tools."</p>
  </blockquote>
  <figcaption>
    Frans Wiering, ed., “Making Corpus Creation in Early Music Rewarding and Effective: Finding the Optimum Between Standardisation and Autonomy” (Utrecht University, 2025), 24. <a href="https://zenodo.org/records/17543932" target="_blank">https://doi.org/10.5281/zenodo.17543932</a>
  </figcaption>
</figure>

<h2>Collaborations</h2>

<div class="scholarly-block collaboration-block">
  <h3>New Senfl Edition</h3>

  <div class="scholarly-block-content">
    <p>
      Thanks to Stefan Gasch, Birgit Lodes, and the <a href="https://senflonline-eng.com/new-senfl-edition/" target="_blank"> New Senfl Edition
      </a> at the Universität für Musik und darstellende Kunst Wien for generously agreeing to contribute <a href="https://1520s-project.org/browse/?q=senfl" target="_blank">their scores</a> to this project.
    </p>
    <a href="https://senflonline-eng.com/new-senfl-edition/" class="scholarly-logo"><img src="/images/Senfl_banner.png" alt="Senfl Banner">
    </a>
  </div>
</div>

<h2>Data Donations</h2>

<p> Thanks to Marnix van Berchum, David Burn, Theodor Dumitrescu, Rex Eakins, Simon Frisch, Irene Holzer, Lance Morrison, Jessie Ann Owens, and Zoe Saunders for generously donating data to the project. <a href="mailto:The1520sProject@gmail.com">Let us know</a> if you'd like to contribute data of your own.</p>
