# Feedbin deduplication
Deduplicate unread entries from your [Feedbin](https://feedbin.com) account using the [Feedbin API](https://github.com/feedbin/feedbin-api).

# Usage
## CLI
To run, set the `FEEDBIN_USERNAME` and `FEEDBIN_PASSWORD` environment variables and call the [just](https://just.systems) recipe (notice their is a leading space and it is **IMPORTANT**; it causes your shell to **not** save the command, and thus your Feedbin password, to your history):

```shell
 FEEDBIN_USERNAME="<username>" FEEDBIN_PASSWORD="<password>" just run
```

## Cloudflare Workers
The repo contains support for deploying to [Cloudflare Workers](https://developers.cloudflare.com/workers/) (and should stay within the [free plan](https://developers.cloudflare.com/workers/platform/pricing/)).

[![Deploy to Cloudflare](https://deploy.workers.cloudflare.com/button)](https://deploy.workers.cloudflare.com/?url=https://github.com/brettcannon/feedbin-deduplication)

If you prefer to deploy via the command-line, follow these steps:

1. `just cloudflare-set-secrets` to set your Feedbin username and password (and create the Cloudflare worker if didn't already exist)
1. `just cloudflare-deploy`

# Development
See the [justfile](https://just.systems) for relevant recipes which require [uv](https://docs.astral.sh/uv/) to be installed.

## Cloudflare

1. Store your credential secrets in a `.env` file (you can copy `.env.example` to `.env` and then fill in the details)
2. Start a pywrangler dev server via `just cloudflare-dev`
3. Hit the cron trigger endpoint via `just cloudflare-cron-trigger`
