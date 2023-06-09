---
layout: page
---

{% include_relative scripts-local.html %}

<style>
   .wrapper {margin-left: 10px;}
   .page-content {mid-width: 500px;}
}
</style>

<script src="https://plugin.humdrum.org/scripts/humdrum-notation-plugin-worker.js">
</script>

<script>
   let cgi = getCgiParameters(); 
   let filename = "Cha2001-De_profundis_clamavi.krn";
   let matches = filename.match(/([A-Z][a-z][a-z])(\d{4}[^-]*)-/);
   let composer = matches[1];
   let id = matches[1] + matches[2];
   // In the future I need to allow for main instead of master:
   // let url = `https://github.com/benory/1520s-project/blob/main/humdrum/${composer}/${id}/${filename}`;
   let url = `https://raw.githubusercontent.com/benory/1520s-project/main/humdrum/${composer}/${filename}`;
              https://raw.githubusercontent.com/benory/1520s-project/main/humdrum/Cha/Cha2001-De_profundis_clamavi.krn
   displayHumdrum({
      source: "my-score",
      url: url,
      autoResize: "true",
      header: "true"
   });
<!-- See https://plugin.humdrum.org/options/#list for more display options -->
</script>

<script type="text/x-humdrum" id="my-score">
</script>
