---
name: aso-helper
description: Optimize app store keywords for iOS App Store and Google Play Store. Use when researching keywords, analyzing keyword performance, generating keyword suggestions, or optimizing app metadata for ASO. Triggers on mentions of ASO, app store optimization, keywords, app listing, app metadata, store ranking, analyze description, keyword frequency, extract keywords, optimize existing description, iOS keyword field, 100 character limit, or trademark check.
---

# ASO Helper

Keyword research, analysis, and optimization for iOS App Store and Google Play Store.

---

## ⚠️ Setup Required (One-Time)

**Before using this skill, install these dependencies:**

```bash
# Python dependencies (for iOS autocomplete + rankings)
pip install selenium webdriver-manager

# Node.js dependencies (for Google Play data)
npm install google-play-scraper aso
```

**Also required:**
- Python 3.x
- Node.js 14+
- Chrome browser (for Google Play rankings)

**Verify installation:**
```bash
python -c "import selenium; print('✓ selenium')"
node -e "require('google-play-scraper'); console.log('✓ google-play-scraper')"
```

If any dependency is missing, the scraper will fail and you'll get pattern-based estimates instead of real data.

---

## Before Starting: Ask User Preferences

**CRITICAL: Ask ALL 3 questions in ONE AskUserQuestion call. NEVER assume preferences. NEVER skip questions. The user must always have control over what analysis they receive.**

Use AskUserQuestion with all 3 questions together:

### Question 1: Output Detail Level
- **Quick** - Just the optimized keywords/description (copy-paste ready)
- **Standard** - Issues found + optimized output
- **Full Analysis** - Complete breakdown with keyword data, frequency tables, and recommendations

### Question 2: Include Rankings & Popularity?
- **Yes - Full metrics** - Fetch app rankings + keyword popularity scores (slower, requires scraper)
- **Popularity only** - Just keyword popularity from autocomplete (faster)
- **No metrics** - Skip data fetching, pattern-based analysis only (fastest)

### Question 3: Focus Areas (Multi-select)
- **Keyword optimization** - Frequency, density, positioning
- **Branded/trademark check** - Flag competitor and trademark keywords
- **Trend research** - WebSearch for current ASO trends
- **Utilization check** - Character limit usage (Google Play)

**Example AskUserQuestion call:**
```
questions: [
  { question: "What level of detail?", header: "Detail", options: [Quick, Standard, Full Analysis], multiSelect: false },
  { question: "Include rankings & popularity data?", header: "Metrics", options: [Full metrics, Popularity only, No metrics], multiSelect: false },
  { question: "What should I focus on?", header: "Focus", options: [Keyword optimization, Branded check, Trend research, Utilization check], multiSelect: true }
]
```

---

## Data Transparency & Error Handling

**ALWAYS be transparent with the user about what data is real vs estimated.**

### Data Source Labels

Include this in every analysis output:

| Data | Source | Type |
|------|--------|------|
| Autocomplete Suggestions | Apple/Google API | **REAL** |
| Popularity Score | Position in autocomplete | **ESTIMATED** |
| App Ranking | iTunes Search / Play Store API | **REAL** (requires App ID) |
| Keyword Density | Calculated from description | **REAL** |
| Trend Keywords | WebSearch | **REAL** (current sources) |

### Error Notifications

**If the scraper fails, IMMEDIATELY tell the user:**
```
⚠️ Scraper failed: [specific error message]
Falling back to pattern-based analysis. Results are ESTIMATES only.
To get real data, ensure dependencies are installed:
  pip install selenium webdriver-manager
  npm install google-play-scraper aso
```

### Missing Data Callouts

**If App ID not provided:**
```
ℹ️ App rankings not available. Provide your App ID to see where you rank for each keyword.
- iOS: From URL apps.apple.com/app/your-app/id123456789 → use 123456789
- Android: From URL play.google.com/store/apps/details?id=com.company.app → use com.company.app
```

**If API returns empty results:**
```
⚠️ No autocomplete data for "[keyword]" — either very low search volume or API issue.
```

**NEVER silently fall back to estimates. ALWAYS notify the user.**

---

## Quick Start

**Analyze Google Play Description:**
```
Platform: Google Play
App Name: [Your App Name]
App ID: [com.yourcompany.appname from Play Store URL]
Category: [e.g., Sports, Games, Productivity]
Description:
---
[Paste full description here]
---
```

