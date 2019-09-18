def user_question():
    question = input("What is your question?")
    while question != 'quit':
        if question[-1] != '?':
            print("I'm sorry, I can only answer questions.")
        question = input("What is your question?")

