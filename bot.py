import os
import telebot
import pickle
import xgboost as xgb
import pandas as pd

print("Starting...")
BOT_TOKEN = os.environ.get('BOT_TOKEN')
bot = telebot.TeleBot(BOT_TOKEN)

are_webhooks_dropped = bot.delete_webhook()
print("Deleted webbhooks, status:", are_webhooks_dropped)

model = pickle.load(open('grid_xgboost_params.sav', 'rb'))
print('Model loaded')


@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    bot.send_message(message.chat.id, "This bot can help you determine the class of water based on its features")
    bot.send_message(message.chat.id, "Type /water to input features one by one or type /water_list to list all features in one message")


@bot.message_handler(commands=['water'])
def res_free_chlrn(message):
    text = "Residual Free Chlorine (mg/L):"
    sent_msg = bot.send_message(message.chat.id, text, parse_mode="Markdown")
    bot.register_next_step_handler(sent_msg, turbidity)


def turbidity(message):
    values = [message.text]
    text = "Turbidity (NTU):"
    sent_msg = bot.send_message(message.chat.id, text, parse_mode="Markdown")
    bot.register_next_step_handler(sent_msg, fluoride, values)


def fluoride(message, values):
    values.append(message.text)
    text = "Fluoride (mg/L):"
    sent_msg = bot.send_message(message.chat.id, text, parse_mode="Markdown")
    bot.register_next_step_handler(sent_msg, coliform, values)


def coliform(message, values):
    values.append(message.text)
    text = "Coliform (Quanti-Tray) (MPN/100mL):"
    sent_msg = bot.send_message(message.chat.id, text, parse_mode="Markdown")
    bot.register_next_step_handler(sent_msg, e_coli, values)
    

def e_coli(message, values):
    values.append(message.text)
    text = "E.coli(Quanti-Tray) (MPN/100mL):"
    sent_msg = bot.send_message(message.chat.id, text, parse_mode="Markdown")
    bot.register_next_step_handler(sent_msg, get_prediction, values)


@bot.message_handler(commands=['water_list'])
def water_list(message):
    text = "Residual Free Chlorine (mg/L), Turbidity (NTU), Fluoride (mg/L), Coliform (Quanti-Tray) (MPN/100mL), E.coli(Quanti-Tray) (MPN/100mL):"
    sent_msg = bot.send_message(message.chat.id, text, parse_mode="Markdown")
    bot.register_next_step_handler(sent_msg, get_prediction_from_list)


def get_prediction(message, values):
    values.append(message.text)
    prediction = predict(values)
    bot.send_message(message.chat.id, "Predicted water class:")
    bot.send_message(message.chat.id, prediction, parse_mode="Markdown")


def get_prediction_from_list(message):
    values = message.text.split(', ')
    prediction = predict(values)
    bot.send_message(message.chat.id, "Predicted water class:")
    bot.send_message(message.chat.id, prediction, parse_mode="Markdown")


def predict(values):
    query = pd.DataFrame(
        {
            'Residual Free Chlorine (mg/L)': values[0],
            'Turbidity (NTU)': values[1],
            'Fluoride (mg/L)': values[2],
            'Coliform (Quanti-Tray) (MPN /100mL)': values[3],
            'E.coli(Quanti-Tray) (MPN/100mL)': values[4],
        },
        index=[0]
    )
    query = query.astype(float)
    prediction = model.predict(query)
    if prediction == 0:
        description = 'Compliance'
    elif prediction == 1:
        description = 'Operational'
    elif prediction == 2:
        description = 'Resample_Compliance'
    elif prediction == 3:
        description = 'Resample_Operational'
    elif prediction == 4:
        description = 'Op-resample'
    else:
        raise ValueError
    return description


bot.infinity_polling()
print("Listening to requests...")