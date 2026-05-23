def get_response(user_input):
    user_input = user_input.lower().strip()

    if user_input in ["hello", "hi", "hey"]:
        return "Hi there!"
    elif user_input in ["how are you", "how are you?"]:
        return "I'm fine, thanks! How about you?"
    elif user_input in ["bye", "goodbye", "see you"]:
        return "Goodbye! Have a great day!"
    elif user_input in ["what is your name", "what's your name"]:
        return "I'm a simple chatbot!"
    else:
        return "Sorry, I don't understand that. Try: hello, how are you, bye."


def main():
    print("Chatbot: Hello! Type 'bye' to exit.")

    while True:
        user_input = input("You: ")

        if not user_input:
            continue

        response = get_response(user_input)
        print(f"Chatbot: {response}")

        if user_input.lower().strip() in ["bye", "goodbye", "see you"]:
            break


if __name__ == "__main__":
    main()
