from typing import Dict

import google.generativeai as genai

from _config import GOOGLE_GEMINI_API_KEY
from application.utils.gemini_config import (
    GEMINI_MODEL,
    GEMINI_SYSTEM_INSTRUCTION,
    generate_gemini_prompt,
    get_gemini_generation_config,
)

# Configure the Gemini GenAI API in order to make requests to it
try:
    genai.configure(api_key=GOOGLE_GEMINI_API_KEY)
except Exception:
    raise Exception(
        "Failed to configure the Gemini GenAI API. Check whether the API key is valid."
    )

model = genai.GenerativeModel(
    model_name=GEMINI_MODEL, system_instruction=GEMINI_SYSTEM_INSTRUCTION
)


def get_gemini_summary(github_data: Dict[str, any], model_temperature: float) -> str:
    """
    Generates a summary of the GitHub repository data using the Gemini model.

    This function takes in a dictionary containing GitHub repository data and
    uses the Gemini model to generate a summary based on that data.

    Args:
        github_data (Dict[str, any]): A dictionary containing GitHub repository information
            as JSON data.

    Returns:
        dict[str,str]: A dictionary summary of the structured output generated by the Gemini model, providing insights into the GitHub repository based on the provided data.
    """
    response = model.generate_content(
        f"{generate_gemini_prompt(github_data)}",
        generation_config=get_gemini_generation_config(temperature=model_temperature),
    )
    return response.text
