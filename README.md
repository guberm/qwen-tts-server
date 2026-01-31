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
- **Network**: Stable internet for initial model download

### Software
- Python 3.9 or later
- CUDA 11.8+ (optional, for NVIDIA GPUs)
- pip (Python package manager)

### Recommended Setup
- **RAM**: 32GB+ (for smooth inference)
- **GPU**: NVIDIA RTX 3060+ (8GB VRAM)
- **Storage**: SSD for faster model loading

## 🚀 Installation & Setup

### Step 1: Install Python

**Windows**:
- Download from [python.org](https://www.python.org/downloads/) (3.9+)
- Check "Add Python to PATH" during installation
- Verify: `python --version`

**macOS**:
```bash
# Using Homebrew
brew install python@3.11
```

**Linux**:
```bash
# Ubuntu/Debian
sudo apt-get install python3.11 python3-pip

# Fedora
sudo dnf install python3.11 python3-pip
```

### Step 2: Clone & Install Dependencies

```bash
# Clone repository
git clone https://github.com/guberm/qwen-tts-server.git
cd qwen-tts-server

# Create virtual environment (recommended)
python -m venv venv

# Activate virtual environment
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### Step 3: Install PyTorch

**With GPU Support (CUDA 12.1)**:
```bash
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu121
```

**With GPU Support (CUDA 11.8)**:
```bash
pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
```

**Without GPU (CPU only)**:
```bash
pip install torch torchvision torchaudio
```

**Verify installation**:
```bash
python -c "import torch; print(torch.cuda.is_available())"
# Returns True if GPU available, False if CPU only
```

### Step 4: Run the Server

```bash
python server.py
```

You should see:
```
============================================================
Qwen3-TTS Free Open Source Server
============================================================

Device: cuda  # or cpu
Model: Qwen/Qwen3-TTS-12Hz-0.6B-Base

🚀 Starting server on http://localhost:5000
Configure your Flutter app to use: http://YOUR_PC_IP:5000
```

**First run**: The model (1-5GB) will download automatically from HuggingFace.

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

### Performance Tuning

#### Use GPU (for faster inference)

```python
# In server.py, line ~40
DEVICE = "cuda"  # Change from "auto" to "cuda"
```

#### Use CPU (for compatibility)

```python
DEVICE = "cpu"
```

#### Enable Mixed Precision (faster on GPU)

```python
import torch
torch.set_float32_matmul_precision('high')  # High performance
```

## 📱 Connect Flutter App

### Step 1: Find Your PC's IP Address

**Windows (PowerShell)**:
```powershell
ipconfig
```
Look for "IPv4 Address" under your network adapter. Example: `192.168.1.100`

**macOS/Linux**:
```bash
ifconfig
# or
ip addr
```

### Step 2: Configure Flutter App

1. Open the Qwen TTS app on your Android device
2. Tap Settings (gear icon)
3. Set:
   - **Server URL**: `http://192.168.1.100:5000` (use your actual IP)
   - **API Key**: Leave empty
4. Select language and voice
5. Tap Generate!

### Step 3: Test Connection

On your PC, verify the server is accessible:

```bash
# Test health endpoint
curl http://localhost:5000/health

# Should return something like:
# {"status": "healthy", "model_loaded": true, "device": "cuda"}
```

## 🔌 API Reference

### Health Check

```bash
GET /health
```

**Response**:
```json
{
  "status": "healthy",
  "model_loaded": true,
  "device": "cuda",
  "model_name": "Qwen/Qwen3-TTS-12Hz-0.6B-Base"
}
```

### Generate TTS Audio

```bash
POST /tts/generate
Content-Type: application/json

{
  "text": "Hello world",
  "voice": "Serena",
  "language_type": "English"
}
```

**Response**:
```json
{
  "status": "success",
  "audio_id": "uuid-string",
  "url": "http://localhost:5000/audio/uuid-string"
}
```

### Get Audio File

```bash
GET /audio/{audio_id}
```

Returns the audio file (WAV format).

### List Supported Voices

```bash
GET /voices
```

**Response**:
```json
{
  "voices": ["Serena", "Cherry", "Ethan", ...]
}
```

### List Models

```bash
GET /models
```

## 💻 Running in Background (Windows)

### Option 1: Windows Task Scheduler

1. Open Task Scheduler
2. Create Basic Task
3. Set trigger: On startup
4. Set action: Start program
   - Program: `C:\Python311\python.exe`
   - Arguments: `C:\path\to\server.py`

### Option 2: Run in Terminal (Simple)

```bash
python server.py
# Keep terminal window open
```

### Option 3: Use `nohup` (macOS/Linux)

```bash
nohup python server.py > server.log 2>&1 &
```

## 📿 Docker Deployment (Optional)

### Build Docker Image

```dockerfile
FROM python:3.11-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
RUN pip install torch torchvision torchaudio

COPY server.py .

EXPOSE 5000
CMD ["python", "server.py"]
```

### Run with Docker

```bash
# Build
docker build -t qwen-tts-server .

# Run
docker run -p 5000:5000 qwen-tts-server
```

## 🍐 Performance Tips

1. **Use 0.6B model** for faster inference
2. **Enable GPU** if available (8x faster)
3. **Cache models** locally (avoid re-downloads)
4. **Use batch processing** for multiple requests
5. **Monitor VRAM** usage: `nvidia-smi`

## 🐛 Troubleshooting

### Issue: "No GPU found, using CPU"
**Solution**: 
- Check CUDA installation: `nvidia-smi`
- Install CUDA Toolkit: https://developer.nvidia.com/cuda-toolkit
- Reinstall PyTorch with CUDA support

### Issue: "Model download fails"
**Solution**:
- Check internet connection
- Ensure 5GB+ disk space
- Try manual download: `huggingface-cli download Qwen/Qwen3-TTS-12Hz-0.6B-Base`

### Issue: "Port 5000 already in use"
**Solution**:
- Find process: `lsof -i :5000` (macOS/Linux) or `netstat -ano | findstr :5000` (Windows)
- Kill process: `kill -9 <PID>` or use Task Manager
- Or change port in server.py: `app.run(port=8000)`

### Issue: "Connection timeout from Flutter app"
**Solution**:
- Verify server is running
- Check PC IP address is correct
- Disable firewall or allow port 5000
- Ensure phone and PC on same network
- Try ping: `ping 192.168.1.100` (use your IP)

### Issue: "Out of memory"
**Solution**:
- Use 0.6B model (smaller)
- Close other applications
- Use CPU instead of GPU
- Reduce batch size
- Increase system swap/virtual memory

## 🔗 Resources

- **HuggingFace Models**: https://huggingface.co/collections/Qwen/qwen3-tts
- **Official Blog**: https://qwen.ai/blog?id=qwen3tts-0115
- **PyTorch**: https://pytorch.org/
- **Flask Docs**: https://flask.palletsprojects.com/
- **Flutter App**: https://github.com/guberm/qwen-tts-app

## 📄 License

MIT License - Free to use and modify

## 🤝 Contributing

Contributions welcome! Areas of interest:
- Optimizations for faster inference
- Additional language support
- Docker/Kubernetes deployment
- Web UI for testing
- More voice options

## 📧 Support

For issues:
1. Check troubleshooting section
2. Search GitHub issues
3. Create new issue with:
   - OS and Python version
   - Error messages/logs
   - Steps to reproduce
   - Hardware specs (CPU/GPU)

---

**Last Updated**: January 31, 2026

**Status**: ✅ Active Development & Maintenance
