print("====================================")
print("          BASIC CHATBOT")
print("====================================")
print("Bot: Hello! I am your basic chatbot.")
print("Bot: Type 'bye' to exit the chatbot.")

while True:
    user_input = input("\nYou: ").lower().strip()

    if user_input in ["hello", "hi", "hey"]:
        print("Bot: Hello! How are you?")

    elif "how are you" in user_input:
        print("Bot: I am fine. Thank you for asking!")

    elif "your name" in user_input:
        print("Bot: My name is CodeBot.")

    elif user_input == "help":
        print("Bot: You can say hello, ask my name, or say bye.")

    elif user_input in ["bye", "exit", "quit"]:
        print("Bot: Goodbye! Have a nice day!")
        break

    else:
        print("Bot: Sorry, I don't understand that.")

print("\nChatbot session ended.")