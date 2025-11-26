# Kaggle Hackathon - Agentic AI

A comprehensive repository for building and experimenting with Agentic AI using Google's ADK (Agent Development Kit) framework. This project showcases how to create intelligent agents powered by Gemini LLM with web UI integration.

## 📋 Project Overview

This repository contains implementations of AI agents that can:
- Answer general questions using Google Search integration
- Process real-time information through the Gemini 2.5 Flash Lite model
- Interact with users through a web-based UI
- Manage API credentials securely
- Run in-memory agent execution with proper error handling and retry logic

## 🎯 Key Features

- **Google ADK Integration**: Uses the Agent Development Kit for building sophisticated AI agents
- **Gemini LLM**: Powered by Google's Gemini 2.5 Flash Lite model for fast and accurate responses
- **Web UI**: Interactive web interface on port 8081 for testing and development
- **Environment Management**: Secure API key handling with `.env` file support
- **Retry Logic**: HTTP retry configuration for robust API calls (5 attempts with exponential backoff)
- **In-Memory Execution**: InMemoryRunner for agent state management

## 📁 Repository Structure

```
kaggle-Hackthon/
├── mainArch.ipynb              # Main notebook with agent setup and demonstrations
├── sample-agent/               # Sample agent package
│   ├── __init__.py
│   └── agent.py               # Root agent definition
├── inspect_adk.py              # Utility to inspect ADK package files
├── find_web_command.py         # Utility to locate web command in ADK
├── read_fastapi.py             # FastAPI integration script
├── patch_notebook.py           # Notebook patching utility for port/URL updates
├── .env.example                # Environment variables template
├── .gitignore                  # Git ignore configuration
└── README.md                   # This file
```

## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- Google API Key (Gemini API access)
- pip package manager

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/adityapaswan568/kaggle-Hackthon.git
cd kaggle-Hackthon
```

2. **Create virtual environment**
```bash
python -m venv venv
venv\Scripts\activate  # On Windows
```

3. **Install dependencies**
```bash
pip install google-adk python-dotenv
```

4. **Configure environment variables**
```bash
# Copy the example file
copy .env.example .env

# Edit .env and add your Google API key
# GOOGLE_API_KEY=your_actual_key_here
```

### Running the Project

1. **Open the main notebook**
```bash
jupyter notebook mainArch.ipynb
```

2. **Run setup cells** (in order):
   - Install `google-adk` and `python-dotenv`
   - Configure API key from `.env`
   - Test API connectivity

3. **Start the ADK Web UI**
   - Run the cell with `!adk web --port 8081 --url_prefix localhost:8081`
   - Navigate to `http://localhost:8081/dev-ui/`

## 📚 Main Components

### `mainArch.ipynb`
The primary notebook demonstrating:
- API key configuration and validation
- ADK agent imports and setup
- Retry configuration for HTTP requests
- Root agent creation with Gemini model
- InMemoryRunner initialization
- Interactive queries with the agent
- Web UI setup and usage

### `sample-agent/agent.py`
Defines a helpful assistant agent:
```python
Agent(
    model='gemini-2.5-flash-lite',
    name='root_agent',
    description='A helpful assistant for user questions.',
    instruction='Answer user questions to the best of your knowledge'
)
```

### Utility Scripts
- **`inspect_adk.py`**: Lists HTML, JS, and CSS files in the ADK package
- **`find_web_command.py`**: Locates web command definitions in ADK
- **`read_fastapi.py`**: Inspects FastAPI implementation details
- **`patch_notebook.py`**: Automatically patches notebook for correct port configurations

## 🔒 Security

All sensitive information is protected:
- API keys stored in `.env` (not committed)
- `.gitignore` configured to exclude:
  - `.env` files
  - `__pycache__/` and compiled Python files
  - Virtual environment directories
  - IDE configuration files

Use `.env.example` as a template - never commit actual credentials.

## 🔧 Configuration

### Port Management
The ADK web UI runs on port 8081 by default. If the port is busy:

```powershell
# Windows PowerShell
Get-NetTCPConnection -LocalPort 8081 | ForEach-Object { Stop-Process -Id $_.OwningProcess -Force }
```

### Retry Configuration
Customizable HTTP retry settings:
```python
retry_config = types.HttpRetryOptions(
    attempts=5,                    # Max retry attempts
    exp_base=7,                   # Exponential backoff base
    initial_delay=1,              # Initial delay in seconds
    http_status_codes=[429, 500, 503, 504]  # Status codes to retry
)
```

## 📊 Usage Examples

### Query the Agent
```python
response = await runner.run_debug("What is the capital of France?")
response = await runner.run_debug("What is the current time?")
```

### Access Web UI
After running the ADK web server, visit:
```
http://localhost:8081/dev-ui/
```

## 🐛 Troubleshooting

1. **Port 8081 in use**: Kill the process using the port command above
2. **API key not found**: Ensure `.env` file exists with `GOOGLE_API_KEY` set
3. **Module not found**: Run `pip install google-adk python-dotenv`
4. **Web UI shows 500 error**: Ensure the `!adk web` cell is running

## 📝 Notes

- The notebook uses Jupyter's async capabilities for agent interactions
- Google Search integration requires proper API configuration
- The agent uses streaming responses for better performance
- Web UI provides a visual interface for debugging and testing

## 👤 Author

**Aditya Paswan** - adityapaswan568

## 📄 License

This project is part of the Kaggle Hackathon challenge.

## 🔗 Resources

- [Google ADK Documentation](https://google.adk.dev)
- [Gemini API](https://ai.google.dev)
- [Python dotenv](https://github.com/theskumar/python-dotenv)

---

*Last Updated: November 26, 2025*
