# Perlas Arnold GitHub Pages Blog

This repository contains a GitHub Pages-compatible Jekyll site that publishes weekly security digest reports at `https://www.perlasarnold.me/blog/`.

## Structure

- `/blog/` is the main landing page for weekly digest posts
- `/_posts/` contains the generated Markdown posts that Jekyll publishes
- `/blog/digest-archive/` exposes the raw generated digest files
- `/archive/` lists the published weekly digests

## Weekly Digest Automation

- Workflow: `.github/workflows/build-digest.yml`
- Generator: `tools/security_digest/build_digest.ps1`
- Generated posts: `/_posts/`
- Generated raw archive: `/blog-digest/`

Run the workflow manually from GitHub Actions or let the weekly schedule publish new digest posts automatically.

## GitHub Pages

This repo is already configured for the custom domain `https://www.perlasarnold.me` through the `CNAME` file and Jekyll config.
