from fastapi import APIRouter
from pydantic import BaseModel

from core.ai.generator import generate_content

router = APIRouter()


class GenerateRequest(BaseModel):
    prompt: str
    model: str | None = None
    temperature: float | None = None
    max_tokens: int | None = None


@router.post("/generate")
def generate(req: GenerateRequest):
    """
    Minimal offline stub: returns a generated string from core.ai.generator.
    """
    text = generate_content(
        req.prompt,
        model=req.model,
        temperature=req.temperature,
        max_tokens=req.max_tokens,
    )
    return {"content": text}
