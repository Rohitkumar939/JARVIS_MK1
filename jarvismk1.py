import sounddevice as sd
import soundfile as sf
import mlx_whisper
import ollama
import subprocess
import warnings

warnings.filterwarnings("ignore")

def record_audio(filename="input.wav", duration=5, fs=16000):
    print("\nListening... Speak now.")
    audio = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='float32')
    sd.wait()
    sf.write(filename, audio, fs)

def speak(text):
    print(f"\nJ.A.R.V.I.S: {text}")
    subprocess.run(["say", text])

print("Welcome to J.A.R.V.I.S, your personal AI assistant.")
messages = [
    {
        "role": "system", 
        "content": "You are a real-world, highly intelligent, and factual AI assistant named J.A.R.V.I.S. You exist in the real world, not a movie. Do not roleplay, do not mention Tony Stark, and do not make up fictional events. Keep responses to exactly 1 or 2 sentences and be helpful and concise."
    }
]

while True:
    try:
        input("\nPress Enter to start recording your question...")
        
        # 1. Record audio from the microphone
        record_audio("input.wav", duration=5)
        
        # 2. Transcribe
        print("[Transcribing...]")
        transcription = mlx_whisper.transcribe(
            "input.wav", 
            path_or_hf_repo="mlx-community/whisper-base.en-mlx"
        )["text"].strip()
        
        # --- NEW: WHISPER HALLUCINATION FILTER ---
        # If Whisper hears silence and hallucinates these words, we erase them.
        known_hallucinations = ["you", "you.", "thank you.", "thank you", "okay.", "okay"]
        if transcription.lower() in known_hallucinations:
            transcription = ""
        # -----------------------------------------
        
        print(f"\nYou: {transcription}")
        if not transcription:
            print("Did not catch that, sir.")
            continue
            
        messages.append({"role":"user", "content": transcription})
        
        # 3. Route text to the correct AI engine
        print("[Thinking...]")
        response = ollama.chat(model="llama3.2:3b", messages=messages)
        reply = response['message']['content']
        
        # 4. Speak the response
        speak(reply)
        
        # Save the AI's response to memory
        messages.append({"role":"assistant", "content": reply})

    except KeyboardInterrupt:
        print("\nGoodbye! Sir, have a great day!")
        break