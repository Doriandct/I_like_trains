# I Like Trains Game

![Thumbnail](img/thumbnail_2.png)

## Overview

I Like Trains Game is a multiplayer game where players take on the role of train operators, navigating a shared game world to collect passengers, strategically expand their trains, and skillfully avoid collisions. Built with Python and Pygame, the game employs a client-server architecture to enable networked gameplay, offering a blend of strategic decision-making and real-time reactions.

## Requirements

*   Python 3.10

## Setup Instructions

Follow these steps to set up and run the game:

### 1. Create a virtual environment (do this once after cloning the project)

```bash
python -m venv venv
```

### 2. Activate the virtual environment (every time before starting the project)

#### On Windows

```bash
.\venv\Scripts\activate
```

#### On macOS/Linux

```bash
source venv/bin/activate
```

### 3. Install the necessary dependencies

After activating the virtual environment, install the necessary dependencies:

```bash
pip install -r requirements.txt
```

### 4. Execute the client

To execute the server locally, use the following command:

```bash
python server/server.py
```

If you want to host a server accessible by other machines, you can override the HOST constant from the console (here is an example):

```bash
python server/server.py 192.168.1.100
```

To execute the client locally, use the following command:

```bash
python client.py
```

Same thing if you want to connect to a distant machine:
```bash
python client.py 192.168.1.100
```


## Logging System

The game uses Python's built-in logging system to help with debugging and monitoring. Change the logging level in the `logging.basicConfig` function in the `agent.py` file.

Available log levels (from most to least verbose):

- DEBUG: Detailed information for debugging
- INFO: General information about game operation
- WARNING: Indicates potential issues
- ERROR: Serious problems that need attention
- CRITICAL: Critical errors that prevent the game from running

Logs are displayed in the console and include timestamps, module name, and log level.

## Simulate a server with multiple clients

### Local server

Start a local server with the previous command and run the following one with the wished number of local clients:

To simulate 10 clients:
```bash
.\simulate_clients.ps1' -numClients 10 
```

### Distant server

Modify the line `$scriptPath = "python client.py"` with the command you want in the `simulate_clients.ps1` program to automatically launch clients that will connect the distant server. 
In the previous example it would be: `$scriptPath = "python client.py 192.168.1.100"`.

Entering the following command will connect 10 clients to the distant server: 
```bash
.\simulate_clients.ps1' -numClients 10 
```