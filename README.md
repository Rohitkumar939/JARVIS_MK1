J.A.R.V.I.S Mk.1 — Local Voice AI Assistant

A lightweight, fully local voice-activated AI assistant built for Apple Silicon Macs. It records audio from your microphone, transcribes it using MLX-optimized Whisper, processes your query locally via Ollama (llama3.2:3b), and speaks the response back using macOS's native speech synthesis.

✨ Features

100% Local & Private: No cloud APIs required—all speech recognition, LLM inference, and text-to-speech happen directly on your Mac.

Apple Silicon Optimized: Uses mlx-whisper for fast, hardware-accelerated speech-to-text transcription.

Hallucination Filtering: Includes a built-in filter to ignore common Whisper silence hallucinations (e.g., "Thank you.", "You").

Conversational Memory: Maintains session context across turns so you can ask follow-up questions naturally.

Concise Responses: System-prompted to deliver factual, grounded, 1–2 sentence answers ideal for voice interaction.

📋 Prerequisites

Because this script leverages Apple's MLX framework and native macOS utilities, you will need:

Hardware & OS: A Mac with Apple Silicon (M1, M2, M3, M4, etc.) running macOS.

Python: Python 3.9 or higher.

Ollama: Installed and running locally with the llama3.2:3b model pulled.

🚀 Installation & Setup

1. Install and Configure Ollama

Download and install Ollama from ollama.com. Once installed, open your terminal and pull the required model:

ollama pull llama3.2:3b


(Ensure the Ollama app or background service is running before starting the assistant.)

2. Install Python Dependencies

Clone or download jarvismk1.py into a project folder, then install the required Python packages:

pip install sounddevice soundfile mlx-whisper ollama


(Note: sounddevice relies on PortAudio. If you encounter audio errors on macOS, install it via Homebrew using brew install portaudio.)

🎙️ Usage

Open your terminal and navigate to the directory containing jarvismk1.py.

Run the script:

python jarvismk1.py


Grant Microphone Permissions: On your first run, macOS will prompt you to allow Terminal (or your IDE) to access the microphone. Click Allow.

Interact:

Press Enter when prompted.

Speak your question within the 5-second recording window.

Wait briefly while J.A.R.V.I.S transcribes, thinks, and speaks the answer aloud.

Exit: Press Ctrl + C at any time to shut down the assistant.

⚙️ Customization

You can easily tweak jarvismk1.py to fit your preferences:

Recording Duration: Change duration=5 in record_audio("input.wav", duration=5) to allow longer questions.

LLM Model: Replace "llama3.2:3b" in ollama.chat(...) with any other model you have pulled in Ollama (e.g., mistral, gemma2, or llama3.1:8b).

Voice: Modify subprocess.run(["say", text]) to use a specific macOS system voice, such as subprocess.run(["say", "-v", "Daniel", text]) for a British accent.
