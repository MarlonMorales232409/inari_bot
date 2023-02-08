
import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler
from telegram import InlineQueryResultArticle, InputTextMessageContent
from telegram.ext import InlineQueryHandler, filters
from telegram import Update
from telegram.ext import MessageHandler, ApplicationBuilder, CommandHandler, ContextTypes, CallbackQueryHandler
import telegram


logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

buttons = [
    [KeyboardButton('timezone')],
    [KeyboardButton('meet')]
]

reply_markup = ReplyKeyboardMarkup(buttons, one_time_keyboard=True)

async def timezone(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text='pronto dare la zona horaria de todos')

async def meet(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text='pronto convocare enlaces de google meet')


async def unknown(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Lo siento, no reconozco este comando.")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    buttons = [
    [KeyboardButton('timezone')],
    [KeyboardButton('meet')],
    [KeyboardButton('mail')]
    ]

    reply_markup = ReplyKeyboardMarkup(buttons, one_time_keyboard=True, resize_keyboard=True)

    await update.message.reply_text('Opciones', reply_markup=reply_markup)
    await context.bot.send_message(chat_id=update.effective_chat.id, text='Inirai Online')




if __name__ == '__main__':
    application = ApplicationBuilder().token('5948340958:AAEEBvAmKYkkj57bWtEBy2O0g14TQ5Vf7w4').build()


    start_handler = CommandHandler('start', start)
    application.add_handler(start_handler)

    timezone_handler = CommandHandler('timezone', timezone)
    application.add_handler(timezone_handler)

    meet_handler = CommandHandler('meet', meet)
    application.add_handler(meet_handler)

    application.add_handler(MessageHandler(filters.Regex('^meet$'), meet))

    # ? Se ejecuta solo si los comandos introducidos no son reconocidos
    # ! Debe dejarse esta instruccion al final de la lista de comandos siempre
    unknown_handler = MessageHandler(filters.COMMAND, unknown)
    application.add_handler(unknown_handler)


    application.run_polling()