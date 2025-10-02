# Multi-Agent System (Powered by phidata & Groq)

This project demonstrates a specialized Retrieval-Augmented Generation (RAG) system built using the **phidata** framework. It orchestrates a team of agents powered by the high-speed Groq inference engine and the Qwen 32B model to search the web, gather information, and provide comprehensive, well-referenced, and structured answers.

## 🚀 Getting Started

Follow these steps to set up and run the multi-agent system.

### Prerequisites

1.  **Python 3.9+** installed.
2.  A **Groq API Key**.

### 1. Project Setup

Start by creating and activating a virtual environment, and installing the necessary packages:

```bash
# Create and activate the virtual environment
python3 -m venv venv
source venv/bin/activate  # Use 'venv\Scripts\activate.bat' on Windows

# Install dependencies
pip install phidata python-dotenv
