# Error Report Worker

This Worker receives the work-page error report popup, verifies the Cloudflare
Turnstile token, maps the public popup field names to private Google Forms
`entry.*` field IDs, and forwards the report to a Google Form.

## Required setup

1. Create a Google Form with these fields:
   - Category
   - Description
   - Email address
   - Work or page being reported
   - User agent
2. Find each Google Forms `entry.*` field ID and copy it into the Worker
   environment variables in `wrangler.toml`.
3. Copy `wrangler.toml.example` to `wrangler.toml`, then set:
   - `GOOGLE_FORM_POST_URL`
   - `GOOGLE_FORM_ENTRY_CATEGORY`
   - `GOOGLE_FORM_ENTRY_TARGET`
   - `GOOGLE_FORM_ENTRY_DESCRIPTION`
   - `GOOGLE_FORM_ENTRY_EMAIL`
   - `GOOGLE_FORM_ENTRY_USER_AGENT`
   - `ALLOWED_ORIGINS`
4. Add the Turnstile secret with:

```sh
wrangler secret put TURNSTILE_SECRET_KEY
```

5. Deploy the Worker and copy its URL into `_config.yml` as
   `error_report.worker_url`.
6. Copy the Turnstile site key into `_config.yml` as
   `error_report.turnstile_sitekey`.

Only `worker_url` and `turnstile_sitekey` belong in the public Jekyll config.
The Google Form URL and field IDs stay in the Cloudflare Worker configuration.
