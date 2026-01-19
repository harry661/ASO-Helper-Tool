---
name: aso-helper
description: Optimize app store keywords for iOS App Store and Google Play Store. Use when researching keywords, analyzing keyword performance, generating keyword suggestions, or optimizing app metadata for ASO. Triggers on mentions of ASO, app store optimization, keywords, app listing, app metadata, store ranking, analyze description, keyword frequency, extract keywords, optimize existing description, iOS keyword field, 100 character limit, or trademark check.
---

# ASO Helper

Keyword research, analysis, and optimization for iOS App Store and Google Play Store.

## Quick Start

**Analyze Google Play Description:**
```
Platform: Google Play
Category: [e.g., Sports, Games, Productivity]
Description:
---
[Paste full description here]
---
```

**Analyze iOS Keyword Field:**
```
App: [App Name]
Category: [e.g., Sports, Games, Productivity]
Keywords: [comma,separated,keywords,no,spaces]
```

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
| Under 1% | Too low | Add more instances |
| 2-3% | Optimal | Maintain |
| Over 5% | Keyword stuffing risk | Reduce |

**Currency Check:**
- Use today's date to determine current year
- Flag any year before current year as outdated (e.g., if current year is 2027, flag "2026", "25-26")
- Recommend updates: past year → current year, past season → current/next season
- WebSearch for upcoming major events in current and next year

**Quality Checklist:**
| Criteria | Target |
|----------|--------|
| Primary keyword in title | Yes |
| Keywords in first 167 chars | 3-5 unique |
| Unique relevant keywords | 10+ |
| Optimal density keywords | 5+ at 2-3% |
| Year references current | Yes (no past seasons) |

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
2. **Keywords to emphasize** - Currently under 2%, increase to 3-5 occurrences
3. **Keywords to reduce** - Currently over 5%, reduce to 2-3%

**Provide before/after metrics:**
| Metric | Before | After |
|--------|--------|-------|
| Total words | [X] | [X] |
| Unique keywords | [X] | [X] |
| Keywords at optimal density | [X] | [X] |
| Keywords in first 167 chars | [X] | [X] |

**Provide optimized description:**
- Full rewritten text with changes applied
- Highlight key changes in recommendations summary

---

## iOS Keyword Field Analysis

### Phase 1: Analyze Field

1. **Count characters** (commas count toward 100 limit)
   - Example: `Photo,Editor` = 5 + 1 + 6 = 12 chars
2. Count keywords
3. Flag issues:
   - Spaces after commas (waste)
   - Words in app name (redundant)
   - Trademark/competitor terms

### Phase 2: Assess Each Keyword

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
- Maximize 100 chars

**Option 2: Aggressive (User's Risk)**
- Keep competitor/trademark keywords
- Maximum visibility, risk of rejection

---

## Output Formats

### Google Play Report

```markdown
## Google Play Description Analysis

### Summary
- Total words: [X]
- Meaningful words: [X] (after stopword filter)
- Unique keywords: [X]
- Description length: [X]/4000 chars

### Keyword Frequency Table
| Keyword | Count | Density | Position | Action |
|---------|-------|---------|----------|--------|
| [word] | [n] | [%] | Title/First 167/Body | Keep/Increase/Reduce |

### Quality Assessment
| Criteria | Status | Notes |
|----------|--------|-------|
| Primary keyword in title | Yes/No | [keyword if found] |
| Keywords in first 167 chars | [X] found | [list keywords] |
| Optimal density (2-3%) | [X] keywords | [list those outside range] |
| Keyword variety | [X] unique | Target: 10+ |
| Year references current | Yes/No | [list outdated years found → recommend current year] |

### Recommendations
**Add:** [keywords] - Place in [title/first 167/body]
**Emphasize:** [keywords] - Currently [X]x, target 3-5x
**Reduce:** [keywords] - Currently [X]%, target 2-3%

### Before/After Comparison
| Metric | Before | After |
|--------|--------|-------|
| Total words | [X] | [X] |
| Unique keywords | [X] | [X] |
| Keywords at optimal density | [X] | [X] |
| Keywords in first 167 | [X] | [X] |

### Changes Applied
| Location | Original | Optimized | Reason |
|----------|----------|-----------|--------|
| First 167 | [old text snippet] | [new text snippet] | Added [category-relevant keywords] |
| Body | [old text snippet] | [new text snippet] | Reduced [overused keyword] density |
| Body | [outdated year] | [current year from today's date] | Updated to current year |

### Optimized Description
[Full rewritten description with ALL changes applied - ready to copy/paste]
```

### iOS Report

```markdown
## iOS Keyword Field Analysis

### Character Count
- Keywords: [X] chars
- Commas: [X] chars
- **Total: [X]/100**

### Keyword Analysis
| Keyword | Chars | Relevance | Issue | Action |
|---------|-------|-----------|-------|--------|
| [word] | [n] | High/Med/Low | [issue or None] | Keep/Remove |

### Issues Found
- Trademarks: [list]
- Competitors: [list]
- Redundant: [list]

---

### Option 1: Safe (Recommended)
**Keywords** ([X]/100 chars):
```
[optimized,keywords,here]
```

**Removed:** [keyword] (reason)
**Added:** [keyword] (trending)

---

### Option 2: Aggressive
**Keywords** ([X]/100 chars):
```
[keywords,with,competitors]
```

**Risk keywords:** [list with warnings]

---

### Character Budget
| Version | Keywords | Commas | Total | Left |
|---------|----------|--------|-------|------|
| Safe | [X] | [X] | [X] | [X] |
| Aggressive | [X] | [X] | [X] | [X] |
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
