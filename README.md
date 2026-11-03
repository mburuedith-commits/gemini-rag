# Gemini RAG and RTCCO Python Script

A lightweight Python-based command-line tool that leverages the Google GenAI SDK to implement **Retrieval-Augmented Generation (RAG)** and **Real-Time Context Control / System Instructions (RTCCO)**. 

The script reads local text data to supply contextual information to the Gemini model, allowing it to answer queries accurately based on your custom dataset.

## Features
* **RAG (Retrieval-Augmented Generation):** Pulls relevant text context dynamically from local files (`data.txt`) to ground model responses.
* **RTCCO (Real-Time Context Control):** Uses system instructions to guide model behavior and tone during execution.
* **Terminal Interface:** Built with Python for quick local execution and interaction via the command line.

## Project Structure
```text
├── chatboard.py      # Main Python script executing the Gemini model integration
└── data.txt          # Local source data used for contextual retrieval
