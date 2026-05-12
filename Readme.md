# Pharmaceutic Index — Claude Integration

Pharmaceutic Index integrates with Claude in two ways. Both give Claude access to our pharmaceutical press release database, but they suit different workflows:

| | **Claude Connector** | **Claude Code Plugin** |
|---|---|---|
| **Best for** | Claude.ai conversations (browser, mobile, desktop) | Claude Code (terminal-based AI coding agent) |
| **What it adds** | Search tool available in any Claude chat | Deal signal skill + search, with reports saved to disk |
| **Installation** | One click in Claude settings | One command in your terminal |
| **Free tier** | 7-day press release coverage, no account needed | 7-day press release coverage, no account needed |
| **Paid tier** | 30-day coverage | 30-day coverage |
| **Get it** | [Connect in Claude settings](#connector) | [Install from Claude Code marketplace](#plugin) or [Agensi](https://www.agensi.io/skills/pharma-deal-signal-monitor) |

---

<a name="connector"></a>
## Option 1 — Claude Connector

The connector is the quickest way to bring Pharmaceutic Index into Claude.ai. Once connected, Claude can search our pharmaceutical press release database directly within your conversations — no need to leave the chat or switch tools.

### What it does

The connector gives Claude access to a semantic search tool over our curated database of pharmaceutical industry press releases. When you ask Claude a question about recent pharma news, deals, clinical data, or pipeline updates, it can query Pharmaceutic Index and bring relevant results into the conversation.

Each search returns the most relevant press releases along with key metadata (title, company, date, source URL) and the passages most relevant to your query.

### What you can ask

The connector uses semantic search, which means it works best with descriptive, concept-based queries rather than specific company names or keywords. Here are some examples:

**Pipeline and clinical development**
- "What GLP-1 receptor agonists for obesity are advancing through late-stage trials?"
- "Are there any new oral weight loss pills getting approved?"
- "What bispecific antibody therapies in oncology have reported new clinical data?"

**Business development and deals**
- "Which gene therapy companies have been acquired recently?"
- "Any new manufacturing partnerships for cell therapy scale-up?"

**Therapeutic area research**
- "What's happening in liver disease drug development for fatty liver?"
- "New approaches to treating neurodegenerative diseases in clinical trials"
- "Recent regulatory approvals for rare blood disorders"

### How to connect

**If Pharmaceutic Index is listed in Claude's connector directory:**

1. Open Claude at [claude.ai](https://claude.ai)
2. Go to **Settings → Connectors**
3. Find **Pharmaceutic Index** and click **Connect**

You can also connect directly from within a conversation by clicking the integrations icon in the chat input area.

**To connect manually:**

1. Open Claude at [claude.ai](https://claude.ai)
2. Go to **Settings → Connectors → Add custom connector**
3. Enter the connector URL: `https://api.pharmaceuticindex.com/mcp`
4. Toggle it on for any conversation

No account or authentication is required for 7-day coverage.

### Access tiers

- **Free (no account):** 7-day press release coverage, no setup required
- **Free account:** 7-day coverage + email digests delivered on a schedule — no need to run searches manually. [Sign up](https://pharmaceuticindex.com/signup)
- **Paid account:** 30-day press release coverage + email digests. [View plans](https://pharmaceuticindex.com/pricing)

---

<a name="plugin"></a>
## Option 2 — Claude Code Plugin

The plugin is designed for users running Claude Code, Anthropic's terminal-based AI coding agent. It bundles a deal signal monitoring skill with the Pharmaceutic Index MCP connection, so Claude Code can run structured sweeps of recent pharma press releases and write prioritised signal reports to disk.

### What it adds

The plugin installs two things at once:

- **`pharma-deal-signal-monitor` skill** — instructs Claude Code to scan press releases across seven deal signal categories (positive clinical readouts, collaboration terminations, regulatory milestones, BD leadership hires, capital raises, IND filings, and explicit partnering language), synthesise findings into a ranked report, and save it as a dated markdown file in your `outputs/` folder.
- **Pharmaceutic Index MCP connection** — automatically configured; no manual URL entry needed.

### What a signal report looks like

Running the skill produces a prioritised deal signal report structured like this:

```
# Pharma BD Deal Signal Report
Generated: 2026-05-12
Signal window: last 7 days (free)

## ⚡ Compound Signals
Companies flagged across multiple signal categories — highest BD priority.

## Signal Findings by Category
Positive Clinical Readouts | Regulatory Milestones | Collaboration Terminations
BD Leadership Hires | Capital Raises | IND Filings | Explicit Partnering Language
```

Reports are saved to `outputs/deal-signal-report-YYYY-MM-DD.md` so weekly scans accumulate without overwriting each other.

### How to install

**From the Claude Code official marketplace (once listed):**

```bash
/plugin install pharma-deal-signal-monitor
```

**From Agensi:**

Download the skill zip from [agensi.io/skills/pharma-deal-signal-monitor](https://www.agensi.io/skills/pharma-deal-signal-monitor) and install into your skills directory:

```bash
mkdir -p .claude/skills/pharma-deal-signal-monitor
# unzip contents into that directory
```

**From GitHub:**

```bash
git clone https://github.com/BastiaanBergman/pharma-deal-signal-monitor \
  .claude/skills/pharma-deal-signal-monitor
```

Then restart Claude Code.

### Running the skill

Once installed, trigger it with a natural language prompt:

```
Scan for pharma BD deal signals this week
```

Or with a specific focus:

```
Scan for deal signals in oncology ADCs this week
Scan for collaboration terminations and asset reversions in rare disease
```

### Access tiers

- **Free (no account):** 7-day coverage, works immediately on install
- **Free account:** 7-day coverage + scheduled email digests. [Sign up](https://pharmaceuticindex.com/signup)
- **Paid account:** 30-day coverage + email digests. [View plans](https://pharmaceuticindex.com/pricing)

At the end of every free-tier report, the skill will suggest how to extend coverage — you won't be asked for credentials before the scan runs.

---

## Data coverage

Pharmaceutic Index covers press releases from major pharmaceutical and biotechnology companies, sourced from corporate investor relations pages and newswire services. The database is continuously updated.

- Free tier returns results from the **last 7 days**
- Paid accounts access results from the **last 30 days**
- Results reflect the most recently indexed releases; very recent publications may take a short time to appear

The connector and plugin both use semantic search. Descriptive, concept-based queries work best. Queries relying on exact company names or product strings may return less precise results.

---

## Privacy

Search queries are processed to return relevant results. No personal data is stored beyond what is needed to serve the request. For full details, see our [Privacy Policy](/privacy).

---

## Support

Questions or issues? Reach us at **info@pharmaceuticindex.com**