**Analyze iOS Keyword Field:**
```
Platform: iOS
App Name: [Your App Name]
App ID: [numeric ID from App Store URL, e.g., 123456789]
Category: [e.g., Sports, Games, Productivity]
Keywords: [comma,separated,keywords,no,spaces]
```

**How to find your App ID:**
- **iOS:** From URL `apps.apple.com/app/your-app/id123456789` → use `123456789`
- **Android:** From URL `play.google.com/store/apps/details?id=com.company.app` → use `com.company.app`

---

## Real-Time Keyword Data

Fetch keyword popularity, app rankings, and branded status using free methods (no API keys needed).

> **Accuracy Note:** Popularity scores below are **rough estimates** based on autocomplete position, NOT actual search volume. Services like AppFollow use Apple Search Ads data which is more accurate. Use these for general guidance; verify critical decisions with paid tools.

### Popularity Score (1-100)

**iOS App Store - Get autocomplete position:**
```bash
curl -s "https://search.itunes.apple.com/WebObjects/MZSearchHints.woa/wa/hints?clientApplication=Software&term=[keyword]" -H "X-Apple-Store-Front: 143441-1,29"
```

**Convert position to score:**
| Autocomplete Position | Popularity Score | Meaning |
|----------------------|------------------|---------|
| 1 (first result) | 95-100 | Extremely popular |
| 2-3 | 80-94 | Very popular |
| 4-6 | 60-79 | Popular |
| 7-10 | 40-59 | Moderate |
| Not in top 10 | 20-39 | Low popularity |
| No suggestions | 1-19 | Very low / niche |

**Google Play - Get traffic score:**
```bash
node -e "require('aso')('gplay').scores('[keyword]').then(r=>console.log(r.traffic.score*10))"
```
Multiply traffic.score (0-10) by 10 to get 1-100 scale.

### App Ranking Lookup

**iOS - Find your app's rank for a keyword:**
```bash
curl -s "https://itunes.apple.com/search?term=[keyword]&country=us&entity=software&limit=200"
```
Search the JSON results for your App ID (trackId field). Position in array = your rank.

**Google Play:**
```bash
node -e "require('aso')('gplay').search({term:'[keyword]',num:100}).then(r=>{let i=r.findIndex(a=>a.appId==='[APP_ID]');console.log(i>=0?'#'+(i+1):'Not ranked')})"
```

### Branded Keyword Detection

**Step 1: WebSearch for competitors**
```
"[category] top apps [current year]"
```
Extract competitor app names → mark keywords matching these as **Branded**

**Step 2: Check against known brands**
Platform brands to flag: Google, Apple, Microsoft, Amazon, Meta, Samsung, Facebook, Instagram, TikTok, Snapchat, Twitter/X, WhatsApp, YouTube, Netflix, Spotify, Uber, Lyft, Airbnb, PayPal, Venmo

**Mark as Branded if:**
- Matches a competitor app name (from WebSearch)
- Contains a platform/company trademark
- Matches a well-known brand in the category

**Output format:** Only show "**Branded**" if detected, leave cell blank otherwise

### Country Codes (X-Apple-Store-Front header)
| Country | Code |
|---------|------|
| US | `143441-1,29` |
| UK | `143444-1,29` |
| Canada | `143455-1,29` |
| Australia | `143460-1,29` |
| Germany | `143443-1,29` |
| France | `143442-1,29` |

---

## Google Play Description Analysis

### Phase 1: Extract & Count Keywords

1. Extract all words from description
2. Filter stopwords (see Reference section)
3. Count frequency of each meaningful keyword
4. Calculate percentage of total meaningful words

**Categorize into:**
- **High-value**: Core terms appearing 2+ times or in title/first line
- **Secondary**: Supporting terms appearing 1-2 times
- **Missing**: Relevant keywords not present

### Phase 2: Assess Quality

**Fetch Real Keyword Metrics:**
For each high-value keyword identified in Phase 1, run:
```bash
npx aso gplay scores "[keyword]"
```

Record difficulty and traffic scores. Prioritize keywords with:
- Low difficulty (<5) AND high traffic (>5) = Best targets
- High difficulty (>7) OR low traffic (<3) = Consider replacing

