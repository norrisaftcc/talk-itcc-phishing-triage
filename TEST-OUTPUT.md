# Test Output

Real output of `scripts/parse_headers.py`, captured on 2026-10-23 with Python 3.13.17 on Linux.
Result: **PASS**. Each value was checked by reading the .eml file against the output.

## Test 1: `samples/fake-phish.eml`

Expected: SPF fail, DMARC fail, Reply-To mismatch, link text/target mismatch (4 red flags).

Command: `python3 scripts/parse_headers.py samples/fake-phish.eml`

```text
=== Phishing triage report: samples/fake-phish.eml ===

From:         Account Security Team <security@paypa1-secure.example.net>
Reply-To:     Support Desk <verify-desk@example.org>
Return-Path:  <bounce-7731@mailer.example.org>
Subject:      URGENT: Your account will be suspended in 24 hours
Date:         Tue, 20 Oct 2026 08:13:55 -0400

Authentication-Results:
  SPF    fail
  DKIM   none
  DMARC  fail

URLs found in body:
  http://login.paypa1-secure.example.net/verify?id=88421
      domain: login.paypa1-secure.example.net

Red flags:
  [!] SPF result is 'fail'.
  [!] DMARC result is 'fail'.
  [!] Reply-To domain (example.org) differs from From domain (paypa1-secure.example.net).
  [!] Link text shows 'www.example.com' but the link goes to 'login.paypa1-secure.example.net'.
```

## Test 2: `samples/fake-legit.eml`

Expected: SPF/DKIM/DMARC pass, no red flags.

Command: `python3 scripts/parse_headers.py samples/fake-legit.eml`

```text
=== Phishing triage report: samples/fake-legit.eml ===

From:         IT Help Desk <it-helpdesk@example.com>
Reply-To:     (missing)
Return-Path:  <it-helpdesk@example.com>
Subject:      Lab maintenance on Friday
Date:         Wed, 21 Oct 2026 10:02:05 -0400

Authentication-Results:
  SPF    pass
  DKIM   pass
  DMARC  pass

URLs found in body:
  https://www.example.com/it/lab-schedule
      domain: www.example.com

Red flags:
  (none found by this script - this does NOT prove the email is safe)
```

## Other checks

- A file with no headers (`real/sample-from-user.eml`) prints `(missing)` for each header and does not crash.
- Running the script with no file name prints a usage message and exits with code 2.
