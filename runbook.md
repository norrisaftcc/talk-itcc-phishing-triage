# Runbook: Triage a Reported Phishing Email

Use this checklist when a user reports a suspicious email. You do not need to write code.
Follow the steps in order. Write down what you find at each step in the ticket.

**Before you start:** Do not click links. Do not open attachments. Do not reply to the sender.

1. **Open a ticket.** Record who reported the email, when, and how (button, forward, phone call).
2. **Ask the user one question:** "Did you click a link, open an attachment, or enter a password?" If yes, go to step 11 now, then come back.
3. **Get the original email as a file.** Ask the user to use the "Report phishing" button or to forward it *as an attachment* (.eml). A normal forward removes the headers you need.
   - **Gmail (web):** Open the email. Select **More** (three dots, next to Reply). Select **Show original** to see the headers. On that page, **Download original** saves an .eml file. [VERIFY]
   - **Outlook on the web:** Open the email. Select **...** (More actions) > **View** > **View message details** to see the headers. Outlook may save a message as .msg, not .eml. The script reads only .eml. [VERIFY]
   - If you cannot get an .eml file, copy the headers from these windows and read steps 5–7 by hand.
4. **Run the header report.** In Codespaces, run:
   `python3 scripts/parse_headers.py path/to/email.eml`
   Save the output in the ticket.
   No Codespaces? Open `TEST-OUTPUT.md` to see an example report.
5. **Check sender alignment.** Compare From, Reply-To, and Return-Path. Different domains are a warning sign, not proof.
6. **Check authentication.** Look at SPF, DKIM, and DMARC. A "fail" is a strong warning sign. "Pass" does not prove the email is safe. Attackers can pass checks on domains they own.
7. **Check the links.** Look at every domain in the report. Look for look-alike spelling (for example, `paypa1` with the number 1). Note any link where the visible text and the real link do not match.
8. **Read the message for pressure.** Look for urgency, threats, requests for passwords or payment, and a generic greeting.
9. **Optional: ask an AI to explain the report.** Use `prompts/explain-headers.md`. Paste only the script report. Never paste real user data, passwords, or full internal emails into a public AI tool. Before you paste, cut query strings from URLs (the part after `?`, which can hold the user's email address) and cut internal names. Check your employer's AI policy first. Check what the AI says against steps 5–8. The AI can be wrong.
10. **Decide.** Mark the email as *phishing*, *spam*, *legitimate*, or *unsure*. If unsure, escalate. Do not guess.
11. **Contain, if the user clicked or entered a password.** Follow your organization's policy. This usually means: reset the password, end active sessions, check MFA, and escalate to security.
12. **Close the loop.** Tell the user the result and thank them for reporting. Record the decision and the evidence in the ticket. Send it to the security team if your policy says so.

*Teaching material. Your organization's policy always comes first.*
