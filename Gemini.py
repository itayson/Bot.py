import requests
from telegram import Update, Bot
from telegram.ext import Updater, CommandHandler, CallbackContext

# Credenciais
TELEGRAM_TOKEN = '7300611039:AAGXQ8JbRisjSNWNkjju9umvZ5BONO5p4Hs'
GEMINI_API_URL = 'https://api.gemini.com/v1/pubticker/btcusd'  # Exemplo de URL da API
GEMINI_API_KEY = 'AIzaSyCmFWODWWmR-TYceGn0x2CRKDJ4miK5d9E'

# Função para buscar na API do Google Gemini
def search_gemini():
    headers = {
        'X-GEMINI-APIKEY': GEMINI_API_KEY,
    }
    response = requests.get(GEMINI_API_URL, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        return None

# Comando do Telegram para buscar na API do Google Gemini
def search_command(update: Update, context: CallbackContext):
    result = search_gemini()
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