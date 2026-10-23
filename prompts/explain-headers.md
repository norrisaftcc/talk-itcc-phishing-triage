# Prompt: Explain a Phishing Triage Report

**How to use:** Copy everything inside the box below. Paste it into an AI assistant.
Replace the last line with the output of `scripts/parse_headers.py`.

**Safety rule:** Paste only the script report. Do not paste real names, passwords,
or full internal emails into a public AI tool.

---

```text
You are helping a beginner help-desk technician triage a reported phishing email.
Below is a short report made by a script. It shows email headers, authentication
results, the URLs in the body, and red flags the script found.

Please do these four things:

1. Explain each header in the report in plain English. Use one or two short
   sentences per header. Say what the header is for and what this value shows.
2. List the red flags you see. For each one, say why it matters.
   Include red flags the script did not list, if you see any.
3. Give your overall view: likely phishing, likely legitimate, or unsure.
   Give your reasons.
4. Say clearly what you are unsure of. Say what you cannot know from this
   report alone (for example, the full Received chain or the attachment contents).

Rules:
- Use short sentences. Do not use jargon without explaining it.
- Do not invent header values that are not in the report.
- If a field says "missing" or "not present", say what that means. Do not guess a value.

REPORT:
<paste the script output here>
```

---

## Version history

Changes to this prompt go through pull requests. Do not edit it directly on `main`.
Each pull request must say what changed, why, and how you tested it
(which sample emails you ran, and what the AI answered before and after).
This lets the team review prompt changes the same way they review code changes.

| Version | Change |
|---|---|
| 1.0 | First version. |
