"""Deep research module for Anthropic, Perplexity, and Google APIs."""

import os
from typing import Optional, cast

import requests
from dotenv import load_dotenv

load_dotenv()

ANTHROPIC_API_KEY = os.environ.get("ANTHROPIC_API_KEY")
PERPLEXITY_API_KEY = os.environ.get("PERPLEXITY_API_KEY")
GOOGLE_API_KEY = os.environ.get("GOOGLE_API_KEY")


def query_anthropic(
    prompt: str, model: str = "claude-3-opus-20240229", max_tokens: int = 512
) -> Optional[str]:
    """Query the Anthropic Claude API (v1/messages endpoint)."""
    if not ANTHROPIC_API_KEY:
        raise ValueError("ANTHROPIC_API_KEY not set in environment.")
    url = "https://api.anthropic.com/v1/messages"
    headers = {
        "x-api-key": ANTHROPIC_API_KEY,
        "anthropic-version": "2023-06-01",
        "content-type": "application/json",
    }
    data = {
        "model": model,
        "max_tokens": max_tokens,
        "messages": [{"role": "user", "content": prompt}],
    }
    response = requests.post(url, headers=headers, json=data)
    response.raise_for_status()
    result = response.json().get("content")
    # Anthropic returns a list of message parts
    if isinstance(result, list) and result:
        return cast(Optional[str], result[0].get("text"))
    return None


def query_perplexity(
    prompt: str, model: str = "pplx-70b-online", max_tokens: int = 512
) -> Optional[str]:
    """Query the Perplexity API for a completion. NOTE: Public API may not be available for all users."""
    if not PERPLEXITY_API_KEY:
        raise ValueError("PERPLEXITY_API_KEY not set in environment.")
    url = "https://api.perplexity.ai/v1/complete"  # Update if you have a different endpoint
    headers = {
        "Authorization": f"Bearer {PERPLEXITY_API_KEY}",
        "Content-Type": "application/json",
    }
    data = {"prompt": prompt, "model": model, "max_tokens": max_tokens}
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 404:
        return "Perplexity public API not available. Check your access or endpoint."
    response.raise_for_status()
    choices = response.json().get("choices", [{}])
    result = choices[0].get("text") if choices else None
    return cast(Optional[str], result)


def query_google(
    prompt: str, model: str = "text-bison-001", max_tokens: int = 512
) -> Optional[str]:
    """Query the Google PaLM API for a completion (Vertex AI Generative Language API)."""
    if not GOOGLE_API_KEY:
        raise ValueError("GOOGLE_API_KEY not set in environment.")
    url = f"https://generativelanguage.googleapis.com/v1beta2/models/{model}:generateText?key={GOOGLE_API_KEY}"
    headers = {"Content-Type": "application/json"}
    data = {"prompt": {"text": prompt}, "maxOutputTokens": max_tokens}
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 403:
        return "Google API key forbidden or not enabled for Generative Language API."
    response.raise_for_status()
    candidates = response.json().get("candidates", [])
    result = candidates[0].get("output") if candidates else None
    return cast(Optional[str], result)


def deep_research(prompt: str) -> dict:
    """Perform deep research using Anthropic, Perplexity, and Google APIs."""
    results = {}
    try:
        results["anthropic"] = query_anthropic(prompt)
    except Exception as e:
        results["anthropic_error"] = str(e)
    try:
        results["perplexity"] = query_perplexity(prompt)
    except Exception as e:
        results["perplexity_error"] = str(e)
    try:
        results["google"] = query_google(prompt)
    except Exception as e:
        results["google_error"] = str(e)
    return results


if __name__ == "__main__":
    # Example usage
    test_prompt = "Explain the theory of relativity in simple terms."
    research_results = deep_research(test_prompt)
    print("Deep Research Results:")
    for provider, result in research_results.items():
        print(f"{provider}:\n{result}\n")
