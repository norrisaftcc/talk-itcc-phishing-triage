#!/usr/bin/env python3
"""Print a short triage report for one .eml file. Teaching tool, standard library only.
Usage:  python3 scripts/parse_headers.py samples/fake-phish.eml
"""
import argparse
import email
import re
from email import policy
from html.parser import HTMLParser
from urllib.parse import urlparse

# A simple pattern for web links. It is not perfect, but it is easy to read.
URL_PATTERN = re.compile(r"https?://[^\s\"'<>)]+")


def domain_of(address_or_url):
    """Return the domain part of an email address or a URL, in lower case."""
    if not address_or_url:
        return ""
    if "://" in address_or_url:
        return (urlparse(address_or_url).hostname or "").lower()
    # Email address: take the part after the "@".
    match = re.search(r"@([\w.-]+)", address_or_url)
    return match.group(1).lower() if match else ""


class LinkFinder(HTMLParser):
    """Collect (visible text, href) pairs from <a> tags in an HTML body."""

    def __init__(self):
        super().__init__()
        self.links = []      # list of [text, href]
        self._href = None    # href of the <a> tag we are inside, if any

    def handle_starttag(self, tag, attrs):
        if tag == "a":
            self._href = dict(attrs).get("href", "")
            self.links.append(["", self._href])

    def handle_data(self, data):
        if self._href is not None:
            self.links[-1][0] += data.strip()

    def handle_endtag(self, tag):
        if tag == "a":
            self._href = None


def check_auth(auth_results):
    """Find spf=, dkim=, and dmarc= results in the Authentication-Results header."""
    found = {}
    for name in ("spf", "dkim", "dmarc"):
        match = re.search(name + r"=(\w+)", auth_results, re.IGNORECASE)
        found[name.upper()] = match.group(1).lower() if match else "not present"
    return found


def main():
    parser = argparse.ArgumentParser(description="Triage report for one .eml file.")
    parser.add_argument("eml_file", help="path to a saved email (.eml)")
    args = parser.parse_args()

    # Read the file in binary mode. The email module decodes it for us.
    with open(args.eml_file, "rb") as handle:
        msg = email.message_from_binary_file(handle, policy=policy.default)

    red_flags = []
    print("=== Phishing triage report:", args.eml_file, "===\n")

    # 1. The basic headers.
    for name in ("From", "Reply-To", "Return-Path", "Subject", "Date"):
        print(f"{name + ':':<13} {msg.get(name, '(missing)')}")

    # 2. Authentication results (SPF, DKIM, DMARC).
    auth = " ".join(str(v) for v in msg.get_all("Authentication-Results", []))
    print("\nAuthentication-Results:")
    if not auth:
        print("  (header not present - cannot check SPF/DKIM/DMARC)")
    for name, result in check_auth(auth).items():
        if auth:
            print(f"  {name:<6} {result}")
        if result in ("fail", "softfail", "permerror"):
            red_flags.append(f"{name} result is '{result}'.")

    # 3. Compare the From domain with the Reply-To domain.
    from_domain = domain_of(str(msg.get("From", "")))
    reply_domain = domain_of(str(msg.get("Reply-To", "")))
    if reply_domain and reply_domain != from_domain:
        red_flags.append(f"Reply-To domain ({reply_domain}) differs from From domain ({from_domain}).")

    # 4. Read every text part of the body. Collect URLs and HTML links.
    urls, html_links = [], []
    for part in msg.walk():
        if part.get_content_type() in ("text/plain", "text/html"):
            text = part.get_content()
            urls.extend(URL_PATTERN.findall(text))
            if part.get_content_type() == "text/html":
                finder = LinkFinder()
                finder.feed(text)
                html_links.extend(finder.links)

    print("\nURLs found in body:")
    unique_urls = list(dict.fromkeys(urls))  # remove duplicates, keep order
    if not unique_urls:
        print("  (none)")
    for url in unique_urls:
        print(f"  {url}\n      domain: {domain_of(url)}")

    # 5. Link text that looks like a web address but points somewhere else.
    for text, href in html_links:
        if "." not in text or " " in text:
            continue  # the visible text is not a web address, so skip it
        if "://" not in text:
            text = "http://" + text  # add a scheme so urlparse can read it
        shown, real = domain_of(text), domain_of(href)
        if real and shown != real:
            red_flags.append(f"Link text shows '{shown}' but the link goes to '{real}'.")

    print("\nRed flags:")
    if not red_flags:
        print("  (none found by this script - this does NOT prove the email is safe)")
    for flag in red_flags:
        print("  [!]", flag)


if __name__ == "__main__":
    main()
