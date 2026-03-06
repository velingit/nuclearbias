# Quick Start Guide - Deploy to GitHub Pages

This guide will help you deploy your Jekyll site to GitHub Pages in 5 minutes.

## Prerequisites

- Git installed on your system
- A GitHub account (free)
- This folder ready to push

## Step 1: Update Configuration

Edit `_config.yml` and replace these placeholders:

```yaml
baseurl: "/energy-analysis"  # Change to your repository name
url: "https://yourusername.github.io"  # Change yourusername to your GitHub username
repository: "yourusername/energy-analysis"  # Change yourusername and repo name
github_username: yourusername

author:
  name: Your Name  # Your actual name
  email: your.email@example.com  # Your email
```

## Step 2: Create GitHub Repository

1. Go to [github.com/new](https://github.com/new)
2. **Repository name**: `energy-analysis` (or your preferred name)
3. **Description**: "European Energy Analysis - Nuclear vs Price"
4. Select **Public** (required for free GitHub Pages)
5. Click **Create repository**

## Step 3: Initialize Git & Push

Open PowerShell/Command Prompt in the `jekyll_site` folder and run:

```bash
# Initialize git repository
git init

# Add all files
git add .

# Create initial commit
git commit -m "Initial commit: European nuclear energy analysis"

# Add remote repository (replace yourusername and repo-name)
git remote add origin https://github.com/yourusername/energy-analysis.git

# Push to GitHub (replace main with master if needed)
git push -u origin main
```

**Note**: You may be prompted for GitHub credentials. Use:
- **Username**: Your GitHub username
- **Password**: Your personal access token (Settings → Developer settings → Personal access tokens)
  - Or simply your GitHub password for HTTPS auth

## Step 4: Enable GitHub Pages

1. Go to your repository on GitHub: `https://github.com/yourusername/energy-analysis`
2. Click **Settings** (top right)
3. Click **Pages** (left sidebar)
4. Under "Source", select **Deploy from a branch**
5. Select **main** branch and **root** folder
6. Click **Save**

## Step 5: Access Your Site

Your site will be live at:
```
https://yourusername.github.io/energy-analysis/
```

**Note**: It may take 1-2 minutes to publish. Refresh the page if you don't see it immediately.

## Troubleshooting

### "git push" fails with authentication error
- Use a personal access token instead of password
- Go to GitHub → Settings → Developer settings → Personal access tokens
- Generate new token with `public_repo` permission
- Use token as password when pushing

### Site shows 404 error
- Check `baseurl` in `_config.yml` matches your repository name
- Ensure GitHub Pages is enabled in repository settings
- Wait 2-3 minutes for GitHub to rebuild the site

### Pages doesn't appear
- Check "Actions" tab in your GitHub repository for build errors
- Verify all Markdown files have YAML frontmatter (lines between `---`)
- Check image paths use `/assets/images/` format

## Local Development (Optional)

Test your site locally before pushing:

```bash
# Install dependencies (first time only, requires Ruby)
bundle install

# Start local server
bundle exec jekyll serve

# View at http://localhost:4000
```

## After Deployment

- Your site is live and accessible
- Any changes pushed to GitHub automatically deploy
- The site rebuilds within a few minutes of each push

## Need Help?

See the main `README.md` for project details, or check GitHub Pages documentation:
https://docs.github.com/en/pages

---

**Happy deploying!** 🚀
