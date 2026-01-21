# ASO Expert Guide

Comprehensive reference for App Store Optimization. This guide provides deep context for keyword analysis and optimization recommendations.

---

## 1. iOS App Store Deep Dive

### How Apple's Algorithm Works

Apple uses a **keyword matching system**, not full-text search:

| Field | Indexed? | Weight | Char Limit |
|-------|----------|--------|------------|
| App Name (Title) | Yes | Highest | 30 |
| Subtitle | Yes | High | 30 |
| Keyword Field | Yes | High | 100 |
| In-App Purchases | Yes | Low | 30 each |
| Developer Name | Yes | Low | — |
| Description | **No** | None | 4000 |

**Key insight:** The description is NOT indexed by Apple. It's purely for conversion (convincing users to download), not discovery.

### Character Limit Strategy

With 100 characters for keywords:
- Average keyword: 6 chars
- Commas needed: ~15-20
- **Realistic capacity: 15-20 keywords**

**Maximize by:**
- Using single words, not phrases ("live" + "scores" beats "live scores")
- No spaces after commas
- Shortest synonyms ("stats" not "statistics")

### Why Single Words Beat Phrases

Apple combines keywords automatically:
- Keywords: `live,scores,football`
- User searches: "live scores", "football scores", "live football"
- All match! One set of keywords covers multiple search phrases.

**Exception:** Compound words that only make sense together:
- "fantasy" + "football" = covered
- "premier" + "league" = better as separate (covers "premier", "league", "premier league")

### Pluralization Rules

Apple indexes **both singular and plural** automatically:
- "score" also matches "scores"
- "game" also matches "games"

**Never waste characters on plurals.** Use singular form only.

### Keyword Cannibalization

Words in your **App Name** and **Subtitle** are already indexed. Repeating them in the keyword field wastes characters.

**Example:**
- App Name: "UEFA Conference League"
- Don't include: "uefa", "conference", "league" in keyword field
- These are already indexed from the title

### Localization Opportunities

Each locale gets its own:
- Title (30 chars)
- Subtitle (30 chars)
- Keywords (100 chars)

**Strategy:**
- US English: Primary keywords
- UK English: Alternative spellings + UK-specific terms
- Australia/Canada: Additional keyword variations
- Other languages: Translate + add local sports terms

A single app can effectively have 500+ indexed keywords across locales.

### Update Frequency Impact

Apple gives a **temporary ranking boost** after updates:
- New version = fresh crawl
- Algorithm re-evaluates keywords
- Visibility spike for 24-72 hours

**Recommendation:** Update keywords with each app release, even minor ones.

---

## 2. Google Play Deep Dive

### How Google's Algorithm Differs

Google uses **full-text NLP analysis**, similar to web search:

| Field | Indexed? | Weight |
|-------|----------|--------|
| App Title | Yes | Highest |
| Short Description | Yes | Very High |
| Full Description | Yes | High |
| Developer Name | Yes | Medium |
| Reviews | Yes | Low-Medium |
| In-App Content | Partial | Low |

**Key insight:** Everything is indexed, including user reviews. Google's algorithm understands context, synonyms, and semantic meaning.

### Keyword Density Sweet Spots

| Density | Assessment |
|---------|------------|
| Under 1% | Too low — add more |
| 1-2% | Acceptable |
| **2-3%** | **Optimal** |
| 3-4% | Acceptable |
| Over 5% | Stuffing risk — reduce |

**Example:** 4000 char description ≈ 600 words
- 2% density = keyword appears ~12 times
- 3% density = keyword appears ~18 times

### Position Weighting

Where keywords appear matters:

| Position | Weight | Recommendation |
|----------|--------|----------------|
| Title (first 30 chars) | 5x | Primary keyword MUST be here |
| Short Description (80 chars) | 4x | 2-3 primary keywords |
| First 167 chars of description | 3x | This is visible in search results |
| Rest of description | 1x | Natural keyword distribution |

### Why 4000 Characters Should Be Maximized

**Underutilization = missed opportunity:**

| Utilization | Assessment |
|-------------|------------|
| Under 50% (2000 chars) | Severely underutilized |
| 50-70% | Underutilized |
| 70-90% | Good |
| 90-100% | Optimal |

More content = more keyword opportunities = more search matches.

**How to expand naturally:**
- Detailed feature explanations
- Use cases and scenarios
- Supported devices/regions
- Recent updates and improvements
- FAQ-style content

### Backlinks and External Factors

Google considers external signals:
- Links to your Play Store listing
- Social media mentions
- Press coverage
- App embeds on websites

These don't directly boost rankings but increase "authority signals."

### Review Keywords

**Google indexes review text.** Users mentioning features in reviews can boost your ranking for those terms.

**Strategy:**
- Prompt satisfied users to leave reviews
- Reply to reviews using relevant keywords
- Features mentioned in reviews become indexed terms

---

## 3. Keyword Research Methodology

