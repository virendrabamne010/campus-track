# 🚀 DEPLOYMENT – GitHub + Streamlit Community Cloud

CampusTrack needs **no secrets, no database and no paid services**, so deployment takes about 5 minutes and is completely free.

---

## Step 1 – Create a GitHub Repository

1. Go to <https://github.com> and log in.
2. Click the **+** icon (top-right) → **New repository**.
3. Repository name: `campus-track` (any name works).
4. Keep it **Public** (required for the free Streamlit Cloud tier).
5. Do **NOT** tick "Add a README" (we already have one).
6. Click **Create repository**.

## Step 2 – Push the Project to GitHub

Open a terminal **inside the project folder** and run:

```bash
git init
git add .
git commit -m "CampusTrack mini project - first release"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/campus-track.git
git push -u origin main
```

> Replace `YOUR_USERNAME` with your GitHub username. Enter your GitHub token/password when asked.

✅ The `.gitignore` already excludes `venv/`, `__pycache__/` and `streamlit_log.txt` junk, so only the needed files are uploaded.

## Step 3 – Connect GitHub with Streamlit Community Cloud

1. Go to <https://share.streamlit.io>.
2. Click **Continue with GitHub** and authorise Streamlit.

## Step 4 – Select Repository

1. Click **Create app** (top-right) → **Deploy a public app from GitHub**.
2. In "Repository", choose `YOUR_USERNAME/campus-track` from the dropdown.

## Step 5 – Select Branch

- Branch: `main`

## Step 6 – Select the Main File

- Main file path: `app.py`

## Step 7 – Deploy

1. (Optional) Change the App URL, e.g. `campustrack`.
2. Click **Deploy!**
3. Wait 2–3 minutes while Streamlit installs `requirements.txt` and boots the app.

## Step 8 – Copy Your Live URL

Your app is now live at:

```
https://YOURAPPNAME.streamlit.app
```

Share this link in your report/viva. Every future `git push` to `main` automatically redeploys the app.

---

## 🔧 Troubleshooting

| Problem | Fix |
|---|---|
| App crashes on start | Check the logs; make sure `requirements.txt` has streamlit, pandas, matplotlib |
| ModuleNotFoundError: modules | Ensure `modules/__init__.py` was pushed to GitHub |
| FileNotFoundError: data | Ensure the `data/` folder and all 4 CSV files were pushed |
| Old version showing | Click **Reboot app** from the app menu (bottom-right) |

---

## ✅ Pre-Deployment Checklist

- [x] Root `app.py` exists
- [x] `requirements.txt` with only needed packages
- [x] Relative paths only (`os.path.join("data", ...)`)
- [x] No secrets, no API keys, no local Windows paths in code
- [x] `.gitignore` excludes venv and caches
- [x] Tested locally with `streamlit run app.py`
