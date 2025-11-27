import streamlit as st
from transformers import SpeechT5Processor, SpeechT5ForTextToSpeech, SpeechT5HifiGan
from datasets import load_dataset
import torch
import soundfile as sf
import io # For in-memory audio handling

# --- Configuration ---
SPEAKER_MAP = {
    "Speaker A (Female)": 7306,
    "Speaker B (Male)": 7400,
    "Speaker C (Male)": 7512,
}
MAX_CHARS = 250
SAMPLE_RATE = 16000

# --- Cached Model Loading ---
@st.cache_resource
def load_tts_components():
    # Load models
    processor = SpeechT5Processor.from_pretrained("microsoft/speecht5_tts")
    model = SpeechT5ForTextToSpeech.from_pretrained("microsoft/speecht5_tts")
    vocoder = SpeechT5HifiGan.from_pretrained("microsoft/speecht5_hifigan")
    
    # Load embedding dataset once
    embeddings_dataset = load_dataset("Matthijs/cmu-arctic-xvectors", split="validation")
    
    return processor, model, vocoder, embeddings_dataset

processor, model, vocoder, embeddings_dataset = load_tts_components()
# -----------------------------

# Streamlit UI
st.title("🎤 SpeechT5 Text-to-Speech Generator")
st.markdown("---")

# Speaker Selection
speaker_name = st.selectbox(
    "1. Choose a Speaker Voice:",
    list(SPEAKER_MAP.keys()),
    index=0
)
speaker_index = SPEAKER_MAP[speaker_name]

# Text Input
st.subheader("2. Enter Text")
text = st.text_area(f"Type up to {MAX_CHARS} characters:", height=150)
remaining_chars = MAX_CHARS - len(text)
st.caption(f"Characters remaining: **{remaining_chars}**")
text_to_process = text.strip()[:MAX_CHARS]


if st.button("Generate Speech", type="primary"):
    if not text_to_process:
        st.warning("Please enter some text first!")
    else:
        with st.spinner(f"Generating speech for {len(text_to_process)} characters..."):
            try:
                # Get the selected speaker embedding
                speaker_embeddings = torch.tensor(embeddings_dataset[speaker_index]["xvector"]).unsqueeze(0)
                
                # Generate speech
                inputs = processor(text=text_to_process, return_tensors="pt")
                speech = model.generate_speech(inputs["input_ids"], speaker_embeddings, vocoder=vocoder)

                # Save audio to in-memory buffer (BytesIO)
                buffer = io.BytesIO()
                # Use sf.write to save the audio data to the buffer
                sf.write(buffer, speech.numpy(), samplerate=SAMPLE_RATE, format="wav")
                audio_bytes = buffer.getvalue()
                
                st.success(f"✅ Speech generation complete for **{speaker_name}**!")

                # Play audio and automatically provide a download link
                st.audio(audio_bytes, format="audio/wav")

            except Exception as e:
                st.error(f"An error occurred during speech generation: {e}")

st.markdown("---")
st.info("Powered by Hugging Face's SpeechT5 and Streamlit.")
