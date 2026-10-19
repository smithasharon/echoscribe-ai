import requests

def extract_actions(transcript):

    prompt = f"""
Extract all action items from this meeting transcript.

Return ONLY JSON.

Format:

[
  {{
    "person": "",
    "task": "",
    "deadline": ""
  }}
]

Transcript:
{transcript}
"""

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "llama3",
            "prompt": prompt,
            "stream": False
        }
    )

    return response.json()["response"]