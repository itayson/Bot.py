import os
   import requests
   from telegram import Update
   from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

   # Configurações
   TELEGRAM_TOKEN = '7636047693:AAFnP7BfCxGKAi-E1M7OSXolQEcoiUsVYlo'
   DEEPSEEK_API_KEY = 'jina_1fd80b89346d4a45b2f6c0d801aada2fQIsefw7r4mYbKmY-dnoftJb6Idiv'
   DEEPSEEK_API_URL = 'https://api.deepseek.com/v1/chat/completions'  # Exemplo de endpoint

   # Função para lidar com o comando /start
   def start(update: Update, context: CallbackContext) -> None:
       update.message.reply_text('Olá! Eu sou um bot integrado com a API do DeepSeek. Como posso ajudar?')

   # Função para lidar com mensagens de texto
   def handle_message(update: Update, context: CallbackContext) -> None:
       user_message = update.message.text

       # Chamada à API do DeepSeek
       headers = {
           'Authorization': f'Bearer {DEEPSEEK_API_KEY}',
           'Content-Type': 'application/json'
       }
       data = {
           'prompt': user_message,
           'max_tokens': 150
       }
       response = requests.post(DEEPSEEK_API_URL, headers=headers, json=data)

       if response.status_code == 200:
           deepseek_response = response.json().get('choices')[0].get('text', 'Desculpe, não entendi.')
           update.message.reply_text(deepseek_response)
       else:
           update.message.reply_text('Desculpe, houve um erro ao processar sua mensagem.')

   def main() -> None:
       # Inicializa o Updater e passa o token do seu bot
       updater = Updater(TELEGRAM_TOKEN)

       # Obtém o dispatcher para registrar handlers
       dispatcher = updater.dispatcher

       # Registra o handler para o comando /start
       dispatcher.add_handler(CommandHandler("start", start))

       # Registra o handler para mensagens de texto
       dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

       # Inicia o bot
       updater.start_polling()

       # Roda o bot até que você pressione Ctrl-C
       updater.idle()

   if __name__ == '__main__':
       main()
