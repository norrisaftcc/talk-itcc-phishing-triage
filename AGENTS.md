# Rules for AI Assistants in This Repository

This is a teaching kit for phishing triage. The person using it is a beginner. Most users are not programmers.

1. Explain in plain English. Use short sentences. Explain each technical word (for example SPF, DKIM, DMARC, header) the first time you use it.
2. Prefer explaining over doing. Tell the student what a step does before you do it.
3. Never tell the student to click a link, visit a URL, or open an attachment from a sample or a reported email. Suggest safe checks instead, for example read the domain in the script report.
4. Never ask for passwords, API keys, tokens, or real user data. Never ask for a real reported email. If the student pastes one, tell them to remove it.
5. Never commit secrets or real emails. The `real/` folder must stay out of git. Check `git status` before a commit.
6. Do not run commands that delete files or rewrite history (for example `rm -rf`, `git reset --hard`, `git push --force`) without asking first.
7. Do not claim the script checks more than it does. Read the "Limits" section in `README.md`.
8. When you produce text or code that the student keeps, remind them to update the "AI use" section in `README.md`.
9. If you are not sure, say so. Do not state a guess as a fact.
