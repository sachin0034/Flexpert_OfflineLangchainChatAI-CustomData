# OfflineLangchainChaiAi-CustomData

OfflineLangchainChaiAi-CustomData is a custom-built chatbot designed to respond to user inputs using a pre-defined dataset. The chatbot leverages machine learning techniques, specifically TF-IDF vectorization and cosine similarity, to provide intelligent and contextually relevant responses. The project is implemented using Python and Streamlit for a web-based interface.

## Features

- **Custom Dataset**: Uses a JSONL file containing user messages and corresponding model responses.
- **Preprocessing**: Utilizes lemmatization for enhanced input preprocessing.
- **Greeting Detection**: Recognizes and responds to common greeting messages.
- **Rephrasing Detection**: Identifies and responds to user queries based on similarity to previously seen messages.
- **Streamlit Integration**: Provides a simple and interactive web interface for the chatbot.

## Installation

### Prerequisites

- Python 3.x
- Streamlit
- scikit-learn
- NLTK

### Steps

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/flexpert-chatbot.git
    cd flexpert-chatbot
    ```

2. Install the required packages:

    ```bash
    pip install -r requirements.txt
    ```

3. Download NLTK data:

    ```python
    import nltk
    nltk.download('wordnet')
    nltk.download('omw-1.4')
    ```

## Usage

1. **Prepare your dataset**: Ensure you have a JSONL file (`dataset.jsonl`) with user messages and corresponding model responses. The structure should be as follows:

    ```json
    {"messages": [{"role": "user", "content": "User message here"}, {"role": "model", "content": "Model response here"}]}
    ```

2. **Run the Streamlit application**:

    ```bash
    streamlit run app.py
    ```

3. **Interact with the chatbot**: Open the Streamlit application in your web browser and start interacting with the chatbot. The chatbot will respond based on the messages and responses from your dataset.

## Code Overview

### `app.py`

This file contains the Streamlit application code. It initializes the conversation history, displays chat messages, accepts user input, and retrieves responses from the chatbot.

### `chatbot.py`

This file contains the core logic for the chatbot. It includes functions for loading the dataset, preprocessing user inputs, detecting greeting messages, and finding the most relevant response using cosine similarity.

### Key Functions

- **`load_jsonl(file_path)`**: Loads the dataset from a JSONL file.
- **`preprocess_input(user_input)`**: Preprocesses user input by tokenizing and lemmatizing.
- **`is_greeting(message)`**: Detects if a message is a greeting.
- **`get_response(user_input)`**: Retrieves the most relevant response to the user input based on cosine similarity.


Feel free to reach out if you have any questions or need further assistance. Happy chatting with OfflineLangchainChaiAi-CustomData!

##Email - sachinparmar98134@gmail.com
