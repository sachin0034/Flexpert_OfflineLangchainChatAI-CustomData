import openai
import json
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from nltk.stem import WordNetLemmatizer
import nltk

# Download required NLTK data
nltk.download('wordnet')
nltk.download('omw-1.4')



# Load your custom dataset from JSONL file
def load_jsonl(file_path):
    with open(file_path, 'r') as file:
        return [json.loads(line) for line in file]

dataset = load_jsonl("dataset.jsonl")

# Extract user messages and model responses from the dataset
user_messages = []
model_responses = []

for item in dataset:
    messages = item.get('messages', [])
    if len(messages) >= 2 and messages[0]['role'] == 'user' and messages[1]['role'] == 'model':
        user_messages.append(messages[0]['content'])
        model_responses.append(messages[1]['content'])

# Check if the lists are populated
if not user_messages or not model_responses:
    raise ValueError("No valid user and model messages found in the dataset.")

# Initialize and fit the TF-IDF vectorizer
vectorizer = TfidfVectorizer().fit(user_messages)
vectors = vectorizer.transform(user_messages).toarray()

# Initialize the lemmatizer
lemmatizer = WordNetLemmatizer()

# Enhanced preprocessing function
def preprocess_input(user_input):
    tokens = user_input.strip().lower().split()
    lemmatized_tokens = [lemmatizer.lemmatize(token) for token in tokens]
    return ' '.join(lemmatized_tokens)

# List of greeting messages
greeting_messages = [
    "hello", "hi", "hey", "good morning", "good afternoon", "good evening", "greetings", "howdy"
]

# Function to detect greeting messages
def is_greeting(message):
    preprocessed_message = preprocess_input(message)
    return preprocessed_message in greeting_messages

# Function to detect rephrasing and handle user queries
def get_response(user_input):
    # Check for greeting message
    if is_greeting(user_input):
        return "Hello! How can I assist you today?"

    # Preprocess the input for rephrasing detection
    preprocessed_input = preprocess_input(user_input)

    # Convert user input to vector
    user_vector = vectorizer.transform([preprocessed_input]).toarray()
    
    # Calculate cosine similarity
    similarities = cosine_similarity(user_vector, vectors)
    
    # Find the index of the most similar user message in the dataset
    most_similar_index = similarities.argmax()
    
    # Get the similarity score of the most similar user message
    most_similar_score = similarities[0, most_similar_index]

    # Define a threshold for similarity
    similarity_threshold = 0.5  # Lower the threshold to make the model more lenient

    # If the similarity score is below the threshold, return a message indicating no relevant information
    if most_similar_score < similarity_threshold:
        return "I'm sorry, I don't have relevant information for your query."

    # Get the most similar user message and its corresponding model response
    most_similar_message = user_messages[most_similar_index]
    response = model_responses[most_similar_index]

    # Return the response directly
    return response

# Example usage
user_input = "Hi"
response = get_response(user_input)
print(response)
