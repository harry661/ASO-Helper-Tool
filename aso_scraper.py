#!/usr/bin/env python3
"""
ASO Keyword Analyzer - Scrapes real keyword data from Google Play and iOS App Store.

Usage:
    python aso_scraper.py "soccer,football,scores" --platform gplay
    python aso_scraper.py "soccer,football" --platform gplay --app-id com.sofascore.app
    python aso_scraper.py "soccer,football" --platform ios --country US
"""

import argparse
import json
import subprocess
import re
import sys
import xml.etree.ElementTree as ET
from urllib.parse import quote

# Selenium imports (only loaded when needed for Google Play)
SELENIUM_AVAILABLE = False
try:
    from selenium import webdriver
    from selenium.webdriver.chrome.options import Options
    from selenium.webdriver.chrome.service import Service
    from selenium.webdriver.common.by import By
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC
    from webdriver_manager.chrome import ChromeDriverManager
    SELENIUM_AVAILABLE = True
except ImportError:
    pass


# ============================================================================
# Chrome Browser Setup (Google Play)
# ============================================================================

def get_browser():
    """Create optimized headless Chrome browser instance."""
    if not SELENIUM_AVAILABLE:
        raise ImportError(
            "Selenium not installed. Run: pip install selenium webdriver-manager"
        )

    opts = Options()
    opts.add_argument("--headless=new")  # New headless mode (Chrome 109+)
    opts.add_argument("--disable-gpu")
    opts.add_argument("--no-sandbox")
    opts.add_argument("--disable-dev-shm-usage")
    opts.add_argument("--disable-images")
    opts.add_argument("--blink-settings=imagesEnabled=false")
    opts.add_argument("--disable-extensions")
    opts.add_argument("--disable-infobars")
    opts.add_argument("--window-size=1920,1080")
    opts.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")
    opts.page_load_strategy = 'eager'  # Don't wait for full page load

    service = Service(ChromeDriverManager().install())
    return webdriver.Chrome(service=service, options=opts)


# ============================================================================
# Google Play Functions
# ============================================================================

def get_gplay_suggestions(browser, keyword, country="US"):
    """
    Get autocomplete suggestions from Google Play search.
    Returns list of suggestions with popularity scores.
    """
    url = f"https://play.google.com/store/search?q={quote(keyword)}&c=apps&hl=en&gl={country}"

    try:
        browser.get(url)

        # Wait for page to load (max 5 seconds)
        WebDriverWait(browser, 5).until(
            EC.presence_of_element_located((By.TAG_NAME, "body"))
        )

        suggestions = []

        # Try to get autocomplete suggestions from search input
        try:
            elements = browser.find_elements(By.CSS_SELECTOR, '[data-display-text]')
            for i, el in enumerate(elements[:10]):
                text = el.get_attribute('data-display-text')
                if text:
                    score = 100 - (i * 10)  # Position 1=100, 2=90, etc.
                    suggestions.append({"keyword": text, "score": score})
        except Exception:
            pass

        return suggestions

    except Exception as e:
        return []


def get_gplay_search_results(browser, keyword, country="US", limit=50):
    """
    Get search results from Google Play.
    Returns list of apps with their positions.
    """
    url = f"https://play.google.com/store/search?q={quote(keyword)}&c=apps&hl=en&gl={country}"

    try:
        browser.get(url)

        # Wait for results to load
        WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR, 'a[href*="/store/apps/details"]'))
        )

        # Scroll to load more results
        for _ in range(3):
            browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
            try:
                WebDriverWait(browser, 2).until(
                    lambda d: d.execute_script("return document.readyState") == "complete"
                )
            except Exception:
                pass

        # Extract app links
        results = []
        links = browser.find_elements(By.CSS_SELECTOR, 'a[href*="/store/apps/details"]')

        seen_ids = set()
        for link in links:
            href = link.get_attribute("href")
            if href and "id=" in href:
                # Extract app ID from URL
                match = re.search(r'id=([^&]+)', href)
                if match:
                    app_id = match.group(1)
                    if app_id not in seen_ids:
                        seen_ids.add(app_id)
                        results.append(app_id)
                        if len(results) >= limit:
                            break

        return results

    except Exception as e:
        return []


def get_gplay_rank(browser, keyword, app_id, country="US"):
    """
    Find app's ranking position for a keyword on Google Play.
    Returns position (1-indexed) or -1 if not found.
    """
    results = get_gplay_search_results(browser, keyword, country, limit=100)

    try:
        position = results.index(app_id) + 1
        return position
    except ValueError:
        return -1


def analyze_gplay(keywords, app_id=None, country="US"):
    """
    Analyze keywords on Google Play using Chrome scraping.
    """
    print(f"Starting Chrome browser for Google Play analysis...", file=sys.stderr)
    browser = get_browser()

    results = []
    try:
        for i, kw in enumerate(keywords):
            print(f"  [{i+1}/{len(keywords)}] Analyzing: {kw}", file=sys.stderr)

            data = {
                "keyword": kw,
                "platform": "gplay",
                "country": country,
                "suggestions": get_gplay_suggestions(browser, kw, country),
            }

            # Calculate popularity score based on if keyword appears in suggestions
            if data["suggestions"]:
                # If we got suggestions, keyword is popular
                data["score"] = 80
            else:
                data["score"] = 40  # Moderate if no suggestions returned

            # Get app ranking if app_id provided
            if app_id:
                rank = get_gplay_rank(browser, kw, app_id, country)
                data["rank"] = rank if rank > 0 else "Not ranked"

            results.append(data)

    finally:
        browser.quit()
        print("Chrome browser closed.", file=sys.stderr)

    return results


# ============================================================================
# iOS App Store Functions (curl-based, no browser needed)
# ============================================================================

