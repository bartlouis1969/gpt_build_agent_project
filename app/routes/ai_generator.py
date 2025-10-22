"""
app/routes/ai_generator.py

FastAPI endpoint voor AI-content generatie.
"""

from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()


class AIGenerateRequest(BaseModel):
    prompt: str
    model: str | None = None
    temperature: float | None = None
    max_tokens: int | None = None


class AIGenerateResponse(BaseModel):
    content: str


@router.post("/ai/generate", response_model=AIGenerateResponse)
def generate_ai_content(request: AIGenerateRequest):
    # Import here to avoid circular import if needed
    from core.ai.generator import generate_content

    try:
        content = generate_content(
            prompt=request.prompt,
            model=request.model,
            temperature=request.temperature,
            max_tokens=request.max_tokens,
        )
        return AIGenerateResponse(content=content)
    except Exception as e:
        return AIGenerateResponse(content=f"Error: {str(e)}")
