# GPInfoF1
[![Python](https://img.shields.io/badge/Python-3.9-red)](https://www.python.org/)
[![Telegram Bot](https://img.shields.io/badge/Teelgram-Bot-blue)](https://python-telegram-bot.org/)
[![Docker](https://img.shields.io/badge/Docker-blue)](https://www.docker.com/)
[![Fly.io](https://img.shields.io/badge/Fly.-io-orange)](https://fly.io/)

**GPInfoF1** is a Telegram bot that displays information about F1 schedules and next GP info.

## Screenshots
![gpinfof1_screenshot](https://user-images.githubusercontent.com/30499621/227471085-ee87a62e-746e-4dfc-8e3f-f8cc10712062.png)

## Commands
- **/help** --> Show help message.
- **/nextf1gp** --> Show Next GP Timetable.
- **/next5g1gp** --> Show Five Next GP Timetable.
- **/f1schedule** --> Show all F1 schedule.

## Prerequisites
- Python 3.7+
- A [Telegram bot](https://core.telegram.org/bots#6-botfather) and its token (see [tutorial](https://core.telegram.org/bots/tutorial#obtain-your-bot-token))
- A [Fly.io](https://fly.io/) account to deploy Telegram Bot (see [tutorial](https://bakanim.xyz/posts/deploy-telegram-bot-to-fly-io/)).

## Getting started

### Configuration
Create a file `token.env` in the root directory and write inside:
| Parameter    | Description                                                                                                                                                   |
|--------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `TOKEN`      | Your Telegram bot's token, obtained using [BotFather](http://t.me/botfather) (see [tutorial](https://core.telegram.org/bots/tutorial#obtain-your-bot-token))  |

### Deploy
To deploy the Telegram Bot to **Fly.io** see this [tutorial](https://bakanim.xyz/posts/deploy-telegram-bot-to-fly-io/).

## License
This project is released under the terms of the MIT license. For more information, see the [LICENSE](LICENSE) file included in the repository.