### Finding Seed Keywords

**Source 1: Autocomplete Mining**
```
Type partial keyword → record suggestions → repeat
```
Autocomplete = real user searches, ordered by popularity.

**Source 2: Competitor Analysis**
- Identify top 10 apps in your category
- Extract their titles, subtitles, descriptions
- Find keywords they all use = category essentials
- Find keywords only leaders use = opportunities

**Source 3: User Language**
- Read your reviews and competitor reviews
- How do users describe features?
- What problems do they mention solving?
- Mirror their vocabulary

### Evaluating Keyword Value

**Formula:** `Value = (Volume × Relevance) ÷ Difficulty`

| Factor | How to Assess |
|--------|---------------|
| Volume | Autocomplete position, third-party tools |
| Relevance | Does your app actually deliver this? |
| Difficulty | How many quality apps rank for it? |

**High-value keywords:**
- Appear in autocomplete (some search volume)
- Directly match your app's features
- Top results aren't all massive apps

### Long-Tail Strategy

**Short-tail:** "soccer" — Very high volume, very high competition
**Long-tail:** "soccer live scores free" — Lower volume, much easier to rank

**When to use long-tail:**
- New apps with no ranking history
- Niche features not served by leaders
- Specific use cases

**Long-tail compounds from single words:**
- Keywords: `soccer,live,scores,free,alerts`
- Covers: "soccer", "live scores", "free soccer scores", "soccer alerts", etc.

### Seasonal Keywords

**Sports examples:**
- August-May: "premier league", "champions league"
- June-July: "world cup", "euros", "copa america"
- January: "transfer news", "winter transfers"
- Fantasy seasons: "fantasy draft", "fpl"

**Strategy:**
- Core keywords stay permanent
- Rotate 2-3 keywords seasonally
- Update 2-4 weeks before season starts

### Category-Specific Patterns

**Sports apps:**
- Live/scores/results/standings/fixtures/stats
- League names (premier, champions, bundesliga)
- Action words (watch, track, follow)

**Games:**
- Gameplay descriptors (puzzle, strategy, action)
- "Free", "offline", "no wifi"
- Comparison terms ("like [popular game]")

**Productivity:**
- Problem words (organize, manage, track)
- Benefit words (easy, fast, simple)
- Integration terms (sync, cloud, share)

---

## 4. Branded Keywords Risk Analysis

### Apple's Trademark Enforcement

Apple actively rejects apps using trademarked keywords:

**Rejection triggers:**
- Competitor app names (SofaScore, FotMob, ESPN)
- Platform brands (Apple, Google, Facebook)
- Game/media franchises (FIFA, NFL, NBA)
- Company names (Microsoft, Amazon, Meta)

**Consequences:**
- App rejected during review
- Existing app pulled from store
- Developer account warning

### Google's Approach

Google is **more lenient** but legal risks remain:
- No automated trademark rejection
- Trademark owners can file complaints
- Google may remove apps after complaints
- Repeat offenses affect developer standing

### When Competitor Keywords ARE Acceptable

**Legitimate uses:**
- Comparison features: "Import from [Competitor]"
- Integration: "Sync with [Platform]"
- Compatibility: "Works with [Device/Service]"
- Generic terms that happen to be brand names

**Example:**
- "excel" (generic spreadsheet term) = borderline acceptable
- "Microsoft Excel" = clear trademark violation

### Safe Alternatives to Branded Terms

| Instead of | Use |
|------------|-----|
| FIFA | football, soccer, world cup |
| ESPN | sports, scores, news |
| SofaScore | live scores, statistics |
| FotMob | match alerts, football scores |
| Premier League | english football, EPL |

**Strategy:** Target what users search for, not specific app names.

---

## 5. Advanced Optimization

### A/B Testing (Google Play Experiments)

Google Play Console offers built-in A/B testing:
- Test different icons
- Test different screenshots
- Test different short descriptions
- Test different feature graphics

**What to test first:** Icon > Screenshots > Short description

**Sample size:** Need 1000+ impressions per variant for statistical significance.

### Conversion Rate Factors

**Impression → Page View → Install**

| Factor | Impact on Conversion |
|--------|---------------------|
| Icon | Highest — first thing users see |
| Rating | Very High — social proof |
| Screenshots | High — shows actual app |
| Short description | Medium — quick value prop |
| Reviews | Medium — detailed social proof |
| Description | Lower — most users don't read |

**Benchmark conversion rates:**
- Excellent: 40%+
- Good: 25-40%
- Average: 15-25%
- Poor: Under 15%

### The Reviews/Ratings Flywheel

Higher ratings → Better conversion → More downloads → More reviews → Higher ratings

**How to start the flywheel:**
- In-app review prompts (after positive moments)
- Respond to all negative reviews
- Fix issues mentioned in 1-2 star reviews
- Don't ask for ratings during onboarding

### Localization ROI

