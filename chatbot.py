def main():
    print("==================================================")
    print("  Welcome to DecodeLabs Rule-Based AI Chatbot!  ")
    print("  Type 'exit' to stop the chat.                   ")
    print("==================================================\n")


    responses = {
        "hello": "Hi there! Welcome to the team.",
        "hi": "Hello! How can I assist you today?",
        "hey": "Hey! Ready to build some AI?",
        "how are you": "I'm operating perfectly within my deterministic guardrails. How are you?",
        "what is your name": "I am the Project 1 Rule-Based Chatbot.",
        "who are you": "I am the Project 1 Rule-Based Chatbot.",
        "what is ai": "AI is the simulation of human intelligence by machines. Right now, I'm using explicit logic rules!",
        "who created you": "I was created as part of the DecodeLabs Industrial Training Kit.",
        "help": "I can respond to simple greetings and questions. Try saying 'hello', 'what is your name', or type 'exit' to quit."
    }

  
    while True:
    
        raw_input = input("You: ")
        
       
        clean_input = raw_input.lower().strip()

       
        if clean_input in ['exit', 'quit', 'bye']:
            print("Chatbot: Goodbye! Shutting down the logic engine...")
            break

      
        if not clean_input:
            continue

      
        
        if clean_input in responses:
            
            reply = responses[clean_input]
        else:
            
            if "help" in clean_input:
                reply = "It looks like you need help! Try saying 'hello', 'what is your name', or type 'exit' to quit."
            elif "weather" in clean_input:
                reply = "I cannot check the weather because I don't have internet access yet—I'm just a logic engine!"
            elif "joke" in clean_input:
                reply = "Why do programmers prefer dark mode? Because light attracts bugs!"
            elif "name" in clean_input:
                reply = "I am the Project 1 Rule-Based Chatbot."
            else:
               
                reply = "I do not understand. My logic skeleton hasn't been programmed for that yet."
                
        
        print(f"Chatbot: {reply}")

if __name__ == "__main__":
    main()
