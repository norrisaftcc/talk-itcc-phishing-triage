# Presenter Steps: Set Up the Template and the Demo Pull Request

Do these steps **before the talk**. Allow 20 minutes. The pull request must exist before you go on stage.

## 1. Create the repository from this folder

1. On GitHub, select **+ > New repository**. Name it, for example `phishing-triage-kit`. Make it **Public**. Do not add a README, `.gitignore`, or license (this folder has them).
2. In a terminal in this folder, run:
   ```
   git remote add origin https://github.com/<your-account>/phishing-triage-kit.git
   git push -u origin main
   ```
3. Run `git status`. Confirm that `real/` does not appear. Open the repository on GitHub. Confirm that `real/` is not there.

## 2. Mark it as a template

1. In the repository, select **Settings**.
2. Under **General**, check **Template repository**.
3. Confirm that the repository page now shows **Use this template**.

## 3. Push the branch `improve-prompt`

1. Run:
   ```
   git push origin improve-prompt
   ```
2. Check the change: `git diff main improve-prompt`. It must show only the change to `prompts/explain-headers.md`.

## 4. Sign in with a second account

1. Open a private browser window.
2. Sign in to a second GitHub account that you made to play a classmate. Use a different email address. Turn on two-factor authentication for it.
3. From your main account, add the second account as a collaborator (**Settings > Collaborators > Add people**). Accept the invitation from the second account.

## 5. Open the pull request from the branch

1. In the private window (second account), open the repository.
2. Select **Pull requests > New pull request**. Set **base** to `main` and **compare** to `improve-prompt`.
3. Title: `Prompt: forbid advice to click links or open attachments`.
4. In the description, write what changed, why, and how you tested it. Use the "Version history" rules in `prompts/explain-headers.md`.
5. Select **Create pull request**. Do **not** merge it. You merge it live in the talk.
6. Note: GitHub shows the commit author from git ("Demo Student"), not the second account. The pull request itself shows the second account as the person who opened it.

## 6. In the talk, say this aloud

"I made a second GitHub account to play a classmate. That account opened this pull request. In a real team, a different person opens it."

## Fallback

If the network fails, show `git log --oneline --all --graph` and `git diff main improve-prompt` in a local terminal.
