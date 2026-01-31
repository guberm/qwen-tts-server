"""
Qwen3-TTS Free Open Source Server
Runs the HuggingFace models locally and provides REST API
"""

from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer
import soundfile as sf
import os
import uuid
import tempfile
from datetime import datetime

app = Flask(__name__)
CORS(app)

# Global model variables
model = None
tokenizer = None
MODEL_NAME = "Qwen/Qwen3-TTS-12Hz-0.6B-Base"  # Start with smaller model
DEVICE = "cuda" if torch.cuda.is_available() else "cpu"

# Create output directory
OUTPUT_DIR = os.path.join(tempfile.gettempdir(), "qwen_tts_output")
os.makedirs(OUTPUT_DIR, exist_ok=True)

def load_model():
    """Load the Qwen3-TTS model"""
    global model, tokenizer
    print(f"Loading model {MODEL_NAME} on {DEVICE}...")
    
    try:
        # This is a placeholder - actual model loading depends on Qwen3-TTS implementation
        # You'll need to check the HuggingFace model card for exact usage
        tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
        model = AutoModelForCausalLM.from_pretrained(
            MODEL_NAME,
            torch_dtype=torch.float16 if DEVICE == "cuda" else torch.float32,
            device_map="auto"
        )
        print("Model loaded successfully!")
        return True
    except Exception as e:
        print(f"Error loading model: {e}")
        print("Note: Qwen3-TTS may require specific loading code.")
        print("Please check the model card at: https://huggingface.co/Qwen/Qwen3-TTS-12Hz-0.6B-Base")
        return False

@app.route('/health', methods=['GET'])
def health():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'model_loaded': model is not None,
        'device': DEVICE,
        'model_name': MODEL_NAME
    })

@app.route('/tts/generate', methods=['POST'])
def generate_tts():
    """
    Generate TTS audio
    Expected JSON:
    {
        "text": "Text to synthesize",
        "voice": "voice_name",
        "language_type": "English"
    }
    """
    try:
        data = request.get_json()
        text = data.get('text', '')
        voice = data.get('voice', 'default')
        language = data.get('language_type', 'Auto')
        
        if not text:
            return jsonify({'error': 'No text provided'}), 400
        
        if model is None:
            return jsonify({'error': 'Model not loaded'}), 500
        
        # Generate unique filename
        audio_id = str(uuid.uuid4())
        output_file = os.path.join(OUTPUT_DIR, f"{audio_id}.wav")
        
        # TODO: Implement actual Qwen3-TTS inference
        # This is a placeholder - you need to check the model's usage from HuggingFace
        print(f"Generating TTS for: {text[:50]}...")
        print(f"Voice: {voice}, Language: {language}")
        
        # Placeholder: Create empty audio file
        # In reality, you'd use the model to generate audio here
        sample_rate = 24000
        duration = 1.0
        audio_data = torch.zeros(int(sample_rate * duration))
        sf.write(output_file, audio_data.numpy(), sample_rate)
        
        return jsonify({
            'status': 'success',
            'audio_id': audio_id,
            'url': f'http://localhost:5000/audio/{audio_id}',
            'message': 'Note: This is a placeholder. Real implementation needs Qwen3-TTS inference code.'
        })
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/audio/<audio_id>', methods=['GET'])
def get_audio(audio_id):
    """Serve generated audio file"""
    audio_file = os.path.join(OUTPUT_DIR, f"{audio_id}.wav")
    
    if not os.path.exists(audio_file):
        return jsonify({'error': 'Audio file not found'}), 404
    
    return send_file(audio_file, mimetype='audio/wav')

@app.route('/voices', methods=['GET'])
def get_voices():
    """Return available voices"""
    # These are the 9 premium timbres mentioned in the blog
    voices = [
        'Serena',    # 苏瑶
        'Uncle Fu',  # 福伯
        'Vivian',    # 十三
        'Aiden',     # 艾登
        'Ryan',      # 甜茶
        'Ono Anna',  # 小野杏
        'Sohee',     # 素熙
        'Dylan',     # 晓东 (Beijing)
        'Eric',      # 程川 (Sichuan)
    ]
    return jsonify({'voices': voices})

@app.route('/models', methods=['GET'])
def get_models():
    """Return available models"""
    models = [
        {
            'name': 'Qwen3-TTS-12Hz-0.6B-Base',
            'size': '0.6B',
            'features': 'Voice clone, fast inference'
        },
        {
            'name': 'Qwen3-TTS-12Hz-0.6B-CustomVoice',
            'size': '0.6B',
            'features': '9 premium timbres'
        },
        {
            'name': 'Qwen3-TTS-12Hz-1.7B-Base',
            'size': '1.7B',
            'features': 'Voice clone, higher quality'
        },
        {
            'name': 'Qwen3-TTS-12Hz-1.7B-CustomVoice',
            'size': '1.7B',
            'features': '9 premium timbres, style control'
        },
        {
            'name': 'Qwen3-TTS-12Hz-1.7B-VoiceDesign',
            'size': '1.7B',
            'features': 'Voice design from descriptions'
        },
    ]
    return jsonify({'models': models})

if __name__ == '__main__':
    print("=" * 60)
    print("Qwen3-TTS Free Open Source Server")
    print("=" * 60)
    print(f"\nDevice: {DEVICE}")
    print(f"Model: {MODEL_NAME}")
    print("\nIMPORTANT NOTES:")
    print("1. This server uses FREE open-source models from HuggingFace")
    print("2. No API key required!")
    print("3. You need to implement the actual Qwen3-TTS inference code")
    print("4. Check the model card for usage instructions:")
    print("   https://huggingface.co/Qwen/Qwen3-TTS-12Hz-0.6B-Base")
    print("\nTo install dependencies:")
    print("  pip install -r requirements.txt")
    print("\nTo change model, edit MODEL_NAME in server.py")
    print("=" * 60)
    
    # Load model
    success = load_model()
    if not success:
        print("\n⚠️  Model failed to load. Server will run but TTS won't work.")
        print("Please check the HuggingFace model documentation for proper usage.\n")
    
    # Start server
    print("\n🚀 Starting server on http://localhost:5000")
    print("Configure your Flutter app to use: http://YOUR_PC_IP:5000")
    print("(Replace YOUR_PC_IP with your actual local IP address)\n")
    
    app.run(host='0.0.0.0', port=5000, debug=True)
