# Gemini Function Tool Agent (Toy AI Agent)

This project implements a simple AI-agent architecture that simulates tool use via Google's Gemini API function-calling capabilities. It serves as a toy version of an autonomous agent that can inspect, modify, and execute Python code within a controlled working directory.

---

## 🚀 Overview

At its core, the agent enables four core file-based tools:
1. **Get directory contents**
2. **Read file content**
3. **Write content to a file**
4. **Execute a Python file**

All functions are schema-wrapped and callable through the Gemini API using the `Tool` interface. The agent ensures all operations are sandboxed within a defined working directory.

---

## 🛠️ Available Tools

These tools are exposed via structured schemas compatible with Gemini's function calling:

### 1. `get_files_info`
Lists files in a directory (relative to the working directory), returning file sizes and directory flags.

### 2. `get_file_content`
Reads up to `MAX_CHARS` characters of a file’s content, with truncation indicated if needed.

### 3. `write_file`
Writes string content to a file. If the file does not exist, it is created. Directories are created as needed.

### 4. `run_python_file`
Executes a Python script with optional command-line arguments and returns its stdout/stderr.

Each tool validates that file access stays within a restricted `WORKING_DIR` for safety.

---

## 🔄 Function Calling via Gemini

The agent uses the `types.Tool` interface to define available functions (`available_functions` in `call_function.py`). When the Gemini model issues a function call, `call_function()` routes the request to the appropriate local function using introspected arguments.

This system allows the model to chain operations like:
- Listing a directory
- Reading a specific file
- Editing that file
- Running it to view the output

---

## 🧪 Example Use Cases

- Let Gemini inspect the content of a Python script and suggest changes
- Automatically write new scripts and test them
- Simulate an AI dev agent that can browse, edit, and run code in a sandboxed directory

---

## 📌 Requirements

- Python 3.10+
- `google-generativeai` Python package

---

## ⚠️ Notes

- The actual configuration for `MAX_CHARS` and `WORKING_DIR` must be defined in a `config.py` file.
- This project is meant as a **controlled sandbox** — no file access outside the working directory is allowed.

---

## ✍️ Author

Geoffrey Giordano

