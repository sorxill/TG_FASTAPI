import requests
from fastapi import APIRouter

from insults.lang import languages

router = APIRouter(
    prefix="/insult",
    tags=["EvilInsults"],
)


@router.get("/{language}")
def get_evil(language: str):
    if language in languages:
        ans = requests.get(
            f"https://evilinsult.com/generate_insult.php?lang={language}&type=json"
        ).json()
        return ans["insult"]
    else:
        return {"error": "Invalid language"}
