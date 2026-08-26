function sendFormResponseEmail(e) {
  const recipient = "the1520sproject@gmail.com";
  const data = readFormSubmitEvent(e);

  const get = (...labels) => {
    for (const label of labels) {
      const value = data[normalizeHeader(label)];
      if (value) return value;
    }
    return "";
  };

  const category = get("Category");
  const target = get("Work or page being reported", "Target", "Page URL");
  const description = get("Description");
  const email = get("Email address", "Your name / contact information");
  const userAgent = get("User Agent", "User agent");
  const timestamp = get("Timestamp");
  const isContactSubmission = normalizeHeader(category) === "contact";

  const body = isContactSubmission
    ? [
        "A new contact message was received:",
        "",
        "Email:",
        email,
        "",
        "Page:",
        target,
        "",
        "Message:",
        description,
        "",
        "Submitted:",
        timestamp,
      ].join("\n")
    : [
        "A new error report was received:",
        "",
        "Email:",
        email,
        "",
        "Work or page being reported:",
        target,
        "",
        "Description:",
        description,
        "",
        "Submitted:",
        timestamp,
        "",
        "User agent:",
        userAgent,
      ].join("\n");

  MailApp.sendEmail({
    to: recipient,
    subject: isContactSubmission
      ? "[1520s Project] New contact message"
      : `[1520s Project] Error report: ${target || "New response"}`,
    body: body,
    replyTo: isEmail(email) ? email : recipient,
    name: "The 1520s Project",
  });
}

function readFormSubmitEvent(e) {
  const data = {};

  if (!e) {
    data.error = "No event object received. This function must run from a trigger.";
    return data;
  }

  if (e.response && typeof e.response.getItemResponses === "function") {
    data.timestamp = String(e.response.getTimestamp() || "");

    e.response.getItemResponses().forEach((itemResponse) => {
      const title = itemResponse.getItem().getTitle();
      const response = itemResponse.getResponse();
      data[normalizeHeader(title)] = Array.isArray(response) ? response.join(", ") : String(response || "");
    });

    return data;
  }

  if (e.namedValues) {
    Object.keys(e.namedValues).forEach((key) => {
      data[normalizeHeader(key)] = e.namedValues[key] && e.namedValues[key][0] ? e.namedValues[key][0] : "";
    });

    return data;
  }

  if (e.range && e.values) {
    const sheet = e.range.getSheet();
    const headers = sheet.getRange(1, 1, 1, e.values.length).getDisplayValues()[0];

    headers.forEach((header, index) => {
      data[normalizeHeader(header)] = e.values[index] || "";
    });

    return data;
  }

  data.error = "Unrecognized Apps Script trigger event.";
  data.event_keys = Object.keys(e).join(", ");
  return data;
}

function normalizeHeader(value) {
  return String(value || "").trim().toLowerCase().replace(/\s+/g, " ");
}

function isEmail(value) {
  return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(value || "");
}
