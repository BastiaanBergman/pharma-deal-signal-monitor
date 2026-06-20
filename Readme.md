# Pharmaceutic Index: Claude Integration

Pharmaceutic Index works inside Claude through two pieces. A connector gives Claude live semantic search over our pharmaceutical press release database. A deal signal skill builds on it to run structured sweeps and produce ranked reports. The skill needs the connector.

---

## Connector

The connector adds a semantic search tool over our curated database of pharmaceutical press releases to any Claude conversation. Ask about recent pharma news, deals, clinical data, or pipeline updates, and Claude pulls relevant releases into the chat, each with its title, company, date, source URL, and the passages that match your query.

Semantic search rewards descriptive, concept-based queries over exact company names or product strings. For example:

- "GLP-1 receptor agonists for obesity advancing through late-stage trials"
- "bispecific antibody therapies in oncology with new clinical data"
- "gene therapy companies acquired recently"
- "recent regulatory approvals for rare blood disorders"

### Connect

If Pharmaceutic Index is in Claude's connector directory, open Settings, then Connectors, find Pharmaceutic Index, and click Connect. You can also connect from within a conversation using the integrations icon in the chat input.

To add it manually, go to Settings, then Connectors, then Add custom connector, and enter:

```
https://api.pharmaceuticindex.com/mcp
```

No account or authentication is needed for 7-day coverage.

---

## Deal signal skill

The skill turns the connector into a structured workflow. It sweeps recent press releases across seven deal signal categories (positive clinical readouts, regulatory milestones, collaboration terminations, BD leadership hires, capital raises, IND filings, and explicit partnering language), ranks the findings, and produces a dated report you can download. Run it weekly and each scan is its own file.

A report is structured like this:

```
# Pharma BD Deal Signal Report
Generated: 2026-05-12
Signal window: last 7 days (free)

## ⚡ Compound Signals
Companies flagged across multiple categories, the highest BD priority.

## Signal Findings by Category
Positive Clinical Readouts | Regulatory Milestones | Collaboration Terminations
BD Leadership Hires | Capital Raises | IND Filings | Explicit Partnering Language
```

### Install

Download the skill from [Agensi](https://www.agensi.io/skills/pharma-deal-signal-monitor) or the [GitHub repo](https://github.com/BastiaanBergman/pharma-deal-signal-monitor). The downloaded zip installs directly as a Claude skill, with no unzipping or file paths needed: add it in Claude's settings and turn it on.

The skill requires the Pharmaceutic Index connector above. Connect that first, or just run the skill: on its first scan it gives you the one-line setup if the connection is missing.

### Run

Trigger it in natural language:

```
Scan for pharma BD deal signals this week
Scan for deal signals in oncology ADCs this week
```

Free-tier reports end with a note on extending coverage. You are never asked for credentials before a scan runs.

---

## Access and coverage

- **Free, no account:** 7-day coverage, works immediately.
- **Free account:** 7-day coverage plus scheduled email digests. [Sign up](https://pharmaceuticindex.com/signup).
- **Paid account:** 30-day coverage plus email digests. [Plans](https://pharmaceuticindex.com/pricing).

Releases are sourced from corporate investor relations pages and newswire services and indexed continuously. Very recent publications may take a short time to appear.

---

## Privacy and support

Queries are processed only to return results. No personal data is stored beyond what serves the request. See the [Privacy Policy](https://pharmaceuticindex.com/privacy). Questions: **info@pharmaceuticindex.com**
