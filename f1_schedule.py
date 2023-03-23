import csv
import utils
import logging
from datetime import datetime
from telegram import BotCommand

# Configura il logger
logger = logging.getLogger()
logger.setLevel(logging.INFO)

# Configura l'handler per la console
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)

# Configura il formato dei messaggi
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
console_handler.setFormatter(formatter)

# Aggiungi l'handler al logger
logger.addHandler(console_handler)


# Help function to see all bot features.
async def help(update, context):
    commands = [
        BotCommand(command='help', description='Show help message'),
        BotCommand(command='nextf1gp', description='Orari Prossimo GP di F1'),
        BotCommand(command='next5f1gp', description='Orari Prossimi 5 GP di F1'),
        BotCommand(command='f1schedule', description='Calendario F1')
    ]
    commands = [f'/{command.command} \- {command.description}' for command in commands]
    help_text = 'Ciao, sono il tuo *Bot per la F1* \U0001f3ce\uFE0F' + \
                '\n\nQuesto è quello che so fare:\n' + \
                '\n'.join(commands)
    logging.info("Help function called!")
    await update.message.reply_text(help_text, disable_web_page_preview=True, parse_mode='MarkdownV2')


# Function to see next gp timetable.
async def next_f1_gp(update, context):
    now = datetime.now()

    with open("GareF1_2023.csv") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        next(csv_reader)
        for gp in csv_reader:
            race_datetime = utils.race_time_with_delay(datetime.fromisoformat(gp[6]))
            if now < race_datetime:
                logging.info("Next F1 GP function called!")
                await update.message.reply_text(utils.format_next_f1_gp(gp), parse_mode='MarkdownV2')
                break


# Function to see all f1 schedule.
async def f1_schedule(update, context):
    with open("GareF1_2023.csv") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        next(csv_reader)
        logging.info("F1 Schedule function called!")
        await update.message.reply_text(utils.format_f1_schedule(csv_reader), parse_mode='MarkdownV2')


# Function to see next five gp timetables.
async def next5_f1_gp(update, context):
    now = datetime.now()

    with open("GareF1_2023.csv") as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=",")
        next(csv_reader)
        gps = []
        current_row = 0
        for gp in csv_reader:
            race_datetime = utils.race_time_with_delay(datetime.fromisoformat(gp[6]))
            if now < race_datetime:
                gps.append(gp)

                current_row = csv_reader.line_num

                # spostiamo il cursore del file al di sotto della riga trovata
                csv_file.seek(0)
                for _ in range(current_row):
                    next(csv_reader)

                # stampiamo le quattro righe successive (o meno)
                for _ in range(4):
                    try:
                        gp = next(csv_reader)
                        gps.append(gp)
                    except StopIteration:
                        # se non ci sono più righe disponibili, interrompiamo il ciclo
                        break
                # usciamo dal ciclo for
                break

        logging.info("Next 5 F1 GP function called!")
        await update.message.reply_text(utils.format_all_f1_gp(gps), parse_mode='MarkdownV2')



