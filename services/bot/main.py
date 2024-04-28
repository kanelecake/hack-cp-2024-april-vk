import os
import grpc
import telebot

from lib import categorizer_pb2_grpc, categorizer_pb2, searchengine_pb2_grpc, searchengine_pb2
from telebot import types
from dotenv import load_dotenv

load_dotenv()

bot = telebot.TeleBot(os.getenv("TOKEN"))

categorizer = grpc.insecure_channel('categorizer_service:18888')
searchengine = grpc.insecure_channel('searchengine_service:18881')

categorizerStub = categorizer_pb2_grpc.CategorizerStub(categorizer)
searchengineStub = searchengine_pb2_grpc.SearchEngineStub(searchengine)

# Feedback
feedbackMarkup = types.InlineKeyboardMarkup()
feedbackMarkupAccept = types.InlineKeyboardButton("Да", callback_data="Yes")
feedbackMarkupDecline = types.InlineKeyboardButton("Нет", callback_data="No")
feedbackMarkup.add(feedbackMarkupAccept, feedbackMarkupDecline)


def start_message(message):
    bot.send_message(
        message.chat.id,
        "Привет! Я Ферн, Ваш ИИ помощник! Вы можете задать мне вопрос, а я постараюсь на него ответить. Чем могу помочь?"
    )


def call_tutor(message):
    bot.send_message(message.chat.id, "Я передала Ваш вопрос куратору! Ожидайте, скоро он Вам ответит)")


@bot.message_handler(commands=['start'])
def handle_start(message):
    start_message(message)


def process_question(message):
    question = message.text
    result = categorizerStub.GetCategory(categorizer_pb2.GetCategoryRequest(
        question=question,
    ))

    print(result)
    if result.probability < 0.4:
        # TODO: РЕАЛИЗОВАТЬ ИСТОРИЮ СООБЩЕНИЙ
        print(result)
        bot.send_message(message.chat.id, "Я не совсем поняла вас. Не могли бы вы переформулировать ваш вопрос более подробно?")
    else:
        answerResponse = searchengineStub.GetAnswer(searchengine_pb2.GetAnswerRequest(
            question=question,
            category=result.category,
        ))

        bot.send_message(message.chat.id, 'Я нашла ответ по вашему запросу: \n\n"' + answerResponse.answer + '"')
        bot.send_message(message.chat.id, "Это то что вы искали?", reply_markup=feedbackMarkup)


@bot.callback_query_handler(func=lambda call: call.data == "Yes")
def handle_yes(call):
    bot.send_message(call.message.chat.id, "Всегда рада помочь. Обращайтесь)")
    bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)


@bot.callback_query_handler(func=lambda call: call.data == "No")
def handle_no(call):
    call_tutor(call.message)
    bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)


@bot.message_handler(content_types=['text'])
def handle_message(message):
    process_question(message)


if __name__ == "__main__":
    bot.polling()
