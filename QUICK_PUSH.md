# Quick Push to GitLab - FontScan

## Your GitLab Repository URL:
**https://gitlab.com/vivek871/FontScan.git**

## Step 1: Install Git (Required First Step)

1. Download Git for Windows: https://git-scm.com/download/win
2. Run the installer (use default settings)
3. **IMPORTANT:** After installation, close and reopen PowerShell/Command Prompt

## Step 2: Run These Commands

Open PowerShell in this folder and run:

```powershell
# Initialize Git
git init

# Add all files
git add .

# Create commit
git commit -m "Initial commit: FontScan - AI-powered font recognition system with modern UI"

# Add your GitLab repository
git remote add origin https://gitlab.com/vivek871/FontScan.git

# Set main branch
git branch -M main

# Push to GitLab
git push -u origin main
```

## Authentication

When you run `git push`, you'll be prompted for credentials:

- **Username:** vivek871
- **Password:** Use a **Personal Access Token (NOT your GitLab password)**
  - Go to: https://gitlab.com/-/user_settings/personal_access_tokens
  - Create token with name "FontScan" and scope: `write_repository`
  - Copy the token and use it as the password

## Alternative: Use the Automated Script

After installing Git, just run:
```powershell
.\push-to-gitlab.ps1
```
Then paste: `https://gitlab.com/vivek871/FontScan.git`

---

**Note:** Git must be installed first before any of these commands will work!

