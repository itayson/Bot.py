import requests
from telegram import Update, Bot
from telegram.ext import Updater, CommandHandler, CallbackContext

# Credenciais
TELEGRAM_TOKEN = '7636047693:AAFnP7BfCxGKAi-E1M7OSXolQEcoiUsVYlo'
DEEPSEARCH_API_URL = 'https://api.deepsearch.com/search'
DEEPSEARCH_API_KEY = 'jina_1fd80b89346d4a45b2f6c0d801aada2fQIsefw7r4mYbKmY-dnoftJb6Idiv'

# Função para buscar na API do DeepSearch
def search_deepsearch(query):
    headers = {
        'Authorization': f'Bearer {DEEPSEARCH_API_KEY}',
        'Content-Type': 'application/json'
    }
    params = {
        'q': query
    }
    response = requests.get(DEEPSEARCH_API_URL, headers=headers, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        return None

# Comando do Telegram para buscar na API do DeepSearch
def search_command(update: Update, context: CallbackContext):
    query = ' '.join(context.args)
    if not query:
        update.message.reply_text('Por favor, forneça um termo de busca.')
        return
    
    result = search_deepsearch(query)
    if result:
        update.message.reply_text(f'Resultado da busca: {result}')
    else:
        update.message.reply_text('Não foi possível obter resultados da API do DeepSearch.')

def main():
    updater = Updater(TELEGRAM_TOKEN, use_context=True)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('search', search_command))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()