import socket

lang = input('what is language?: ')

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost', 1337))

while True:
    message = input('Enter your message dude: ')
    if message == 'stop':
        client.close()
        break
    else:
        client.send(f'[{lang}]{message}'.encode())
