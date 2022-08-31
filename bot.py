from rubpy import Socket
from threading import Thread
from random import choice
from rubpy.network import Network

bot = Socket('yhfwbdezsdvcmfssltsmkvuchxqidmd')
net = Network()

def ads(text):
	for i in ['http', '@', 'join']:
		if i in text:
			return 1

def is_forwarded(data, forward_type,):
		try:
			if data.get('file_inline'):
				if data.get('forwarded_from'):
					if data.get('forwarded_from').get('type_from').lower() == forward_type:
						return True
			else:
				if data.get('forwarded_from').get('type_from').lower() == forward_type:
					return True
		except KeyError:
			return False
		except AttributeError:
			try:
				if data.get('file_inline'):
					path = data.get('forwarded_from')
					if path != None:
						if path.get('type_from').lower() == forward_type:
							return True
					else:
						return False
			except AttributeError:
				return False

def answer(chat):
	ran = ["سید ناموصا ولمون کن 🗿","سید پدرت رو اینقدر صدا نمیکنی ها 🗿","جونم سید؟ 🗿","ای بابا باز اینه 🗿",]
	sel = [choice(ran)
	bot.rubika.sendMessage(bot.object_guid(chat), sel, reply_to_message_id = bot.message_id(chat))
	return 1

def deleteMessage(chat,):
	while True:
		group_guid = bot.object_guid(chat,)
		admins = [i['member_guid'] for i in bot.rubika.getGroupAdmins(group_guid)]
		if bot.author_object_guid(chat,) in admins:
			return False
		else:
			return bot.rubika.deleteMessages(group_guid, [bot.message_id(chat,)])

def jok(chat,):
	bot.rubika.sendMessage(bot.object_guid(chat,), net.get('https://services.chabk.ir/api/jok/').data.decode('utf-8'), reply_to_message_id = bot.message_id(chat,))


for chat in bot.handler():
	if bot.set_action(chat) and bot.message_type(chat) == 'Text':
		text = bot.text(chat)
		print(text)
		if text == 'ربات' or text == 'بات':
			Thread(target = answer, args = (chat,)).start()
		elif is_forwarded(chat, 'channel'):
			print('True')
			Thread(target = deleteMessage, args = (chat,)).start()
		elif ads(text,):
			Thread(target = deleteMessage, args = (chat,)).start()
		elif text == 'جوک':
			Thread(target = jok, args = (chat,)).start()
