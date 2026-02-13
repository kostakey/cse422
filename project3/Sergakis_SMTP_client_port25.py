from socket import *

# Message content
msg = "\r\n I love computer networks!"
endmsg = "\r\n.\r\n"

# Choose a mail server
mailserver = "mail.egr.msu.edu"
mailport = 25

# Create socket and establish a TCP connection with mailserver
# Fill in start
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((mailserver, mailport))
# Fill in end

recv = clientSocket.recv(1024).decode()
print(recv)
if recv[:3] != '220':
    print('220 reply not received from server.')

# Send HELO command and print server response.
# Fill in start
heloCommand = 'HELO Gone Fishing\r\n'
clientSocket.send(heloCommand.encode())
# Fill in end

recv1 = clientSocket.recv(1024).decode()
print(recv1)
if recv1[:3] != '250':
    print('250 reply not received from server.')

# Send MAIL FROM command and print server response.
# Fill in start
mailFrom = "MAIL FROM: <fischermanjoe@egr.msu.edu>\r\n"
clientSocket.send(mailFrom.encode())
recv2 = clientSocket.recv(1024).decode()
print(recv2)
# Fill in end

# Send RCPT TO command and print server response.
# Replace "xxxx@xx.xx" with your actual recipient email address
rcptto = "RCPT TO: <sergaki1@msu.edu>\r\n" 
# Fill in start
clientSocket.send(rcptto.encode())
recv3 = clientSocket.recv(1024).decode()
print(recv3)
# Fill in end

# Send DATA command and print server response.
# Fill in start
dataCommand = "DATA\r\n"
clientSocket.send(dataCommand.encode())
recv4 = clientSocket.recv(1024).decode()
print(recv4)
# Fill in end

# Send message data.
# Fill in start
clientSocket.send(msg.encode())
# Fill in end

# Message ends with a single period.
# Fill in start
clientSocket.send(endmsg.encode())
recv5 = clientSocket.recv(1024).decode()
print(recv5)
# Fill in end

# Send QUIT command and get server response.
# Fill in start
quitCommand = "QUIT\r\n"
clientSocket.send(quitCommand.encode())
recv6 = clientSocket.recv(1024).decode()
print(recv6)
clientSocket.close()
# Fill in end