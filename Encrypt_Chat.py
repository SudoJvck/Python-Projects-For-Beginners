#Follow me @SudoJvck
#Encrypted Chat using Python
#Import libraries below
import rsa
import threading
import socket

#create keys
public_key, private_key = rsa.newkeys(1024)
public_partner = None

#one member of the chat will need to host the chat.
#define variable for chat host

choice = input("Do you want to host (1) or Connect (2): ")

#define function for hosting member using TCP
#we will use a demo ip address to host connection
if choice == "1":
  server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  server.bind(("192.168.0.164", 9999)) #your IP Address
  server.listen()

#Retrieve key
  client, _ = server.accept()
  client.send(public_key.save_pkcs1("PEM"))
  public_partner = rsa.PublicKey.load_pkcs1(client.recv(1024))


elif choice == "2":
  client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  client.connect(("192.168.0.164", 9999)) #Their IP address
  public_partner = rsa.PublicKey.load_pkcs1(client.recv(1024))
  client.send(public_key.save_pkcs1("PEM"))
else:
    exit()

#Define function to send messages
def sending_messages(c):
  while True:
    message = input("")
    c.send(rsa.encrypt(message.encode(), public_partner))
    print("You: " + message)

#Define function to receive messages 
def receiving_messages(c):
  while True:
    print("Partner: " + rsa.decrypt(c.recv(1024), private_key).decode())

threading.Thread(target=sending_messages, args=(client,)).start()
threading.Thread(target=receiving_messages, args=(client,)).start()


    
    
    
    
  
  
  

  
