# GitLab Setup Guide for FontScan

## Step 1: Install Git (if not already installed)

1. Download Git for Windows from: https://git-scm.com/download/win
2. Run the installer and follow the setup wizard
3. Restart your terminal/PowerShell after installation

## Step 2: Create a GitLab Repository

1. Go to https://gitlab.com (or your GitLab instance)
2. Click "New Project" or "Create Project"
3. Choose "Create blank project"
4. Enter project name: `FontScan` (or your preferred name)
5. Set visibility (Private/Public) as needed
6. **DO NOT** initialize with README, .gitignore, or license (we already have these)
7. Click "Create project"

## Step 3: Initialize Git and Push to GitLab

After Git is installed, open PowerShell in your project directory and run these commands:

### Initialize Git Repository
```bash
git init
```

### Configure Git (if not already done)
```bash
git config --global user.name "Your Name"
git config --global user.email "your.email@example.com"
```

### Add all files
```bash
git add .
```

### Create initial commit
```bash
git commit -m "Initial commit: FontScan - AI-powered font recognition system with modern UI"
```

### Add GitLab remote (replace with your GitLab URL)
```bash
git remote add origin https://gitlab.com/your-username/FontScan.git
```

Or if using SSH:
```bash
git remote add origin git@gitlab.com:your-username/FontScan.git
```

### Push to GitLab
```bash
git branch -M main
git push -u origin main
```

## Alternative: Using GitLab CLI

If you prefer, you can also use GitLab CLI:
```bash
# Install GitLab CLI (glab)
# Then run:
glab repo create FontScan --public
git init
git add .
git commit -m "Initial commit"
git push -u origin main
```

## Troubleshooting

### If you get authentication errors:
- For HTTPS: Use a Personal Access Token instead of password
  - Go to GitLab → Settings → Access Tokens
  - Create token with `write_repository` scope
  - Use token as password when prompted

### If you get "remote origin already exists":
```bash
git remote remove origin
git remote add origin YOUR_GITLAB_URL
```

## Files Being Ignored

The following files/folders are excluded from Git:
- `__pycache__/` - Python cache files
- `model/*.h5` - Model files (too large)
- `static/uploads/*` - User uploaded images
- `*.pyc` - Compiled Python files
- Virtual environment folders

---

**Note:** Make sure to replace `your-username` and `FontScan` with your actual GitLab username and repository name.

