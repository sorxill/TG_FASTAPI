from fastapi import FastAPI, Request

from insults.insult import router as router_insult
from quotes.quote import router as router_quote

app = FastAPI(
    title="FAST_API_TG_BOT",
)

app.include_router(router_insult)
app.include_router(router_quote)


@app.get("/")
def helo_world():
    return {
        "answer": "Hello World!",
    }


@app.post("/hook")
async def handle_webhook(request: Request):
    data = await request.json()
    return data