**Position Scoring:**
| Position | Weight | Why |
|----------|--------|-----|
| Title (first 30 chars) | Highest | Direct ranking factor |
| First line of description | High | Sets context for algorithm |
| First 167 chars | High | Visible in search results |
| Body (168-4000 chars) | Medium | Supports density |

**Density Targets:**
| Density | Assessment | Action |
|---------|------------|--------|
| Under 1% | ❌ Too low | Must increase significantly |
| 1-2% | ⚠️ Below optimal | Increase to hit 2-3% |
| **2-3%** | **✓ Optimal** | **Target range for primary keywords** |
| 3-4% | ✓ Acceptable | Fine if natural |
| Over 5% | ❌ Stuffing risk | Reduce immediately |

**Target Density by Keyword Priority:**
| Priority | Keywords | Target Density | Occurrences (in 600 words) |
|----------|----------|----------------|---------------------------|
| Primary | 3-5 core keywords | **2.5-3%** | 15-18x each |
| Secondary | 5-10 supporting | 1.5-2% | 9-12x each |
| Tertiary | 10+ related | 0.5-1% | 3-6x each |

**Character Utilization:**
| Utilization | Assessment | Action |
|-------------|------------|--------|
| Under 50% | ❌ Critical | Must expand significantly |
| 50-70% | ⚠️ Underutilized | Expand with keyword-rich content |
| 70-85% | ✓ Good | Continue expanding if possible |
| **85-95%** | **✓ Optimal** | **Target range (3,400-3,800 chars)** |
| 95-100% | ✓ Maxed | Ideal if content remains natural |

**Expansion Strategies (when under 85%):**
- Detailed feature explanations (2-3 sentences per feature)
- Use cases: "Perfect for fans who want to..."
- Comparison phrases: "Get faster updates than..."
- FAQ-style content: "Looking for live scores? Check..."
- Seasonal content: "Follow the 2025-26 season with..."
- Benefits: "Never miss a goal with instant notifications"
- Social proof: "Join millions of fans tracking..."

**Currency Check:**
- Use today's date to determine current year
- Flag any year before current year as outdated (e.g., if current year is 2027, flag "2026", "25-26")
- Recommend updates: past year → current year, past season → current/next season
- WebSearch for upcoming major events in current and next year

**Quality Checklist:**
| Criteria | Target |
|----------|--------|
| Primary keyword in title | Yes |
| Keywords in first 167 chars | 5-7 unique |
| Unique relevant keywords | 15+ |
| Primary keywords at 2-3% density | 3-5 keywords |
| Secondary keywords at 1.5-2% density | 5-10 keywords |
| Year references current | Yes (no past seasons) |
| **Character utilization** | **85%+ (3,400+ chars)** |

### Phase 3: Research Trends

Use WebSearch with 1-2 queries:
```
"[category] app keywords ASO [current year]"
"[competitor app] app store optimization"
```

Extract: trending terms, competitor keywords, seasonal opportunities.

### Phase 4: Optimize

**Provide recommendations:**
1. **Keywords to add** - From research, with suggested placement (title/first 167/body)
2. **Primary keywords to maximize** - Push to 2.5-3% density (15-18 occurrences)
3. **Secondary keywords to increase** - Push to 1.5-2% density (9-12 occurrences)
4. **Keywords to reduce** - Currently over 5%, reduce to 2-3%
5. **Expand description** - If under 85% utilization, add content until 3,400+ chars

**Provide before/after metrics:**
| Metric | Before | After |
|--------|--------|-------|
| Total words | [X] | [X] |
| Unique keywords | [X] | [X] |
| Keywords at optimal density | [X] | [X] |
| Keywords in first 167 chars | [X] | [X] |
| Character utilization | [X]% | [X]% |

**Provide optimized description:**
- Full rewritten text with changes applied
- Follow Writing Style Guidelines to maintain human tone
- Highlight key changes in recommendations summary

---

## Writing Style Guidelines

When generating optimized descriptions, follow these rules to ensure human-sounding output:

**Match the Original Tone:**
- Preserve the original description's voice (casual, professional, playful, etc.)
- If the original uses dashes for lists, keep using dashes
- Match the level of formality and enthusiasm

