lock:
    uv pip compile pyproject.toml -o pylock.toml

sync:
    uv pip sync --preview-features pylock pylock.toml

format:
    uvx ruff format

lint:
    uvx ruff check --fix
    uvx ty check

run:
    uv run main.py
