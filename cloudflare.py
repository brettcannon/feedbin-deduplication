import workers

import main


class Default(workers.WorkerEntrypoint):
    async def scheduled(self, _controller, _env, _ctx):
        # Run `uv run --group cloudflare pywrangler secret put` to set the secrets.
        username = self.env.FEEDBIN_USERNAME
        password = self.env.FEEDBIN_PASSWORD

        await main.main(username, password)
