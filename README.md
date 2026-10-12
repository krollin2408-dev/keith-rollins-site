# keithrrollins.com

Portfolio of Keith Rollins, marketing strategist and communications leader.

## Update the site

1. Edit content in `src/content.py` (or styles in `src/assets/site.css`).
2. Run `python3 src/build.py`.
3. Commit and push. GitHub Pages republishes `docs/` within a minute or two.

## Publish (when ready)

1. In the repo, go to **Settings → Pages**.
2. Under "Build and deployment," choose **Deploy from a branch**, then **main** and **/docs**. Save.
3. Under "Custom domain," enter `keithrrollins.com` and save.
4. At your domain registrar, point the apex domain to GitHub's four A records (185.199.108.153, 185.199.109.153, 185.199.110.153, 185.199.111.153) and add a `www` CNAME to `krollin2408-dev.github.io`.
5. Turn on **Enforce HTTPS** once it becomes available.
