# Conversion tracking, UTMs and attribution

A base tag tells the ad platform that someone visited. It does not tell it that a conversion came out of the
visit. This file covers the UTM convention (no code), the conversions to create, the client-side event (code),
and the tickets to write when the host has gaps.

## UTM convention

No code needed, and it must be identical across every post campaign so analytics can compare posts.

```
utm_source=linkedin
utm_medium=paid                     organic for the author's and the company page's posts
utm_campaign=post-{short slug}      one value per blog post campaign
utm_content={ad id, lowercase}     si-01 for the ad named SI-01, and so on, never reused
```

Lowercase, hyphens, no spaces. The ad is named by its id in the platform (`SI-01`), and the `utm_content`
value and the row in the tracking sheet are that id lowercased (`si-01`). That equality, ignoring case, is the
only join key between the platform's numbers and the host's.

## Conversions to create

| Conversion | Type | Rule or trigger | Category | Notes |
| :-- | :-- | :-- | :-- | :-- |
| Intent page view | Page load | URL starts with the sign-in or form page | Key page view | Works with the base tag alone |
| Conversion page reached | Page load | URL starts with the conversion page | Sign up | A proxy. Over-counts returning users |
| Conversion started | Event-specific | First record written | Lead | Needs the code below |
| Conversion completed | Event-specific | Submitted | Lead | Needs the code below |

Settings that fit small B2B campaigns: 30-day click and 7-day view windows, last touch, no monetary value
until Sales agrees one. Prefer the plain **Lead** category over "Qualified lead", which the platform ties to
its own CRM-oriented setup flow.

An event-specific conversion issues a numeric id inside a snippet such as `lintrk('track', { conversion_id:
12345678 })`. **Copy only the number.** Do not paste the snippet into the site. A page-load conversion's id
cannot be used in a track call.

Check the account for existing conversions before creating any; duplicates split the counts.

## The client-side event

Requirements the implementation must meet, each one an entry in [provenance.md](provenance.md):

| Requirement | Why |
| :-- | :-- |
| Read consent **at fire time**, per destination | The vendor function stays defined on `window` after its component unmounts, so checking `typeof window.lintrk` alone ignores a consent withdrawal mid-session |
| Marketing consent gates the ad platform, analytics consent gates analytics | They are different legal categories. One flag for both leaks data one way or the other |
| Fire once per (conversion, record) | UI effects re-run over the whole message or state list on every change |
| Dedupe in `localStorage`, tolerate it being blocked | A rare duplicate beats a lost conversion |
| A missing id means "skip that destination", never an error | Conversions are created in the ad account later than the code ships |
| Do not send the record id or any personal data | The event name is enough |

Whether ids live in code or in environment variables is the host's call. Vendor ids are public in the page
source either way. Hardcoding beside the existing partner id is simpler; public env vars need a redeploy
anyway because they are inlined at build time.

```ts
// conversions.ts
export type ConsentState = {
  analytics?: boolean;
  marketing?: boolean;
};

export type FunnelConversion = "conversion_started" | "conversion_completed";

const CONSENT_STORAGE_KEY = "cookie-consent";
const FIRED_KEY_PREFIX = "conversion-fired";

// Event-specific conversion ids issued by the ad platform.
// `null` means the conversion does not exist yet and is not reported.
const AD_PLATFORM_CONVERSION_IDS: Record<FunnelConversion, number | null> = {
  conversion_started: null,
  conversion_completed: null,
};

declare global {
  interface Window {
    lintrk?: (action: "track", data: { conversion_id: number }) => void;
    gtag?: (command: "event", eventName: string) => void;
  }
}

export function parseConsent(stored: string | null): ConsentState {
  if (!stored) return {};
  try {
    const parsed: unknown = JSON.parse(stored);
    return parsed && typeof parsed === "object" ? (parsed as ConsentState) : {};
  } catch {
    return {};
  }
}

/** True the first time a (conversion, record) pair is seen in this browser. */
function claim(kind: FunnelConversion, recordId: string): boolean {
  const key = `${FIRED_KEY_PREFIX}:${kind}:${recordId}`;
  try {
    if (localStorage.getItem(key)) return false;
    localStorage.setItem(key, String(Date.now()));
  } catch {
    // Storage blocked: an occasional duplicate beats a lost conversion.
  }
  return true;
}

export function trackFunnelConversion(kind: FunnelConversion, recordId: string): void {
  if (typeof window === "undefined" || !recordId) return;

  let consent: ConsentState = {};
  try {
    consent = parseConsent(localStorage.getItem(CONSENT_STORAGE_KEY));
  } catch {
    return;
  }
  if (consent.marketing !== true && consent.analytics !== true) return;
  if (!claim(kind, recordId)) return;

  const conversionId = AD_PLATFORM_CONVERSION_IDS[kind];
  if (consent.marketing === true && conversionId !== null && typeof window.lintrk === "function") {
    window.lintrk("track", { conversion_id: conversionId });
  }

  if (consent.analytics === true && typeof window.gtag === "function") {
    window.gtag("event", kind);
  }
}
```

Rename `FunnelConversion`'s members to the host's vocabulary (`brief_created`, `demo_booked`), and read the
consent key and shape from the host's consent component. Call `trackFunnelConversion` from the place the UI
first learns the record exists, for example an effect over the server's responses. Because of `claim`,
re-running over the whole list is safe.

Tests worth keeping: nothing is sent without consent; analytics consent alone never reaches the ad platform;
one event per record and per kind; a `null` id skips the ad platform; a filled id is sent as exactly
`("track", { conversion_id })`.

## Tickets to write when the probe finds gaps

Put these in the runbook's engineering table with a priority. Do not block a first small run on them, except
where marked.

| Ticket | Priority |
| :-- | :-- |
| **First-party UTM capture.** On first page load with `utm_*` present, store them in a first-party cookie (90 days, first touch wins). Read it where the conversion is recorded server-side and persist campaign and ad id beside the conversion. Show both where Sales reviews conversions | Do before launch if possible. With one campaign per post and a handful of conversions a month, it is the only way to say which post produced which conversion. Mention it in the privacy notice |
| **Analytics events**: conversion-link click on the post, engaged read (75% scroll or 60 s) | High. At about 100 paid readers a month these are the only numbers large enough to steer by |
| **Event-specific conversion** as above | Medium. URL rules are a usable proxy at first |
| **Keep the query string through auth redirects** | Only if ads will ever point at the conversion page (retargeting). Until then link to the sign-in URL with the redirect and UTMs on it |
| **Server-side conversions API** | Later. Recovers cross-device conversions. It is still marketing processing and must respect the visitor's consent choice; needs a legal check |

## Reporting without UTM capture

For each conversion, note date, country and company (from the email domain). Compare with the platform's
company demographics for the same dates. A company in both is a **likely** ad-sourced conversion, never a
confirmed one. Also ask in the first sales reply how they heard about the offer. The honest campaign measure
is the uplift over a baseline taken in the 28 days before launch.

## Tracking checklist

- [ ] UTM scheme written into the runbook with a full example URL per ad
- [ ] Existing conversions in the account listed before any are created
- [ ] Event code reads consent at fire time and dedupes per record
- [ ] Ids copied as numbers, stored where the host keeps its other vendor ids
- [ ] Conversion tested in a browser profile without an ad blocker; test record deleted
- [ ] Baseline for the 28 days before launch written down
