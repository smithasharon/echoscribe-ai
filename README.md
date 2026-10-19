# EchoScribe AI – Intelligent Meeting Assistant

## Overview
EchoScribe AI is an AI-powered meeting assistant that converts meeting audio into text, generates concise summaries, and extracts action items to simplify meeting documentation.

## Problem Statement
Manually documenting meetings takes time, and important points or follow-up tasks may be missed. EchoScribe AI automates this process using AI models.

## Objectives
- Convert meeting audio into text.
- Generate concise meeting summaries.
- Extract action items, responsible persons, and deadlines when mentioned.
- Reduce manual note-taking and improve meeting follow-up.

## Features
- **Speech-to-Text:** Converts audio into text using OpenAI Whisper.
- **Meeting Summarization:** Generates summaries using Google's FLAN-T5.
- **Action-Item Extraction:** Uses Meta Llama 3 through Ollama.
- **Local LLM Execution:** Runs Llama 3 locally using Ollama.

## Technologies Used
- Python
- OpenAI Whisper
- Hugging Face Transformers
- FLAN-T5
- Meta Llama 3
- Ollama
- SoundDevice
- SciPy
- Requests
- FFmpeg

## Architecture
1. Record meeting audio and save it as a WAV file.
2. Convert the audio into text using Whisper.
3. Pass the transcript to FLAN-T5 for summarization.
4. Pass the same transcript to Llama 3 for action-item extraction.
5. Provide the transcript, summary, and action items as outputs.

## Installation and Setup
1. Install Python and FFmpeg.
2. Install the required Python dependencies.
3. Install Ollama and download the Llama 3 model.
4. Run the project using the main Python script.

## Limitations
- Transcription quality depends on audio clarity.
- AI-generated summaries and action items may contain errors.
- Long transcripts may be truncated.
- Speaker identification is not currently implemented.

## Future Enhancements
- Add speaker identification.
- Improve long-transcript processing.
- Develop a user-friendly web interface.
- Improve output validation and accuracy.

## Author
Smitha Sharon M
