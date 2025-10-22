"""
core/ai/generator.py

GPT-gestuurde content generator voor trading headlines en strategieën.
"""

import os
import openai


def generate_content(prompt, model=None, temperature=None, max_tokens=None):
    """
    Genereer content met GPT op basis van een prompt.
    :param prompt: De input prompt (str)
    :param model: Modelnaam (optioneel)
    :param temperature: Creativiteit (optioneel)
    :param max_tokens: Max tokens (optioneel)
    :return: gegenereerde tekst (str)
    """
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise RuntimeError("OPENAI_API_KEY ontbreekt.")
    client = openai.OpenAI(api_key=api_key)
    response = client.chat.completions.create(
        model=model or os.getenv("MODEL_NAME", "gpt-4"),
        messages=[{"role": "user", "content": prompt}],
        temperature=temperature or float(os.getenv("DEFAULT_TEMPERATURE", "0.7")),
        max_tokens=max_tokens or int(os.getenv("MAX_TOKENS", "100")),
    )
    return response.choices[0].message.content
