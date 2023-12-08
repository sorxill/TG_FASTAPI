from fastapi import FastAPI

from insults.insult import router as router_insult
from quotes.quote import router as router_quote

app = FastAPI(
    title="FAST_API_TG_BOT",
)

app.include_router(router_insult)
app.include_router(router_quote)
