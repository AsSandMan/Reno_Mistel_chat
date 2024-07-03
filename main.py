# Подключаем сокет и настройки
from emoji import demojize
import socket
import conf
import logging
import re

# Настраиваем параметры
server = conf.server
port = conf.port
token = conf.token
nickname = conf.nickname
channel = conf.channel

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s — %(message)s', datefmt='%Y-%m-%d_%H:%M:%S', handlers=[logging.FileHandler('chat.log', encoding='utf-8')])

# Создаём класс для подключения к серверу
class Connection:
    def __init__(self):
        # Создаём сокет и подключаемся к серверу
        self.sock = socket.socket()
        self.sock.connect((server, port))
        
        # Отправляем команды
        self.sock.send(f"PASS {token}\n".encode('utf-8'))
        self.sock.send(f"NICK {nickname}\n".encode('utf-8'))
        self.sock.send(f"JOIN {channel}\n".encode('utf-8')) 
    
    def send(self, msg):
        self.sock.send(msg.encode('utf-8'))
    def resp(self):
        
        # Получаем ответ от сервера
        resp = self.sock.recv(2048).decode('utf-8')
        msg = []
        #пинг-понг от сервера
        if resp.startswith('PING'):
            self.sock.send("PONG\n".encode('utf-8'))
        #текстовые сообщения
        elif len(resp) > 0:
            logging.info(repr(resp))
            
            nick = re.findall(r'(?=:)(.*)(?=\!)', resp)[0]
            text = re.findall(r'(?<=PRIVMSG #reno_mistel :)(.*)(?=\r)', resp)
            
            # #':treldik!treldik@treldik.tmi.twitch.tv PRIVMSG #reno_mistel :SSSsss\r\n'
            # msg = re.findall(r'(?<=:)(.*)(?=\r)', resp)[0]
            words = resp.split(":") #????
            #reno_mistel!reno_mistel@reno_mistel.tmi.twitch.tv PRIVMSG #reno_mistel :: :! ломается
            
            
            try:
                nick.split('!')[0]
                msg.append([nick, text[0]])
                print(msg)
            except:
                pass
            # print(nick, msg)
            
            
        
    
        
        print(resp)

    def close(self):
        # Закрываем соединение
        self.sock.close()
        print('Connection closed')
        


        
conn = Connection()

while True:
    conn.resp()
    # conn.close()
    # def message(message):
        
    

