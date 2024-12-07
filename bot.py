from telegram import Update
from telegram.ext import ContextTypes, ApplicationBuilder, CommandHandler, MessageHandler, filters
from config import BOT_TOKEN

# Función para el comando /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.effective_user
    message = (
        f"¡Hola {user.first_name}! 👋\n\n"
        "Bienvenido a nuestro bot. Aquí tienes algunas cosas que puedo hacer:\n"
        "- Responder a tus mensajes\n"
        "- Ayudarte con información\n"
        "- Y mucho más...\n\n"
        "¡No dudes en preguntarme lo que necesites!"
    )
    await update.message.reply_text(message)

# Función para manejar mensajes de texto
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    text = update.message.text
    response = f"Has enviado: '{text}'. ¿En qué puedo ayudarte con esto?"
    await update.message.reply_text(response)

# Configuración del bot
def main() -> None:
    application = ApplicationBuilder().token(BOT_TOKEN).build()

    # Registrar el handler para el comando /start
    application.add_handler(CommandHandler("start", start))

    # Registrar el handler para mensajes de texto
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    # Iniciar el bot
    application.run_polling()

if __name__ == '__main__':
    main()