**Structure & Headers:**
- Headers and sections CAN be added if they genuinely improve readability
- Good reasons to add structure: grouping related features, breaking up walls of text, highlighting key sections
- Bad reasons: making it "look organized", filling space, following a template
- Headers should be plain text (e.g., "Live Scores" not "📊 LIVE SCORES")
- Limit to 2-4 sections maximum — more feels templated
- Each section should have substance, not just 1-2 bullet points

**Avoid AI Patterns:**
| Pattern to Avoid | Example | Instead |
|------------------|---------|---------|
| Emoji headers | 📊 LIVE SCORES | Live Scores (or no header) |
| Generic superlatives | "the ultimate", "all-in-one", "best way to" | Use specific value props |
| Filler phrases | "all in one place", "everything you need" | Cut or replace with specifics |
| Formulaic lists | Every bullet starts with verb | Vary sentence structure |
| Manufactured social proof | "Join millions of fans" | Only if verifiable/original had it |
| Over-structured sections | 6+ identical sections | 2-4 sections max, only when needed |
| Repetitive sentence openers | "Get... Get... Get..." | Vary: "Check", "See", "Your" |

**Keyword Integration:**
- Weave keywords into existing sentences rather than adding new bullet points
- Expand existing feature descriptions rather than creating new sections
- Use synonyms and natural variations (scores/results, alerts/notifications)
- A slightly awkward keyword placement is worse than omitting it

**Expansion Approach (when under 70% utilization):**
- Elaborate on features already mentioned, don't add invented features
- Add details the user would actually want to know
- Extend existing paragraphs before creating new sections
- If adding content, match the surrounding style exactly

---

## iOS Keyword Field Analysis

### Phase 1: Analyze Field

1. **Count total characters** of the keyword string
   - Count the literal string length (including all commas)
   - Example: `Photo,Editor` = 12 chars total
   - Example: `a,b,c` = 5 chars total
   - **Do NOT add up keywords + commas separately** — count the actual string
   - Verify: `Soccer,Goal,Draw,UECL` = 21 chars (not 4 words + 3 commas calculated separately)
2. Count keywords
3. Flag issues:
   - Spaces after commas (waste)
   - Words in app name (redundant)
   - Trademark/competitor terms

### Phase 2: Assess Each Keyword

**Fetch Keyword Popularity:**
For each keyword in the field, check if it appears in App Store autocomplete:
```bash
curl -s "https://search.itunes.apple.com/WebObjects/MZSearchHints.woa/wa/hints?clientApplication=Software&term=[keyword]" -H "X-Apple-Store-Front: 143441-1,29"
```

Assess each keyword:
- **High value:** Appears in top 3 suggestions OR is an exact match
- **Medium value:** Appears in suggestions 4-10
- **Low value:** Does not appear in autocomplete results (low search volume)

Evaluate relevance and issues for every keyword.

| Assessment | Flag If |
|------------|---------|
| Trademark | Competitor app or brand name |
| Redundant | Already in app name |
| Unrelated | Wrong category/competition |
| Low value | Generic or year numbers |

### Phase 3: Research Trends

Same WebSearch as Google Play workflow.

### Phase 4: Generate TWO Options

**Option 1: Safe (Recommended)**
- Remove all flagged keywords
- Replace with trending alternatives
- **Target 95-100 chars** — unused characters = missed keyword opportunities
- If under 95 chars after replacements, add more relevant keywords until near limit

