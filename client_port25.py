from socket import *

# Message content
# msg = "\r\n I love computer networks!"
subject = "Subject: I've Gone Fishing\r\n" ##
# from_header = "From: Fischer, Joe <fischermanjoe@egr.msu.edu>\r\n" ##
# to_header = "To: Sergakis, Kosta <sergaki1@msu.edu>\r\n" ##
content = "True professional dominance isn't found in the shallow end of the talent pool where the \"prey-eyed\" are content to drift. It is claimed in the deep water by those who understand that Aura is a byproduct of absolute, uncompromising discipline. While the school is busy discussing \"work-life balance,\" the high-value architect is busy out-scaling the entire ecosystem, optimizing their output-maxxing, and mogging the competition through sheer, high-fidelity execution. Stagnancy is a slow-motion surrender to the current of mediocrity. You don't wait for the pond to become favorable; you disrupt the water until the environment aligns with your vision. The window for elite-tier transition is narrow, and the middle ground is a trap for the hesitant. If you're feeling froggy, jump!"
signature = "Sent from my Samsung Smart Fridge"
endmsg = "\r\n.\r\n"

msg = subject + "\r\n" + content + "\n\n" + signature ##

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
rcptto = "RCPT TO: <rosscart@msu.edu>\r\n" 
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