from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN: Final = 'YOUR TOKEN'
BOT_USERNAME: Final = '@YOUR_BOT_NAME'


# COMMANDS-->
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Hello! Thanks for chatting . I am a GPT BOT!')


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('I am a GPT! Please type something so i can respond!!')


async def custom_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('This is a custom command!!')


# RESPONSES-->

def handle_response(text: str) -> str:
    processed: str = text.lower()

    if 'hello' in processed:
        return 'Hey there!!'
    if 'how are you' in processed:
        return 'I am good!!'
    if 'i love you python' in processed:
        return 'remember to subscribe!!'
    if 'I love you' in processed:
        return 'I love you too '
    if 'hey there' in processed:
        return 'yoo'

    return 'I do not understand what you wrote!!'


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message_type: str = update.message.chat.type
    text: str = update.message.text

    print(f'User ({update.message.chat.id}) in {message_type}: "{text}"')

    if message_type == 'group':
        if BOT_USERNAME in text:
            new_text: str = text.replace(BOT_USERNAME, '').strip()
            response: str = handle_response(new_text)
        else:
            return

    else:
        response: str = handle_response(text)

    print('Bot:', response)
    await update.message.reply_text(response)


# ERRORS -->
async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} caused error {context.error}')


if __name__ == '__main__':
    print('Starting the BOT........')
    print('------------------------------------------------')
    app = Application.builder().token(TOKEN).build()

    # COMMANDS-->

    app.add_handler(CommandHandler('Start', start_command))
    app.add_handler(CommandHandler('help', help_command))
    app.add_handler(CommandHandler('custom', custom_command))

    # MESSAGE-->
    app.add_handler(MessageHandler(filters.TEXT, handle_message))

    # ERROR-->
    app.add_error_handler(error)

    # POLLS THE BOT -->
    print('Polling.....')

    app.run_polling(poll_interval=2)
