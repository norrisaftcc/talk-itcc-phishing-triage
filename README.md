# Phishing Triage Kit

A small teaching kit for triaging reported phishing emails.

**This is a teaching kit, not a production tool.** Use it to learn the steps.
At work, follow your organization's tools and policy.

## Who it is for

Help desk staff and Tier 1 SOC analysts. Both roles handle phishing reports from users.
You do not need to be a programmer. You need to run one command.

## What is in the kit

| File | What it does |
|---|---|
| `runbook.md` | A step-by-step checklist for a person. Start here. |
| `scripts/parse_headers.py` | Reads one saved email (.eml). Prints the key headers, SPF/DKIM/DMARC results, all URLs, and simple red flags. |
| `prompts/explain-headers.md` | A prompt you paste into an AI assistant with the script report. The AI explains the headers in plain English. |
| `samples/fake-phish.eml` | A made-up phishing email. |
| `samples/fake-legit.eml` | A made-up normal email, for contrast. |
| `.gitignore` | Stops git from tracking real emails (`real/`), secrets (`*.env`), and Outlook exports (`*.pst`, `*.msg`). |
| `TEST-OUTPUT.md` | The real output of the script on both samples. |

All sample emails use reserved example domains (`example.com`, `example.net`, `example.org`).
They do not name real people or real companies.

## How to run it in GitHub Codespaces (browser only)

You do not need to install anything on your computer.

1. Open this repository on GitHub.
2. Select the green **Code** button. Select the **Codespaces** tab. Select **Create codespace on main**.
3. Wait for the editor to open in your browser. A terminal opens at the bottom.
4. In the terminal, type:
   ```
   python3 scripts/parse_headers.py samples/fake-phish.eml
   ```
5. Compare with the normal email:
   ```
   python3 scripts/parse_headers.py samples/fake-legit.eml
   ```
6. Open `runbook.md` and walk through the steps with the report.

Codespaces has Python 3 already. The script uses only the Python standard library.
Note: free Codespaces hours are limited each month. Stop the codespace when you finish.

## How it was tested

- Ran the script on both sample emails with Python 3.13 on Linux.
- Checked by hand that each value in the report matches the .eml file.
- Checked that the phishing sample shows four red flags: SPF fail, DMARC fail,
  Reply-To domain mismatch, and link text / link target mismatch.
- Checked that the legitimate sample shows no red flags.
- The exact output is in `TEST-OUTPUT.md`.

Not tested: real-world emails, attachments, non-English emails, encoded or shortened URLs,
and emails with many Authentication-Results headers from different servers.

## Limits

- The script checks only a few simple signs. "No red flags" does **not** mean the email is safe.
- It reads the first `spf=`, `dkim=`, and `dmarc=` values it finds. Real emails can have
  several Authentication-Results headers. Only trust the one added by your own mail server.
- The URL pattern is simple. It can miss links or include extra characters.
- It does not open attachments, follow links, or check reputation lists.
- **The AI can be wrong about headers.** It can misread a value or state a guess as fact.
  Always check what it says against the report and the runbook.

## AI use

- **Tool:** An AI coding assistant (Claude) helped build this kit.
- **What it produced:** First drafts of the script, the sample emails, the runbook, the prompt, and this README.
- **What a human checked:** The presenter must review every file before the talk.
  Check that the script output matches the samples, that the runbook steps match good
  practice at your workplace, and that no sample uses a real domain or brand.
  <!-- Presenter: replace this line with who reviewed it and when. -->

## Privacy rule

Never commit real user emails. Put them in `real/` on your own machine only.
Git ignores that folder. Run `git status` to confirm.
