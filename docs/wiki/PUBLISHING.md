# Publishing to the GitHub Wiki tab

The documentation source is version-controlled in `docs/wiki/`. The actual GitHub Wiki is a separate Git repository and is populated by [Publish Safety Edition Wiki](../../.github/workflows/publish-wiki.yml).

## One-time setup

1. Ensure the repository's **Wiki** feature is enabled and a **Home** page exists (already shown in the GitHub Wiki tab).
2. Create a GitHub personal access token with permission to write this repository's Wiki. GitHub fine-grained token Wiki support may vary; a classic token with `repo` scope is an alternative for private repositories, or `public_repo` for public repositories, subject to account policy. Use the least privilege that works.
3. In the main repository, open **Settings → Secrets and variables → Actions → New repository secret**.
4. Create the secret **`WIKI_PUSH_TOKEN`** and paste the token. Never commit or share it in chat.
5. Open **Actions → Publish Safety Edition Wiki → Run workflow**. Confirm the workflow succeeded.
6. Visit [the Wiki tab](https://github.com/TomcoGame/Open-MABEL-Safety-Edition/wiki) to check Home, sidebar, guide pages, and images.

After setup, changes to the source guides and images on `main` trigger a wiki sync automatically. The workflow updates managed Markdown pages; it does not delete unrelated existing Wiki pages.

## Design limitations

GitHub's Markdown sanitizer and SVG proxy may prevent animation from playing inline. Animated SVG source and static fallback remain linked. For a fully interactive browser training experience, a separate documentation site is more reliable.

The Wiki is a **published learning interface**, while hazard registers, requirements, architecture records and verification evidence stay authoritative in the main repository.
