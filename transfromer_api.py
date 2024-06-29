from transformers import pipeline

# Load a pre-trained text generation model
chatbot = pipeline('text-generation', model='gpt2')

def get_response(prompt):
    response = chatbot(prompt, max_length=100, num_return_sequences=1)
    return response[0]['generated_text']

if __name__ == "__main__":
    print("Chatbot: Hello! How can I assist you today?")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit", "bye"]:
            print("Chatbot: Goodbye!")
            break
        response = get_response(user_input)
        print(f"Chatbot: {response}")
