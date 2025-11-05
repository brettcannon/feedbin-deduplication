lock:
    uv pip compile pyproject.toml -o pylock.toml

sync:
    uv pip sync --preview-features pylock pylock.toml

format:
    uvx ruff format

lint:
    uvx ruff check --fix
    uvx pyrefly check

run:
    uv run main.py

cloudflare-dev:
    uv run --group cloudflare pywrangler dev

cloudflare-deploy:
    uv run --group cloudflare pywrangler deploy

cloudflare-set-secrets:
    uv run --group cloudflare pywrangler secret put FEEDBIN_USERNAME
    uv run --group cloudflare pywrangler secret put FEEDBIN_PASSWORD

cloudflare-cron-trigger:
    curl "http://127.0.0.1:8787/cdn-cgi/handler/scheduled"
