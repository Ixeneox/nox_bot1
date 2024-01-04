import telebot 
from telebot import types
from pytube import YouTube
import os 


token="6506234777:AAFwjQ-ugZhbVezeZVxosZmlvQ4ftTfpQ_4"

bot=telebot.TeleBot(token)

@bot.message_handler(commands=["start"])
def start_command(message):
    chat_id=message.chat.id
    bot.send_message(chat_id,text="Let's try this command /yt")


@bot.message_handler(commands=["yt"])
def get(message):
    markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn=types.KeyboardButton("VIDEO")
    btn2=types.KeyboardButton("AUDIO")
    markup.row(btn,btn2)
    bot.send_message(message.chat.id,text="what do you wanna download ? VIDEO or AUDIO",reply_markup=markup)






@bot.message_handler(func=lambda message:True)

def chose_v_a(message):
   
 if message.text=="VIDEO":
    bot.send_message(message.chat.id,text="please send the link")
    bot.register_next_step_handler(message,video_download)

 if message.text=="AUDIO":
    bot.send_message(message.chat.id,text="please send the link")
    bot.register_next_step_handler(message,audio_download)




  



def video_download(message):
   sent=bot.send_animation(message.chat.id,animation="1.gif")
   sent_id=sent.message_id
   user_link=message.text
   url=YouTube(user_link)
   video_title=url.title
   stream=url.streams.get_by_resolution('720p')
   stream.download(filename="{}.mp4".format(video_title))
   bot.send_video(message.chat.id,open("{}.mp4".format(video_title),"rb"))
   bot.delete_message(message.chat.id,sent_id)
   os.remove("{}.mp4".format(video_title))

def audio_download(message):
   sent=bot.send_animation(message.chat.id,open("1.gif","rb"))
   sent_id=sent.message_id
   user_link=message.text
   url=YouTube(user_link)
   video_title=url.title
   stream=url.streams.get_audio_only()
   stream.download(filename="{}.mp3".format(video_title))
   bot.send_audio(message.chat.id,open("{}.mp3".format(video_title),"rb"))
   bot.delete_message(message.chat.id,sent_id)
   os.remove("{}.mp3".format(video_title))



    



bot.polling()



