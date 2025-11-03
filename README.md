# Feedbin deduplication
Deduplicate unread entries from your [Feedbin](https://feedbin.com) account using the [Feedbin API](https://github.com/feedbin/feedbin-api).

# Usage
To run, set the `FEEDBIN_USERNAME` and `FEEDBIN_PASSWORD` environment variables and call the [just](https://just.systems) recipe (notice their is a leading space and it is **IMPORTANT**; it causes your shell to **not** save the command, and thus your Feedbin password, to your history):

```shell
 FEEDBIN_USERNAME="" FEEDBIN_PASSWORD="" just run
```

# Development
See the [justfile](https://just.systems) for relevant recipes which require [uv](https://docs.astral.sh/uv/) to be installed.