**Option 2: Aggressive (User's Risk)**
- Keep competitor/trademark keywords
- **Target 95-100 chars**
- Maximum visibility, risk of rejection

**Character Budget Rule:**
- Always aim for 95-100 chars used
- If a recommendation is under 95 chars, list additional keywords to fill the gap
- Prioritize: high-relevance terms > trending terms > synonyms/variations

**⚠️ CRITICAL: Character Count Validation**

**BEFORE outputting ANY keyword recommendation, you MUST verify the character count.**

1. **Run validation:**
```bash
echo -n "[your,keyword,string]" | wc -c
```

2. **NEVER trust mental math.** The limit is exactly 100 characters.

3. **Include character breakdown in output:**
```markdown
| Keyword | Chars |
|---------|-------|
| Soccer | 6 |
| football | 8 |
| Champions | 9 |
| ... | ... |
| **Keywords total** | X |
| **Commas (n-1)** | X |
| **TOTAL** | **X/100** |
```

4. **If total > 100:** Remove lowest-value keywords until ≤100, then re-verify.

5. **Show the verified count:** `✅ Verified: X/100 characters`

---

## Output Formats

**Use the format matching the user's chosen detail level:**

### Quick Output (Detail Level: Quick)

**Google Play:**
```
[Full optimized description - ready to copy/paste]
```

**iOS:**
```
[optimized,keywords,here,ready,to,paste]
```
No tables, no analysis - just the deliverable.

---

### Standard Output (Detail Level: Standard)

**Google Play:**
```markdown
**Length:** [X]/4000 ([X]%) | **Issues:** [X]

| Issue | Fix |
|-------|-----|
| [problem] | [action] |

## Optimized Description
[Full text]

## Top Keywords (Optimized)
| Keyword | Count | Density | Target | Status |
|---------|-------|---------|--------|--------|
| [primary keywords] | 15x | 2.5% | 2-3% | ✓/⚠️ |
| [secondary keywords] | 10x | 1.7% | 1.5-2% | ✓/⚠️ |

**Utilization:** [X]% (target: 85%+)
```

**iOS:**
```markdown
**[X]/100 chars** | **Issues:** [X]

| Keyword | Issue | Action |
|---------|-------|--------|
| [word] | [problem] | Remove/Keep |

## Option 1: Safe ([X]/100)
[keywords,here]

## Option 2: Aggressive ([X]/100)
[keywords,here]
```

---

### Full Analysis Output (Detail Level: Full)

Use the detailed formats below.

---

### Google Play Report (Full)

```markdown
# GOOGLE PLAY - ASO Analysis

**App:** [Name] | **Length:** [X]/4000 ([X]%) | **Status:** GOOD / NEEDS WORK

---

## Keywords

**IMPORTANT:** Always run the scraper to get real data:
```bash
python aso_scraper.py "keyword1,keyword2" --platform gplay --app-id [APP_ID]
```

| Keyword | Rank | Count | Score | Top Suggestions | Issue | Action |
|---------|------|-------|-------|-----------------|-------|--------|
| conference league | #1 | 3x | 100 | conference league, conference league app | ✓ | OK |
| UEFA | #5 | 3x | 90 | uefa champions league, uefa, uefa tv | ✓ | OK |
| football | — | 2x | 100 | football games, football live | ✓ | **+5x** |
| soccer | — | 1x | 100 | soccer, soccer games, soccer star | ✓ | **+4x** |
| live scores | — | 0x | 100 | live scores, live scores football | ✓ | **ADD** |

**Understanding the data:**
- **Rank** = Your app's position in Google Play search results — REAL DATA
- **Count** = How many times keyword appears in your description
- **Score** = Popularity from autocomplete (100=exact match, lower=less popular) — REAL DATA
- **Top Suggestions** = What users see when typing this keyword — REAL DATA
- **Issue** = ✓ means relevant, ⚠️ explains the problem

---

## Add These

| Keyword | Search Interest | Example Usage |
|---------|-----------------|---------------|
| live scores | HIGH | "Check live scores and results" |
| results | HIGH | "scores, results, and standings" |
| sports | HIGH | "the best sports app" |

---

## First 167 Characters

**Current:** "[First 167 chars]..."

**Better:** "[Improved version with high-value keywords]..."

---

## Optimized Description

```
[Full rewritten description - ready to copy/paste]
```

---

## Keyword Utilization (Optimized)

| Keyword | Priority | Count | Density | Target | Status |
|---------|----------|-------|---------|--------|--------|
| football | Primary | 15x | 2.5% | 2-3% | ✓ Optimal |
| scores | Primary | 14x | 2.3% | 2-3% | ✓ Optimal |
| live | Primary | 12x | 2.0% | 2-3% | ✓ Optimal |
| match | Secondary | 10x | 1.7% | 1.5-2% | ✓ Good |
| results | Secondary | 9x | 1.5% | 1.5-2% | ✓ Good |
| standings | Secondary | 8x | 1.3% | 1.5-2% | ⚠️ Below target |
| ... | ... | ... | ... | ... | ... |
| **Total unique** | — | **20+** | — | — | — |
| **Utilization** | — | — | — | **85%+** | ✓/⚠️ |

**Density guide:** <1% = too low | 1-2% = below optimal | **2-3% = optimal** | >5% = stuffing

---

## What Changed

| Change | Before | After | Why |
|--------|--------|-------|-----|
| Added "live scores" | 0x | 3x | HIGH search interest, was missing |
| Added "sports" | 0x | 2x | HIGH search interest, was missing |
| Increased "football" | 2x | 8x | Too low for main keyword |
| Increased "soccer" | 1x | 4x | Too low |
| Added section headers | No | Yes | Improves readability + keyword density |
| Length | 37% | 72% | Was underutilized |
```

---

### iOS Report (Full)

```markdown
# iOS APP STORE - Keyword Field Analysis

**App:** [App Name]
**ID:** [123456789]

---

## Overview

| Metric | Value | Target |
|--------|-------|--------|
| Characters Used | [X]/100 | 95-100 |
| Keywords | [X] | Maximize |
| Branded Found | [X] | 0 |

---

## Keyword Performance

**IMPORTANT:** Always run the scraper to get real data:
```bash
python aso_scraper.py "keyword1,keyword2" --platform ios --app-id [APP_ID]
```

| Keyword | Rank | Score | Top Suggestions | Issue | Action |
|---------|------|-------|-----------------|-------|--------|
| [word] | #1 | 95 | soccer, soccer stars, soccer games | ✓ | Keep |
| [word] | #12 | 95 | champions league, champions | ✓ | Keep |
| [word] | — | 70 | drawing apps, drawing games | ⚠️ triggers art apps | Remove |
| [word] | — | 70 | goal tracker, goal battle | ⚠️ triggers productivity | Remove |
| [word] | — | 95 | sofascore, sofascore live | ⚠️ competitor app | Remove |
| [word] | — | 20 | (none) | ⚠️ no search volume | Remove |

**Understanding the data:**
- **Rank** = Your app's position in search results (from iTunes Search API) — REAL DATA
- **Score** = Popularity from autocomplete API (95=exact match found, 70=related, 20=none) — REAL DATA
- **Top Suggestions** = What users actually see when typing this keyword — REAL DATA
- **Issue** = ✓ means relevant to your app, ⚠️ explains the problem

---

## Issues Found

### Branded Keywords

| Keyword | Type | Risk |
|---------|------|------|
| [keyword] | Competitor App | HIGH |
| [keyword] | Platform Brand | HIGH |

### Other Issues

| Keyword | Issue | Action |
|---------|-------|--------|
| [keyword] | In app name (redundant) | Remove |
| [keyword] | Space after comma | Fix format |
| [keyword] | Low popularity | Replace |

---

## Suggested Replacements

| Add This | Popularity | Chars | Replaces |
|----------|------------|-------|----------|
| [word] | 85/100 | [X] | [old word] |
| [word] | 78/100 | [X] | [old word] |

---

## Optimized Keywords

### Option 1: Safe (Recommended)

```
[keyword,keyword,keyword,keyword,keyword]
```

| Metric | Value |
|--------|-------|
| Characters | [X]/100 |
| Keywords | [X] |
| Remaining | [X] chars |

**Changes:**
- Removed: [keyword] (branded), [keyword] (low pop.)
- Added: [keyword] (pop: 85), [keyword] (pop: 78)

---

### Option 2: Aggressive

```
[keyword,keyword,keyword,keyword,keyword]
```

| Metric | Value |
|--------|-------|
| Characters | [X]/100 |
| Keywords | [X] |
| Remaining | [X] chars |

**Risk keywords kept:**
- [keyword] — Competitor name (may cause rejection)
- [keyword] — Platform brand (may cause rejection)

---

## Summary Comparison

| Version | Chars | Keywords | High Pop. | Branded |
|---------|-------|----------|-----------|---------|
| Original | [X] | [X] | [X] | [X] |
| Safe | [X] | [X] | [X] | 0 |
| Aggressive | [X] | [X] | [X] | [X] |

---

## Data Sources

| Column | Source | Type |
|--------|--------|------|
| Rank | iTunes Search API | REAL |
| Score | iOS Autocomplete API | REAL |
| Top Suggestions | iOS Autocomplete API | REAL |

**All data is real** — fetched directly from Apple's APIs via the scraper. No estimates.
```

---

## Platform Rules

### iOS App Store

| Field | Limit |
|-------|-------|
| Title | 30 chars |
| Subtitle | 30 chars |
| Keywords | 100 chars |

**Rules:**
- Commas count toward 100 char limit
- No spaces after commas
- Don't repeat words from app name (already indexed)
- No plurals (Apple indexes both forms)
- Single words perform better than phrases
- Avoid competitor names and trademarks

### Google Play Store

| Field | Limit |
|-------|-------|
| Title | 30 chars |
| Short description | 80 chars |
| Full description | 4000 chars |

**Rules:**
- Keywords in title carry most weight
- First 167 chars visible in search results
- Repeat important keywords 3-5x naturally
- Use bullet points for readability

---

## Reference

### Stopwords (Filter from analysis)

**English:** a, an, the, and, or, but, is, are, was, were, be, been, have, has, had, do, does, did, will, would, could, should, may, might, must, can, for, with, at, by, from, into, to, of, in, on, off, over, under, then, here, there, when, where, how, all, each, more, most, other, some, no, not, only, so, than, too, very, just, also, now, your, our, their, this, that, these, those, what, which, who

**Generic app terms:** app, application, download, free, new, best, top, great, amazing, awesome, perfect, excellent, wonderful, fantastic, today, fun, world

**Keep these:** track, sync, share, save, manage, edit, create, organize, search, filter, export, backup, secure, fast, easy, pro

### Trademark Flags

**Identify competitor trademarks by:**
1. WebSearch "[app category] popular apps" to find top competitors
2. Flag any competitor app names or brand terms
3. Flag platform trademarks (Google, Apple, Microsoft, Meta, etc.)

| Type | How to Identify | Action |
|------|-----------------|--------|
| Competitor apps | Top apps in same category | Remove (Safe) |
| Platform brands | Google, Apple, Microsoft, Amazon, Meta | Remove (Safe) |
| Third-party brands | Payment processors, social platforms | Remove (Safe) |
| Category leaders | Research via WebSearch | Flag for review |

**Context rule:** Only use keywords directly relevant to your app's actual features.

### ASO Scraper Tool (Recommended)

For real-time data from both app stores, use the included Python scraper:

**One-time setup:**
```bash
pip install selenium webdriver-manager
npm install google-play-scraper
```

**Usage:**
```bash
# Google Play - analyze keywords
python aso_scraper.py "soccer,football,scores" --platform gplay

# Google Play - with app ranking lookup
python aso_scraper.py "soccer,football" --platform gplay --app-id com.sofascore.app

# iOS App Store - analyze keywords
python aso_scraper.py "soccer,football" --platform ios --country US

# iOS - with app ranking lookup
python aso_scraper.py "soccer,football" --platform ios --app-id 1176147574
```

**Output:** JSON with real data - popularity scores, autocomplete suggestions, and app rankings.

**Requirements:**
- Python 3.x
- Node.js (for Google Play suggestions via google-play-scraper)
- Chrome browser (for Google Play rankings)
- curl (for iOS - no browser needed)

---

### Free Keyword Data Sources (Manual)

**iOS App Store Autocomplete (Direct API):**
```bash
curl -s "https://search.itunes.apple.com/WebObjects/MZSearchHints.woa/wa/hints?clientApplication=Software&term=[keyword]" -H "X-Apple-Store-Front: 143441-1,29"
```
- Returns XML with suggestions ordered by popularity
- Position in list indicates relative search volume
- No authentication required

**Google Play (via aso library):**

One-time setup:
```bash
npm install aso google-play-scraper
```

Get keyword scores:
```bash
node -e "require('aso')('gplay').scores('[keyword]').then(r=>console.log(JSON.stringify(r,null,2)))"
```

Get keyword suggestions:
```bash
node -e "require('aso')('gplay').suggest({strategy:'SEARCH',keywords:['[keyword]'],num:20}).then(r=>console.log(JSON.stringify(r,null,2)))"
```

**Score Interpretation (Google Play):**
| Score | Difficulty | Traffic |
|-------|------------|---------|
| 0-3 | Easy to rank | Low volume |
| 4-6 | Moderate | Medium volume |
| 7-10 | Very hard | High volume |

**Rate Limiting:**
- iOS API: Generally reliable, but add 1s delay between requests if batching
- Google Play library: Makes many HTTP requests per keyword, batch 5-10 at a time

**Sources:**
- [facundoolano/aso](https://github.com/facundoolano/aso) - Google Play scores
- [facundoolano/app-store-scraper](https://github.com/facundoolano/app-store-scraper) - iOS data
