# server_client-chat
### Description:
this project was created to show you how networking and 2 computers can chat with each other. this is a project that teach you how hosts can communicate with each other
this chat works only on the LAN because the code refer to the local/private IP. this project is for Ethical Hackers and CCNA learners that want a living example
of 2 computers communicate in the Ethernet.

## How It Works?
the python files are using a library called 'socket' and with that library in python you can open ports and create a connection with hosts.
the 'serverChat.py' file used to open Port 1234 and wait for the client to connect, while the client is connecting the server is in "listen mode".
after the connection was made the server and the client communicate with each other by sending messages and 