def get_ios_autocomplete(keyword, country="us"):
    """
    Get autocomplete suggestions from iOS App Store.
    Uses Apple's hints API - no browser needed.
    """
    # Country code to storefront mapping
    storefronts = {
        "us": "143441-1,29",
        "gb": "143444-1,29",
        "uk": "143444-1,29",
        "ca": "143455-1,29",
        "au": "143460-1,29",
        "de": "143443-1,29",
        "fr": "143442-1,29",
    }

    storefront = storefronts.get(country.lower(), "143441-1,29")
    url = f'https://search.itunes.apple.com/WebObjects/MZSearchHints.woa/wa/hints?clientApplication=Software&term={quote(keyword)}'

    try:
        result = subprocess.run(
            ['curl', '-s', url, '-H', f'X-Apple-Store-Front: {storefront}'],
            capture_output=True, text=True, timeout=10
        )

        if result.returncode != 0:
            return []

        # Parse XML response
        suggestions = []
        try:
            root = ET.fromstring(result.stdout)
            # Find all string elements (suggestions)
            # Filter out URLs and metadata strings
            position = 0
            for elem in root.iter('string'):
                text = elem.text
                if text and not text.startswith('http') and text != 'Suggestions':
                    position += 1
                    score = 100 - ((position - 1) * 10)  # Position-based scoring
                    suggestions.append({"keyword": text, "score": max(score, 10)})
                    if len(suggestions) >= 10:
                        break
        except ET.ParseError:
            pass

        return suggestions

    except Exception:
        return []


def get_ios_search_results(keyword, country="us", limit=100):
    """
    Search iOS App Store and return app IDs in order.
    """
    url = f'https://itunes.apple.com/search?term={quote(keyword)}&country={country}&entity=software&limit={limit}'

    try:
        result = subprocess.run(
            ['curl', '-s', url],
            capture_output=True, text=True, timeout=15
        )

        if result.returncode != 0:
            return []

        data = json.loads(result.stdout)
        return [str(app['trackId']) for app in data.get('results', [])]

    except Exception:
        return []


def get_ios_rank(keyword, app_id, country="us"):
    """
    Find app's ranking position for a keyword on iOS App Store.
    """
    results = get_ios_search_results(keyword, country, limit=200)

    try:
        position = results.index(str(app_id)) + 1
        return position
    except ValueError:
        return -1


def analyze_ios(keywords, app_id=None, country="us"):
    """
    Analyze keywords on iOS App Store using curl (no browser).
    """
    print(f"Analyzing iOS App Store keywords...", file=sys.stderr)

    results = []
    for i, kw in enumerate(keywords):
        print(f"  [{i+1}/{len(keywords)}] Analyzing: {kw}", file=sys.stderr)

        suggestions = get_ios_autocomplete(kw, country)

        # Calculate popularity score
        if suggestions:
            # Check if exact keyword appears in suggestions
            exact_match = any(s['keyword'].lower() == kw.lower() for s in suggestions)
            if exact_match:
                score = 95
            else:
                score = 70  # Related suggestions exist
        else:
            score = 20  # No suggestions = low popularity

        data = {
            "keyword": kw,
            "platform": "ios",
            "country": country,
            "score": score,
            "suggestions": suggestions[:5],  # Limit to top 5 for cleaner output
        }

        # Get app ranking if app_id provided
        if app_id:
            rank = get_ios_rank(kw, app_id, country)
            data["rank"] = rank if rank > 0 else "Not ranked"

        results.append(data)

    return results


# ============================================================================
# Main Entry Point
# ============================================================================

def main():
    parser = argparse.ArgumentParser(
        description="ASO Keyword Analyzer - Get real keyword data from app stores",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python aso_scraper.py "soccer,football" --platform gplay
  python aso_scraper.py "soccer,football" --platform gplay --app-id com.sofascore.app
  python aso_scraper.py "soccer,football" --platform ios --country US --app-id 1176147574
        """
    )

    parser.add_argument(
        "keywords",
        help="Comma-separated list of keywords to analyze"
    )
    parser.add_argument(
        "--platform", "-p",
        choices=["gplay", "ios"],
        required=True,
        help="Platform to analyze: gplay (Google Play) or ios (App Store)"
    )
    parser.add_argument(
        "--app-id", "-a",
        help="Your app's ID to check ranking (optional)"
    )
    parser.add_argument(
        "--country", "-c",
        default="US",
        help="Country code (default: US)"
    )
    parser.add_argument(
        "--output", "-o",
        choices=["json", "table"],
        default="json",
        help="Output format (default: json)"
    )

    args = parser.parse_args()

    # Parse keywords
    keywords = [k.strip() for k in args.keywords.split(",") if k.strip()]

    if not keywords:
        print("Error: No keywords provided", file=sys.stderr)
        sys.exit(1)

    # Run analysis
    if args.platform == "gplay":
        if not SELENIUM_AVAILABLE:
            print("Error: Selenium not installed. Run: pip install selenium webdriver-manager", file=sys.stderr)
            sys.exit(1)
        results = analyze_gplay(keywords, args.app_id, args.country)
    else:
        results = analyze_ios(keywords, args.app_id, args.country.lower())

    # Output results
    if args.output == "json":
        print(json.dumps(results, indent=2))
    else:
        # Simple table output
        print("\nKeyword Analysis Results")
        print("=" * 60)
        for r in results:
            rank_str = f"#{r['rank']}" if r.get('rank') and r['rank'] != "Not ranked" else "Not ranked"
            print(f"  {r['keyword']:<20} Score: {r['score']}/100  Rank: {rank_str}")
        print("=" * 60)


if __name__ == "__main__":
    main()
