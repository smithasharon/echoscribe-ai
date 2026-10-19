from speech_to_text import transcribe_audio
from summarizer import generate_summary
from llm_action_extractor import extract_actions

# Step 1: Convert audio to text
transcript = transcribe_audio("meeting.wav")

print("\n========== TRANSCRIPT ==========\n")
print(transcript)

# Step 2: Generate summary
summary = generate_summary(transcript)

print("\n========== SUMMARY ==========\n")
print(summary)

# Step 3: Extract action items using Llama 3
actions = extract_actions(transcript)

print("\n========== ACTION ITEMS ==========\n")
print(actions)

