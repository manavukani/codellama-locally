# CodeHelper using CodeLlama

CodeHelper is a tool that generates code snippets based on natural language prompts, powered by CodeLlama. Follow the steps below to set up and run CodeHelper on your local machine.

## Prerequisites

- Install and setup CodeLlama by following the instructions at [Ollama Download Page](https://ollama.com/download).

## Installation

1. Open your terminal.
2. Type the following command to verify proper installation of CodeLlama:
   ```
   ollama run codellama
   ```
   - Example prompt: "In Bash, how do I list all text files in the current directory (excluding subdirectories) that have been modified in the last month?"

3. Create a virtual environment for CodeHelper and activate it.
4. Install the required Python dependencies by running:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Clone this repository into your local system.
2. Train CodeLlama by running the following command in your terminal:
   ```
   ollama create codehelper -f modelfile
   ```
3. Verify proper setup of CodeHelper by running:
   ```
   ollama run codehelper
   ```
4. Launch the CodeHelper interface by running the following command:
   ```
   python app.py
   ```

Now you are ready to use CodeHelper to generate code snippets based on your prompts.

## Benefits of Locally Running LLM

1. **Increased Privacy**: Run the Language Model locally to keep your data and prompts on your machine, ensuring enhanced privacy and security.
  
2. **Faster Response Times**: With a locally hosted model, enjoy quicker code snippet generation without relying on external servers.

3. **Offline Availability**: Use CodeHelper without an internet connection, ideal for offline development environments.

4. **Customization**: Fine-tune the model locally to better suit your specific coding needs and preferences.

5. **Reduced Dependency on External Services**: Depend less on external services by running the Language Model locally, ensuring consistent functionality even during server downtime.
