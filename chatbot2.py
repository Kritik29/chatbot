from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

chatbot = ChatBot('Ron Obvious')

# Create a new trainer for the chatbot
trainer = ChatterBotCorpusTrainer(chatbot)

# Train the chatbot based on the english corpus
trainer.train("chatterbot.corpus.english")

print("You are now connected to Charlie.bot")
print('ctrl+c to exit')
while True:
    try:
        print(' ')
        request = input("You: ")
        response = chatbot.get_response(request)
        print("Bot: ", response)
        print(' ')
    except (KeyboardInterrupt, EOFError, SystemExit):
        break
