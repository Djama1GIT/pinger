# Pinger

Pinger is a bot that checks if my website has not crashed.

## Installation and Setup <sup><sub>(tested on Linux)</sub></sup>

1. Install Docker and Docker Compose if they are not already installed on your system.

2. Clone the project repository:

```bash
git clone https://github.com/Djama1GIT/telebot-pinger.git
cd telebot-pinger
```
3. Start the project:

```bash
docker-compose up --build
```


## Technologies Used

- Python - The programming language used for the project.
- Asyncio - A library in Python for writing single-threaded concurrent code using coroutines, multiplexing I/O access over sockets, and other resources.
- Aiohttp - An asynchronous HTTP client/server framework for asyncio and Python.
- PyTelegramBotAPI - A simple but extensible Python implementation for the Telegram Bot API.
- Docker - A platform used in the project for creating, deploying, and managing containers, allowing the application to run in an isolated environment.
