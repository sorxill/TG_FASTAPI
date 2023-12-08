import requests
from fastapi import APIRouter, HTTPException

router = APIRouter(
    prefix="/quote",
    tags=["Quotes"],
)


@router.get("/")
def get_quote_of_the_day():
    try:
        request_quote = requests.get("https://favqs.com/api/qotd").json()
        ans = {
            "tags": f"{request_quote['quote']['tags']}",
            "author": f"{request_quote['quote']['author']}",
            "body": f"{request_quote['quote']['body']}",
        }

        return ans

    except Exception:
        raise HTTPException(
            status_code=500,
            detail={
                "status": "error",
                "data": None,
                "details": None,
                "description": "Problem in the process of solving",
            },
        )
