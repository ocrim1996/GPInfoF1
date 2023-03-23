from dotenv import load_dotenv
import os
from telegram.ext import ApplicationBuilder, CommandHandler
from f1_schedule import next_f1_gp, f1_schedule, help, next5_f1_gp

load_dotenv("token.env")
bot_token = os.getenv("TOKEN")

app = ApplicationBuilder().token(bot_token).build()

app.add_handler(CommandHandler("help", help))
app.add_handler(CommandHandler("nextf1gp", next_f1_gp))
app.add_handler(CommandHandler("next5f1gp", next5_f1_gp))
app.add_handler(CommandHandler("f1schedule", f1_schedule))

app.run_polling()