**High ROI markets for English apps:**
1. United States (primary)
2. United Kingdom
3. Canada
4. Australia
5. India (English-speaking segment)

**Language localization priority:**
1. Spanish (400M+ speakers)
2. Portuguese (Brazil)
3. German
4. French
5. Japanese

**Minimum localization:** Translate title, subtitle/short description, screenshots text.

### Update Cadence Recommendations

| Scenario | Update Frequency |
|----------|------------------|
| New app, building rankings | Every 2-4 weeks |
| Established app, stable rankings | Every 4-8 weeks |
| Seasonal app | Before each season |
| Post-major algorithm change | Within 1-2 weeks |

Each update = opportunity to refresh keywords and get ranking boost.

---

## 6. Common Mistakes (Anti-Patterns)

### Keyword Stuffing

**Wrong:**
```
Soccer live scores soccer football soccer match soccer standings soccer fixtures soccer statistics soccer news soccer alerts
```

**Right:**
```
Follow your favorite teams with live scores, match alerts, and detailed statistics. Check standings and upcoming fixtures across all major leagues.
```

Google's NLP detects unnatural repetition and may penalize rankings.

### Generic Words That Waste Space

**iOS keyword field wasters:**
- "app" (users know it's an app)
- "free" (shown in price anyway)
- "best" (unverifiable claim)
- "2024", "2025" (dates expire)
- "new" (subjective, temporary)

**Better use of space:** Specific feature keywords.

### Chasing Volume Over Relevance

**Mistake:** Targeting "games" because it has high volume.
**Problem:** Your live scores app won't rank and won't convert.

**Rule:** Only target keywords your app genuinely serves.

### Ignoring Autocomplete Context

**Mistake:** Using "draw" for football draw results.
**Reality:** Autocomplete shows "drawing apps", "draw games".

**Always check:** What does autocomplete suggest for this keyword?

### Set-and-Forget Mentality

ASO is **ongoing**, not one-time:
- Competitor keywords change
- User search behavior evolves
- Seasonal trends shift
- Algorithm updates occur

**Minimum:** Review keywords quarterly.
**Ideal:** Review with each app update.

---

## 7. Metrics & Success Measurement

### Impression Share Tracking

**App Store Connect / Google Play Console metrics:**
- Impressions: How often your app appears in search
- Product page views: How often users click through
- Conversion rate: Views → Installs

**Track keyword-level impressions** to see which keywords drive visibility.

### Conversion Rate Benchmarks by Category

| Category | Average CR | Good CR |
|----------|------------|---------|
| Games | 25-35% | 40%+ |
| Social | 20-30% | 35%+ |
| Utilities | 15-25% | 30%+ |
| Sports | 20-30% | 35%+ |
| News | 15-25% | 30%+ |

If your CR is below category average, focus on conversion (icon, screenshots) before keywords.

### Keyword Ranking Monitoring

**Frequency:**
- Critical keywords: Daily
- Secondary keywords: Weekly
- Long-tail keywords: Monthly

**What to track:**
- Rank position
- Rank trend (up/down/stable)
- Competitor movements

### When to Iterate vs. Hold Steady

**Iterate (change keywords) when:**
- Ranked keywords aren't driving installs
- New seasonal opportunity
- Competitor moved into your position
- Algorithm update affected rankings

**Hold steady when:**
- Rankings are improving (give it 2-4 weeks)
- Good conversion rate on current keywords
- No external changes in market

---

## Quick Reference Tables

### iOS Character Budget

| Field | Limit | Typical Keywords |
|-------|-------|------------------|
| Title | 30 | 1-2 (brand + primary) |
| Subtitle | 30 | 2-3 |
| Keywords | 100 | 15-20 |
| **Total** | **160** | **18-25** |

### Google Play Character Budget

| Field | Limit | Typical Keywords |
|-------|-------|------------------|
| Title | 30 | 1-2 |
| Short Description | 80 | 3-5 |
| Full Description | 4000 | 20-30 unique |
| **Total** | **4110** | **24-37** |

### Keyword Quality Scorecard

| Criteria | Score |
|----------|-------|
| Appears in autocomplete | +2 |
| Exact match in suggestions | +1 |
| Top suggestion shows relevant apps | +2 |
| Top suggestion shows irrelevant apps | -2 |
| Is competitor/trademark | -3 |
| No autocomplete suggestions | -1 |

**Target: Keywords scoring 3+ only**

---

## Sources & Further Reading

- [Apple App Store Guidelines](https://developer.apple.com/app-store/review/guidelines/)
- [Google Play Policy Center](https://play.google.com/about/developer-content-policy/)
- [Appfigures ASO Resources](https://appfigures.com/resources/)
- [facundoolano/aso](https://github.com/facundoolano/aso) - Google Play data library
- [iTunes Search API](https://developer.apple.com/library/archive/documentation/AudioVideo/Conceptual/iTuneSearchAPI/)
