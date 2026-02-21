# GitHub Repository Setup Guide

This guide helps you set up this project on GitHub with all the necessary configurations.

## Step 1: Create a New Repository

1. Go to [GitHub](https://github.com) and sign in
2. Click the **"+"** icon → **"New repository"**
3. Fill in the details:
   - **Repository name:** `devex-sample-service` (or your preferred name)
   - **Description:** "DevEx showcase: Flask API with CI/CD, testing, and AI-powered documentation"
   - **Visibility:** Public or Private
   - **DON'T** initialize with README (we already have one)

4. Click **"Create repository"**

## Step 2: Push Your Code

```bash
# Initialize git (if not already done)
cd /Users/rootaccess/Documents/DevEx
git init

# Add all files
git add .

# Make initial commit
git commit -m "feat: initial DevEx sample service implementation

- Add Flask REST API with health check and products endpoints
- Implement Docker containerization
- Add comprehensive testing with pytest
- Configure linting (flake8, pylint, black)
- Add GitHub Actions CI/CD pipeline
- Implement security scanning
- Add dependency health checks
- Implement AI-powered documentation generation
- Add Makefile for developer commands"

# Add your GitHub repository as remote
git remote add origin https://github.com/YOUR_USERNAME/devex-sample-service.git

# Push to GitHub
git branch -M main
git push -u origin main
```

## Step 3: Configure Repository Secrets

For AI documentation generation, add your OpenAI API key:

1. Go to your repository on GitHub
2. Click **Settings** → **Secrets and variables** → **Actions**
3. Click **"New repository secret"**
4. Add:
   - **Name:** `OPENAI_API_KEY`
   - **Secret:** Your OpenAI API key (get it from https://platform.openai.com/api-keys)
5. Click **"Add secret"**

> **Note:** This is optional. The AI doc generator will work in mock mode without an API key.

## Step 4: Enable GitHub Actions

1. Go to the **Actions** tab
2. GitHub will detect the workflow file
3. Click **"I understand my workflows, go ahead and enable them"**

## Step 5: Verify CI Pipeline

1. Make a small change (e.g., update README.md)
2. Create a new branch:
   ```bash
   git checkout -b test/verify-ci
   git add .
   git commit -m "docs: test CI pipeline"
   git push origin test/verify-ci
   ```
3. Create a Pull Request on GitHub
4. Watch the CI pipeline run!

## Step 6: Configure Branch Protection (Optional)

For production-ready setup:

1. Go to **Settings** → **Branches**
2. Click **"Add branch protection rule"**
3. Branch name pattern: `main`
4. Enable:
   - ✅ Require a pull request before merging
   - ✅ Require status checks to pass
   - ✅ Require branches to be up to date
   - Select checks: `lint`, `test`, `security-scan`, `secret-scan`
5. Save changes

## Step 7: Add Repository Topics

Make your repo discoverable:

1. Go to your repository home page
2. Click the ⚙️ icon next to "About"
3. Add topics:
   - `devex`
   - `developer-experience`
   - `flask`
   - `python`
   - `ci-cd`
   - `docker`
   - `github-actions`
   - `automation`
   - `ai-documentation`
4. Save changes

## Step 8: Update README Badges

Replace `YOUR_USERNAME` in README.md with your GitHub username:

```bash
# In README.md, update:
[![CI Pipeline](https://github.com/YOUR_USERNAME/devex-sample/actions/workflows/ci.yml/badge.svg)]

# To:
[![CI Pipeline](https://github.com/your-actual-username/devex-sample-service/actions/workflows/ci.yml/badge.svg)]
```

## Verification Checklist

Before submitting your repository, verify:

- ✅ All files are committed and pushed
- ✅ CI pipeline runs successfully
- ✅ README badges work correctly
- ✅ Repository secrets configured (if using AI features)
- ✅ Branch protection enabled (optional)
- ✅ Repository topics added
- ✅ Description is clear and informative

## Submitting Your Work

Once everything is set up:

1. Copy your repository URL:
   ```
   https://github.com/YOUR_USERNAME/devex-sample-service
   ```

2. Ensure the repository is **public** (or give access to reviewers)

3. Share the URL as instructed in the assignment

## Tips for a Great Submission

1. **Clean Git History**
   - Use meaningful commit messages
   - Follow conventional commits
   - Avoid "WIP" or "test" commits

2. **Documentation**
   - Ensure README is comprehensive
   - Run `make docs` to generate SDD
   - Add any additional context in docs/

3. **Working CI**
   - Verify all CI checks pass
   - Fix any failing tests or linters
   - Check security scans

4. **Professional Touches**
   - Add a nice repository description
   - Include relevant topics/tags
   - Make sure .gitignore is complete

## Troubleshooting

### "CI workflow not running"
- Check Actions tab is enabled
- Verify `.github/workflows/ci.yml` exists
- Check workflow syntax with: `yamllint .github/workflows/ci.yml`

### "Tests failing in CI but passing locally"
- Ensure all dependencies in requirements.txt
- Check Python version matches (3.11)
- Review CI logs for specific errors

### "Security scan failing"
- Review Bandit and Safety output
- Update vulnerable dependencies
- Add exceptions if false positives

---

Good luck with your submission! 🚀
