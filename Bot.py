import requests
from telegram import Update, Bot
from telegram.ext import Updater, CommandHandler, CallbackContext
from Gemini import get_gemini_data

# Credenciais
TELEGRAM_TOKEN = '7300611039:AAGXQ8JbRisjSNWNkjju9umvZ5BONO5p4Hs'

# Comando do Telegram para buscar na API do Google Gemini
def search_command(update: Update, context: CallbackContext):
    result = get_gemini_data()
    if result:
        update.message.reply_text(f"Resultado da busca: {result}")
    else:
        update.message.reply_text("Não foi possível obter resultados da API do Google Gemini.")

def main():
    updater = Updater(TELEGRAM_TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('search', search_command))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()