import json

data = json.loads(open('nfL6.json', 'r').read())
train = []

for k, row in enumerate(data):
    train.append(row['question'])
    train.append(row['answer'])

from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer

chatbot = ChatBot('Seneca')
chatbot2 = ChatBot('Bart Simpson')
trainer = ListTrainer(chatbot)
trainer2 = ChatterBotCorpusTrainer(chatbot2)
trainer.train(train[:1024])
trainer2.train("chatterbot.corpus.english")

print('ctrl+c to exit')

while True:
    try:
        print(' ')
        print(' ')
        request = input('You: ')
        print(' ')
        response = chatbot.get_response(request)
        response2 = chatbot2.get_response(request)
        print('Bot 1: ', response)
        print(' ')
        print('Bot 2: ', response2)
    except (KeyboardInterrupt, EOFError, SystemExit):
        break
