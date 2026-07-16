const TURNSTILE_VERIFY_URL = "https://challenges.cloudflare.com/turnstile/v0/siteverify";

const DEFAULT_ALLOWED_ORIGINS = [
	"https://1520s-project.org",
	"https://www.1520s-project.org",
	"http://localhost:4000",
	"http://127.0.0.1:4000",
	"http://localhost:4001",
	"http://127.0.0.1:4001",
	"http://localhost:8888",
	"http://127.0.0.1:8888",
];

const GOOGLE_FORM_ENTRY_ENV = {
	category: "GOOGLE_FORM_ENTRY_CATEGORY",
	target: "GOOGLE_FORM_ENTRY_TARGET",
	description: "GOOGLE_FORM_ENTRY_DESCRIPTION",
	email: "GOOGLE_FORM_ENTRY_EMAIL",
	user_agent: "GOOGLE_FORM_ENTRY_USER_AGENT",
};

export default {
	async fetch(request, env) {
		let origin = request.headers.get("Origin") || "";
		let corsOrigin = getCorsOrigin(origin, env.ALLOWED_ORIGINS);

		if (request.method === "OPTIONS") {
			return new Response(null, {
				status: corsOrigin ? 204 : 403,
				headers: corsHeaders(corsOrigin),
			});
		}

		if (origin && !corsOrigin) {
			return jsonResponse({ ok: false, error: "Origin not allowed" }, 403, corsOrigin);
		}

		if (request.method !== "POST") {
			return jsonResponse({ ok: false, error: "Method not allowed" }, 405, corsOrigin);
		}

		if (!isWorkerConfigured(env)) {
			return jsonResponse({ ok: false, error: "Worker is not configured" }, 500, corsOrigin);
		}

		let formData;
		try {
			formData = await request.formData();
		} catch (error) {
			return jsonResponse({ ok: false, error: "Invalid form data" }, 400, corsOrigin);
		}

		let report = readReport(formData);
		if (!report.description || !report.email || !report.target) {
			return jsonResponse({ ok: false, error: "Missing required fields" }, 400, corsOrigin);
		}

		let turnstileToken = formData.get("cf-turnstile-response");
		if (!turnstileToken || typeof turnstileToken !== "string") {
			return jsonResponse({ ok: false, error: "Missing verification token" }, 400, corsOrigin);
		}

		let turnstileResult = await verifyTurnstile(
			turnstileToken,
			env.TURNSTILE_SECRET_KEY,
			request.headers.get("CF-Connecting-IP")
		);

		if (!turnstileResult.success) {
			return jsonResponse({ ok: false, error: "Verification failed" }, 400, corsOrigin);
		}

		let googleResponse = await fetch(env.GOOGLE_FORM_POST_URL, {
			method: "POST",
			body: buildGoogleFormData(report, env),
		});

		if (!googleResponse.ok) {
			return jsonResponse({ ok: false, error: "Google Form submission failed" }, 502, corsOrigin);
		}

		return jsonResponse({ ok: true }, 200, corsOrigin);
	},
};

function isWorkerConfigured(env) {
	if (!env.GOOGLE_FORM_POST_URL || !env.TURNSTILE_SECRET_KEY) {
		return false;
	}
	return Object.values(GOOGLE_FORM_ENTRY_ENV).every(function(envName) {
		return Boolean(env[envName]);
	});
}

function readReport(formData) {
	return {
		category: readString(formData, "category") || "Error report",
		target: readString(formData, "target"),
		description: readString(formData, "description"),
		email: readString(formData, "email"),
		user_agent: readString(formData, "user_agent"),
	};
}

function readString(formData, name) {
	let value = formData.get(name);
	return typeof value === "string" ? value.trim() : "";
}

function buildGoogleFormData(report, env) {
	let googleFormData = new FormData();
	for (let fieldName of Object.keys(GOOGLE_FORM_ENTRY_ENV)) {
		let googleEntryName = env[GOOGLE_FORM_ENTRY_ENV[fieldName]];
		googleFormData.append(googleEntryName, report[fieldName] || "");
	}
	googleFormData.append("fvv", "1");
	googleFormData.append("pageHistory", "0");
	return googleFormData;
}

async function verifyTurnstile(token, secret, remoteIp) {
	let formData = new FormData();
	formData.append("secret", secret);
	formData.append("response", token);
	if (remoteIp) {
		formData.append("remoteip", remoteIp);
	}

	let response = await fetch(TURNSTILE_VERIFY_URL, {
		method: "POST",
		body: formData,
	});

	if (!response.ok) {
		return { success: false };
	}

	return response.json();
}

function getCorsOrigin(origin, configuredOrigins) {
	if (!origin) {
		return "*";
	}
	let allowedOrigins = parseAllowedOrigins(configuredOrigins);
	return allowedOrigins.includes(origin) ? origin : "";
}

function parseAllowedOrigins(configuredOrigins) {
	if (!configuredOrigins) {
		return DEFAULT_ALLOWED_ORIGINS;
	}
	return configuredOrigins
		.split(",")
		.map(function(origin) {
			return origin.trim();
		})
		.filter(Boolean);
}

function corsHeaders(origin) {
	let headers = {
		"Access-Control-Allow-Methods": "POST, OPTIONS",
		"Access-Control-Allow-Headers": "Content-Type",
		"Vary": "Origin",
	};

	if (origin) {
		headers["Access-Control-Allow-Origin"] = origin;
	}

	return headers;
}

function jsonResponse(body, status, origin) {
	return new Response(JSON.stringify(body), {
		status,
		headers: {
			...corsHeaders(origin),
			"Content-Type": "application/json; charset=utf-8",
			"Cache-Control": "no-store",
		},
	});
}
