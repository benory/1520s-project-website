

/////////////////////////////
//
// getCgiParameters -- Extract the CGI parameters from the URL of the page.
//     id = File ID for the work to display, such as Jac2001.
//

function getCgiParameters() {
  let url = window.location.search.substring(1);
  let output = {};
  if (!url) {
    return output;
  }

  let settings = url.split('&');
  for (let setting of settings) {
    let [key, value] = setting.split('=');
    let decodedKey = decodeURIComponent(key);
    if (!decodedKey) {
      continue;
    }
    let decodedValue = decodeURIComponent(value);

    if (typeof output[decodedKey] === 'undefined') {
      output[decodedKey] = decodedValue;
    } else if (typeof output[decodedKey] === 'string') {
      output[decodedKey] = [output[decodedKey], decodedValue];
    } else {
      output[decodedKey].push(decodedValue);
    }
  }

  return output;
}



