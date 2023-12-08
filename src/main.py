from fastapi import FastAPI

from insults.insult import router as router_insult

app = FastAPI(
    title="FAST API_TG BOT",
)

app.include_router(router_insult)
