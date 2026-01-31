# Qwen3-TTS Free Open Source Server

A local Python server that runs the **FREE** Qwen3-TTS models from Alibaba Qwen's HuggingFace collection. No API key, no payment, no cloud dependency - everything runs on your machine!

## 🌟 Features

- ✅ **Completely FREE** - No API key or payment required
- ✅ **Open Source Models** - Download directly from HuggingFace
- ✅ **Local Processing** - Runs on your own hardware
- ✅ **Privacy First** - Your data stays on your machine
- ✅ **Android Ready** - Works with the included Flutter app
- ✅ **Multiple Models** - Choose from 0.6B and 1.7B versions
- ✅ **10 Languages** - Chinese, English, Japanese, Korean, German, French, Russian, Portuguese, Spanish, Italian
- ✅ **Streaming Support** - Real-time audio generation

## 📊 Available Models

| Model | Size | Speed | Quality | Voice Design | Custom Voice | Streaming |
|-------|------|-------|---------|--------------|--------------|----------|
| Qwen3-TTS-12Hz-0.6B-Base | 0.6B | ⚡ Fast | Good | - | ✅ | ✅ |
| Qwen3-TTS-12Hz-1.7B-Base | 1.7B | Medium | Excellent | - | ✅ | ✅ |
| Qwen3-TTS-12Hz-1.7B-CustomVoice | 1.7B | Medium | Excellent | - | ✅ (9 voices) | ✅ |
| Qwen3-TTS-12Hz-1.7B-VoiceDesign | 1.7B | Medium | Excellent | ✅ (text prompt) | ✅ | ✅ |

## 💻 System Requirements

### Minimum Hardware
- **RAM**: 8GB (0.6B model), 16GB (1.7B model)
- **GPU**: Optional (NVIDIA CUDA recommended for speed)
- **Storage**: 2-5GB for model download

### Software
- Python 3.9 or later
- CUDA 11.8+ (optional, for NVIDIA GPUs)

## 🚀 Quick Start

### 1. Install Dependencies

```bash
cd qwen_tts_server
pip install -r requirements.txt
```

### 2. Install PyTorch

**With NVIDIA GPU (CUDA 12.1)**:
```bash
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121
```

**Without GPU (CPU only)**:
```bash
pip install torch torchvision torchaudio
```

### 3. Run the Server

```bash
python server.py
```

The server will start on `http://0.0.0.0:5000`

**First run**: The model (1-5GB) will download automatically from HuggingFace

## ⚙️ Configuration

### Select a Model

Edit `server.py` line ~20:

```python
# Option 1: Fastest (0.6B - recommended for mobile)
MODEL_NAME = "Qwen/Qwen3-TTS-12Hz-0.6B-Base"

# Option 2: Best quality (1.7B)
MODEL_NAME = "Qwen/Qwen3-TTS-12Hz-1.7B-Base"

# Option 3: Custom voices with style (1.7B)
MODEL_NAME = "Qwen/Qwen3-TTS-12Hz-1.7B-CustomVoice"

# Option 4: Voice design from text descriptions (1.7B)
MODEL_NAME = "Qwen/Qwen3-TTS-12Hz-1.7B-VoiceDesign"
```

## 📱 Connect Flutter App

1. **Find your PC's IP address** (Windows):
   ```bash
   ipconfig
   ```
   Look for "IPv4 Address" (typically `192.168.x.x` or `10.x.x.x`)

2. **On your Android device**, open the Qwen TTS app:
   - Go to Settings
   - Enter Server URL: `http://192.168.1.100:5000` (use your actual IP)
   - Leave API Key empty
   - Select language and voice
   - Start using!

## 🔌 API Reference

### 1. Health Check
```bash
GET /health
```
Response: `{"status": "healthy", "model_loaded": true, "device": "cuda"}`

### 2. Generate TTS Audio
```bash
POST /tts/generate
Content-Type: application/json

{
  "text": "Hello world",
  "voice": "Serena",
  "language_type": "English"
}
```

Response: `{"status": "success", "audio_id": "uuid", "url": "..."}`

### 3. List Supported Voices
```bash
GET /voices
```

### 4. List Models
```bash
GET /models
```

### 5. Get Audio File
```bash
GET /audio/{audio_id}
```

## 🎯 Supported Languages & Voices

The model supports these languages with multiple voices each:
- 🇨🇳 Chinese (Mandarin, Cantonese, Shanghai)
- 🇬🇧 English (multiple accents)
- 🇯🇵 Japanese
- 🇰🇷 Korean
- 🇩🇪 German
- 🇫🇷 French
- 🇷🇺 Russian
- 🇵🇹 Portuguese
- 🇪🇸 Spanish
- 🇮🇹 Italian

## 📦 Project Structure

```
qwen_tts_server/
├── server.py              # Flask server & model loading
├── requirements.txt       # Python dependencies
├── README.md             # This file
└── .gitignore           # Git ignore rules
```

## 🔗 Resources

- **Model Cards**: https://huggingface.co/collections/Qwen/qwen3-tts
- **Official Blog**: https://qwen.ai/blog?id=qwen3tts-0115
- **GitHub Qwen**: https://github.com/QwenLM/Qwen3-TTS
- **Flutter App**: https://github.com/guberm/qwen-tts-app

## ⚠️ Important Notes

- **First startup** will download 1-5GB model from HuggingFace (one-time)
- **GPU is optional** but recommended for faster inference
- **Streaming mode** requires proper client implementation
- **Model implementation** - Current server.py is a placeholder. Check HuggingFace model cards for exact inference code

## 🐛 Troubleshooting

**Issue**: "No GPU found, using CPU"
- **Solution**: Install CUDA or proceed with CPU (slower but works)

**Issue**: Connection refused (Flutter app)
- **Solution**: Check firewall allows port 5000, verify PC IP, ensure server is running

**Issue**: Model download fails
- **Solution**: Check internet connection, ensure disk space (5GB+), try manual download from HuggingFace

**Issue**: Out of memory
- **Solution**: Use 0.6B model, close other apps, use CPU instead

## 📄 License

MIT License - Free to use and modify

## 🤝 Contributing

Contributions welcome! This is a community-driven project.

---

**Last Updated**: January 31, 2026