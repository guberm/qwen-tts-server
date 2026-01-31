# Qwen3-TTS v1.0.0 Release

**Release Date**: January 31, 2026

First production release of Qwen3-TTS - A complete free, open-source text-to-speech solution!

## 🎉 What's Included

### ✅ Flutter Android App (v1.0.0)
- Complete Flutter application for Android
- Support for 10 languages and 49 voices
- Free local server integration
- Cloud API support (Alibaba DashScope)
- Text sharing from other apps
- Built-in audio player
- Local settings persistence
- Beautiful Material Design UI

### ✅ Python TTS Server (v1.0.0)
- Flask-based REST API server
- Support for 4 Qwen3-TTS models (0.6B and 1.7B)
- GPU acceleration (CUDA support)
- Free open-source models from HuggingFace
- No API key required
- Fully local processing
- Multi-language support

## 📥 Downloads

### Android App
- **app-release.apk** (46.8 MB) - Ready to install on Android 7.0+
- **qwen-tts-app-v1.0.0.zip** - Complete source code

### Server
- **qwen-tts-server-v1.0.0.zip** - Complete Python server with dependencies

## 🚀 Quick Start

### Install Server

```bash
# Extract server zip
unzip qwen-tts-server-v1.0.0.zip
cd qwen-tts-server-v1.0.0

# Install Python dependencies
pip install -r requirements.txt

# Install PyTorch
pip install torch torchvision torchaudio

# Run server
python server.py
```

### Connect Flutter App

1. Find your PC's IP: `ipconfig` (Windows)
2. In app Settings:
   - Server URL: `http://192.168.1.100:5000` (use your IP)
   - Leave API Key empty
3. Select language and voice
4. Start generating speech!

## 📋 Features

### Server Features
- ✅ Multiple model options (0.6B, 1.7B)
- ✅ GPU acceleration support
- ✅ REST API endpoints
- ✅ Voice cloning capability
- ✅ Streaming support
- ✅ Automatic model download
- ✅ Health checks
- ✅ Flask with CORS support
- ✅ Error handling
- ✅ Device detection (GPU/CPU)

### App Features
- ✅ 49 professional voices
- ✅ 10 language support
- ✅ Real-time audio playback
- ✅ Text import from other apps
- ✅ Configurable server/cloud API
- ✅ Language-based voice filtering
- ✅ Character counter with limits
- ✅ Error handling and user feedback
- ✅ Settings persistence
- ✅ Material Design 3 UI

## 🌟 Supported Languages

- 🇨🇳 Chinese (26 voices including dialects)
- 🇬🇧 English (13 voices)
- 🇯🇵 Japanese (5 voices)
- 🇰🇷 Korean (4 voices)
- 🇪🇸 Spanish (5 voices)
- 🇵🇹 Portuguese (4 voices)
- 🇫🇷 French (4 voices)
- 🇩🇪 German (4 voices)
- 🇮🇹 Italian (3 voices)
- 🇷🇺 Russian (3 voices)

## 📊 System Requirements

### Server
- Python 3.9+
- 8GB RAM (for 0.6B model)
- 2-5GB disk space
- Optional: NVIDIA GPU with CUDA for faster inference
- Windows, macOS, or Linux

### Android App
- Android 7.0+ (API 24)
- 50 MB free space
- Network connection for API calls

## 🔧 Technical Details

### Stack
- **Backend**: Flask (Python)
- **Frontend**: Flutter 3.0+ (Dart)
- **Models**: Qwen3-TTS from HuggingFace
- **Dependencies**: PyTorch, Transformers
- **Acceleration**: CUDA support for NVIDIA GPUs

### Models Included

#### 0.6B Models
- `Qwen3-TTS-12Hz-0.6B-Base` - Fast, lightweight
- `Qwen3-TTS-12Hz-0.6B-CustomVoice` - 9 preset voices

#### 1.7B Models
- `Qwen3-TTS-12Hz-1.7B-Base` - High quality
- `Qwen3-TTS-12Hz-1.7B-CustomVoice` - 9 preset voices with style control
- `Qwen3-TTS-12Hz-1.7B-VoiceDesign` - Voice design from descriptions

## 📝 Release Notes

### v1.0.0 - Initial Release

#### Added
- Complete Flask server for TTS generation
- Multiple Qwen3-TTS model support
- CUDA GPU acceleration
- REST API with health checks
- Voice and model listing endpoints
- Comprehensive error handling
- Docker support (optional)
- Complete documentation
- Python requirements file
- GitHub releases

#### Features
- Free and open-source
- No API key required
- GPU acceleration
- Multi-language support
- Cross-platform compatibility
- Easy Flask-based REST API
- CORS enabled for web clients

## 🆘 Troubleshooting

### Server won't start
- Check Python 3.9+ installed
- Verify dependencies: `pip install -r requirements.txt`
- Check port 5000 not in use
- Ensure internet for model download

### Model download fails
- Check internet connection
- Verify 5GB+ disk space
- Try manual download from HuggingFace

### GPU not detected
- Install CUDA Toolkit
- Verify NVIDIA drivers
- Reinstall PyTorch with CUDA support

### Connection from app fails
- Verify server running
- Check firewall allows port 5000
- Verify PC IP address
- Ensure same network

## 📚 Documentation

Comprehensive documentation available in:
- **README.md** - Server setup and API reference
- **requirements.txt** - Python dependencies
- **GitHub Wiki** - Detailed guides

## 🔗 Resources

- **App Repository**: https://github.com/guberm/qwen-tts-app
- **Server Repository**: https://github.com/guberm/qwen-tts-server
- **Qwen Models**: https://huggingface.co/collections/Qwen/qwen3-tts
- **Official Blog**: https://qwen.ai/blog?id=qwen3tts-0115

## 📄 License

MIT License - Free to use and modify

## 🤝 Contributing

Contributions welcome! Areas of interest:
- Performance optimization
- Additional model support
- Streaming improvements
- Docker containerization
- Kubernetes deployment

## ✨ Credits

- **Qwen3-TTS Models**: Alibaba Qwen Team
- **Flask Framework**: Pallets Projects
- **PyTorch**: Meta
- **HuggingFace**: Community & Alibaba
- **Community Contributors**: Your support!

## 🗓️ What's Next?

### Planned Features
- Advanced batch processing
- Voice cloning improvements
- WebSocket streaming
- Advanced caching
- Performance benchmarks
- Additional language models
- API authentication
- Rate limiting

---

**Thank you for using Qwen3-TTS Server!**

For feedback, issues, or contributions, please visit:
- Issues: https://github.com/guberm/qwen-tts-server/issues
- Discussions: https://github.com/guberm/qwen-tts-server/discussions
