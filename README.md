# server_client-chat

## Description:
this project was created to show you how networking and 2 computers can chat with each other. this is a project that teach you how hosts can communicate with each other
this chat works only on the LAN because the code refer to the local/private IP. this project is for Ethical Hackers and CCNA learners that want a living example
of 2 computers communicate in the Ethernet.

## How It Works?
the python files are using a library called 'socket' and with that library in python you can open ports and create a connection with hosts.
with the simplest GUI in python and the reverse_shell method I manage  to communicate with the hosts, and it works just like that:
the 'serverChat.py' file used to open Port 1234 and wait for the client to connect, while the client is connecting the server is in "listen mode".
after the connection was made the server and the client communicate with each other by sending messages.
the client has a Client tag and the server has a Server tag and you can learn from that how the ethernet works.


# Installation and Usage:

#### System Requirements
- Python 3.x
- threading (library) 
- tkinter (library)

#### Installation:
1. **Clone the repository from GitHub:**
   ```cmd
   git clone https://github.com/ReddCrow12/server_client-chat.git

2. **Navigate to the project directory:**
   ```cmd
    cd server_client-chat
    cd server-client chat

#### Usage 
1. **To run 'serverChat', execute the following command in your terminal:**
   ```cmd
   python serverChat.py

2. **To run 'clientChat', execute the following command in your terminal:**
   ```cmd
   python clientChat.py

# Screenshots:
![image](https://github.com/ReddCrow12/server_client-chat/assets/173953884/ead4b9e7-ace5-40e4-922b-4893211150da)

![image](https://github.com/ReddCrow12/server_client-chat/assets/173953884/fa7885bc-5050-4240-ae7c-88d46fdf8593)

![image](https://github.com/ReddCrow12/server_client-chat/assets/173953884/22facc16-65f6-43b3-9d15-9f23958ea79a)

