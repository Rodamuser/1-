import requests
import telebot,time
from telebot import types
from gatet import Tele
import os
token = '7398537207:AAE6Yt9vQ5Li7LOGRW2O_9LWhf-aZKsY5wo'
bot=telebot.TeleBot(token,parse_mode="HTML")
subscriber = '1706037532'
@bot.message_handler(commands=["start"])
def start(message):
	if not str(message.chat.id) == '1706037532':
		bot.reply_to(message, "You cannot use the bot to contact developers to purchase a bot subscription @strawhatchannel69")
		return
	bot.reply_to(message,"Send the file now")
@bot.message_handler(content_types=["document"])
def main(message):
	if not str(message.chat.id) == '1706037532':
		bot.reply_to(message, "You cannot use the bot to contact developers to purchase a bot subscription @strawhatchannel69")
		return
	dd = 0
	live = 0
	ch = 0
	ko = (bot.reply_to(message, "Checking Your Cards...⌛").message_id)
	ee = bot.download_file(bot.get_file(message.document.file_id).file_path)
	with open("combo.txt", "wb") as w:
		w.write(ee)
	try:
		with open("combo.txt", 'r') as file:
			lino = file.readlines()
			total = len(lino)
			for cc in lino:
				current_dir = os.getcwd()
				for filename in os.listdir(current_dir):
					if filename.endswith(".stop"):
						bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text='𝗦𝗧𝗢𝗣𝗣𝗘𝗗 ✅\n𝗕𝗢𝗧 𝗕𝗬 ➜ @strawhatchannel69')
						os.remove('stop.stop')
						return
				try:
					data = requests.get('https://lookup.binlist.net/'+cc[:6]).json()
					
				except:
					pass
				try:
					bank=(data['bank']['name'])
				except:
					bank=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
				try:
					emj=(data['country']['emoji'])
				except:
					emj=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
				try:
					cn=(data['country']['name'])
				except:
					cn=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
				try:
					dicr=(data['scheme'])
				except:
					dicr=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
				try:
					typ=(data['type'])
				except:
					typ=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
				try:
					url=(data['bank']['url'])
				except:
					url=('𝒖𝒏𝒌𝒏𝒐𝒘𝒏')
				
				try:
					last = str(Tele(cc))
				except Exception as e:
					print(e)
				mes = types.InlineKeyboardMarkup(row_width=1)
				cm1 = types.InlineKeyboardButton(f"• {cc} •", callback_data='u8')
				cm3 = types.InlineKeyboardButton(f"• 𝗔𝗣𝗣𝗥𝗢𝗩𝗘𝗗 ✅ ➜ [ {live} ] •", callback_data='x')
				cm4 = types.InlineKeyboardButton(f"• 𝗗𝗘𝗖𝗟𝗜𝗡𝗘𝗗 ❌ ➜ [ {dd} ] •", callback_data='x')
				cm5 = types.InlineKeyboardButton(f"• 𝗧𝗢𝗧𝗔𝗟 👻 ➜ [ {total} ] •", callback_data='x')
				stop=types.InlineKeyboardButton(f"[ 𝐒𝐓𝐎𝐏 ]", callback_data='stop')
				mes.add(cm1, cm3, cm4, cm5, stop)
				bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text='''Wait for processing 
𝒃𝒚 ➜ @strawhatchannel69 ''', reply_markup=mes)
				msg = f'''{cc}
Payment successful ✅'''
				print(last)
				if 'Thank you' in last:
					live += 1
					bot.reply_to(message, msg)
				else:
					dd += 1
					time.sleep(5)
	except Exception as e:
		print(e)
	bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text='𝗕𝗘𝗘𝗡 𝗖𝗢𝗠𝗣𝗟𝗘𝗧𝗘𝗗 ✅\n𝗕𝗢𝗧 𝗕𝗬 ➜ @strawhatchannel69')
@bot.callback_query_handler(func=lambda call: call.data == 'stop')
def menu_callback(call):
	with open("stop.stop", "w") as file:
		pass
print("+-----------------------------------------------------------------+")
bot.polling()
