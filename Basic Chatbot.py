

def chatbot():
    print("Chatbot: Hello! Type something to start (type 'bye' to exit)\n")

    while True:
        user_input = input("You: ").lower()

        if user_input == "hello":
            print("Chatbot: Hi!")
        elif user_input == "how are you":
            print("Chatbot: I am fine, thanks!")

        elif user_input == "what are you doing now":
            print("chatbot: now i am doing coding")
        elif user_input == "what is your future plan":
            print("chatbot: i want to engineer")
        elif user_input == "chatbot: o nice to meet you":    
            print("chatbot: nice to meet you also!") 
        elif user_input == "bye":
            print("Chatbot: Goodbye!")
            break
        else:
            print("Chatbot: Sorry, I don't understand that.")


chatbot()
