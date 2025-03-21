import requests
import asyncio
from telegram import Update
from telegram.ext import Application, CommandHandler, CallbackContext

# Credenciais fictícias
TELEGRAM_TOKEN = '7636047693:AAFnP7BfCxGKAi-E1M7OSXolQEcoiUsVYlo'
DEEPSEARCH_API_URL = 'https://api.deepsearch.com/search'
DEEPSEARCH_API_KEY = 'jina_1fd80b89346d4a45b2f6c0d801aada2fQIsefw7r4mYbKmY-dnoftJb6Idiv'

# Função para buscar na API do DeepSearch
def search_deepsearch(query):
    headers = {
        'Authorization': f'Bearer {DEEPSEARCH_API_KEY}',
        'Content-Type': 'application/json'
    }
    params = {'q': query}
    
    response = requests.get(DEEPSEARCH_API_URL, headers=headers, params=params)
    
    if response.status_code == 200:
        return response.json()
    return None

# Comando do Telegram para buscar na API do DeepSearch
async def search_command(update: Update, context: CallbackContext):
    if not context.args:
        await update.message.reply_text('Por favor, forneça um termo de busca.')
        return
    
    query = ' '.join(context.args)
    result = search_deepsearch(query)
    
    if result:
        await update.message.reply_text(f'Resultado da busca: {result}')
    else:
        await update.message.reply_text('Não foi possível obter resultados da API do DeepSearch.')

# Função principal para iniciar o bot
def main():
    app = Application.builder().token(TELEGRAM_TOKEN).build()
    
    app.add_handler(CommandHandler('search', search_command))
    
    print("Bot está rodando...")
    app.run_polling()

if __name__ == '__main__':
    main()