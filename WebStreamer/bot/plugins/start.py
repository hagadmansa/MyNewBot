from pyrogram import filters
from WebStreamer.vars import Var
from pyrogram.types import Message
from WebStreamer.bot import StreamBot
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

START_TEXT = """đ <b>Hello</b>,

đ¤ My Name is Hagadmansa Mega Bot, I can stream Telegram Files over HTTP.

đ§ Don't know how to do? No worries, just press the help button.

đ¨âđģ My Creator is <a href=https://t.me/hagadmansa>Hagadmansa</a>."""
   
HELP_TEXT = """<b>âšī¸ Help</b>

Here is the list of my commands, please read carefully everything. if anything happened to you then we are not responsible."""

HOWTOUSEME_TEXT = """<b>âšī¸ Help</b> > How To Use Me

My name is Hagadmansa Mega Bot, I am a member of Hagadmansa family. I can provide you direct download link of any telegram file/media. If you send me any file/media I will give an external download link, you can use that link to download any file outside telegram. My link is supported in any browser.

âĸ Send me any file/media from Telegram.
âĸ I Will provide an external download link for you.
âĸ All links will be permanent and have the fastest speed.

<b>đ Warning:</b>

âĸ 18+ content and pornography are strictly prohibited. Don't send me any pornographic/violent videos. You will get an instant ban if we see any kind of content like this."""

INSTRUCTIONS_TEXT = """<b>âšī¸ Help</b> > Instructions

1. Don't send photos to the bot, send them as a file.
2. Don't send multiple files at a time, send them one by one.

<b>đ Warning:</b>

âĸ 18+ content and pornography are strictly prohibited. Don't send me any pornographic/violent videos. You will get an instant ban if we see any kind of content like this."""

TUTORIALS_TEXT = """<b>âšī¸ Help</b> > Tutorials

All tutorials related to Bots, Website, Movies and etc, will be updated here. Till then you can visit my movie website <b>www.hagadmansa.com</b> to watch movies. Don't forget to subscribe my updates channel <b>@hagadmansa</b>.

<b>đ Warning:</b>

âĸ 18+ content and pornography are strictly prohibited. Don't send me any pornographic/violent videos. You will get an instant ban if we see any kind of content like this."""

ABOUT_TEXT = """<b>đ About</b>

<b>â¯ My Name:</b> <a href='https://t.me/hagadmansamegabot'>Hagadmansa Mega Bot</a>
<b>â¯ Creator:</b> <a href='https://t.me/hagadmansa'>Hagadmansa</a>
<b>â¯ Library:</b> <a href='https://pyrogram.org'>Pyrogram</a>
<b>â¯ Language:</b> <a href='https://Python.org'>Python</a>
<b>â¯ Database:</b> <a href='https://mongodb.com'>MongoDB</a>
<b>â¯ Server:</b> <a href='https://heroku.com'>Heroku</a>
<b>â¯ Channel:</b> <a href='https://t.me/hagadmansa'>Hagadmansa</a>
<b>â¯ Group:</b> <a href='https://t.me/hagadmansachat'>Hagadmansa Support</a>
<b>â¯ Brothers:</b> <a href='https://t.me/hagadmansabot'>Hagadmansa Bot</a>, <a href='https://t.me/hagadmansarobot'>Hagadmansa Robot</a>"""

RATING_TEXT = """<b>đ About</b> > Rating

I have a public channel a private channel and 3 bots, along with this also I have a website. you can rate and write a review on our public channel and bots.

<b>đŖ @hagadmansa</b>

1. Details are <a href='https://t.me/tlgrmcbot?start=hagadmansa'>here</a>
2. Review this channel <a href='https://t.me/tlgrmcbot?start=hagadmansa-review'>here</a>

<b>đ¤ @hagadmansabot</b>

1. Details are <a href='https://t.me/tlgrmcbot?start=hagadmansabot'>here</a>
2. Review this bot <a href='https://t.me/tlgrmcbot?start=hagadmansabot-review'>here</a>

<b>đ¤ @hagadmansarobot</b>

1. Details are <a href='https://t.me/tlgrmcbot?start=hagadmansarobot'>here</a>
2. Review this bot <a href='https://t.me/tlgrmcbot?start=hagadmansarobot-review'>here</a>

<b>đ¤ @hagadmansamegabot</b> 

1. Details are <a href='https://t.me/tlgrmcbot?star=hagadmansamegabot'>here</a>
2. Review this bot <a href='https://t.me/tlgrmcbot?start=hagadmansamegabot-review'>here</a>"""

SOURCE_TEXT = """<b>đ About</b> > Source

<b>âī¸NOTE:</b>

We are not open source yet, if in future we are open our code for everyone then we'll update the source code here."""

DONATE_TEXT = """<b>đ About</b> > Donate

<b>âī¸NOTE:</b>

We are not raising any funds right now, if in future we raise funds then we'll update here."""
        
START_BUTTONS = InlineKeyboardMarkup(
        [[
            InlineKeyboardButton('đ Website', url='https://hagadmansa.com'),
            InlineKeyboardButton('đŖ Updates', url='https://t.me/hagadmansa')
            ],[
            InlineKeyboardButton('âšī¸ Help', callback_data='help'),
            InlineKeyboardButton('đ About', callback_data='about')
        ]]
    )

HELP_BUTTONS = InlineKeyboardMarkup(
        [[
            InlineKeyboardButton('â How to use me', callback_data='howtouseme')
            ],[
            InlineKeyboardButton('âī¸ Instructions', callback_data='instructions'),
            InlineKeyboardButton('đš Tutorials', callback_data='tutorials'),
            ],[
            InlineKeyboardButton('đ Back', callback_data='home'),
            InlineKeyboardButton('đŖ Channel', url='https://t.me/hagadmansa')
        ]]
    )
HOWTOUSEME_BUTTONS = InlineKeyboardMarkup(
        [[
            InlineKeyboardButton('đ Back', callback_data='help'),
            InlineKeyboardButton('đ  Home', callback_data='home')
            ]]
    )
INSTRUCTIONS_BUTTONS = InlineKeyboardMarkup(
        [[
            InlineKeyboardButton('đ Back', callback_data='help'),
            InlineKeyboardButton('đ  Home', callback_data='home')
            ]]
   )
TUTORIALS_BUTTONS = InlineKeyboardMarkup(
        [[
            InlineKeyboardButton('đ Back', callback_data='help'),
            InlineKeyboardButton('đ  Home', callback_data='home')
            ]]
    )
ABOUT_BUTTONS = InlineKeyboardMarkup(
        [[
            InlineKeyboardButton('đ Visit Our Website', url='https://hagadmansa.com')
            ],[
            InlineKeyboardButton('â­ī¸ Rating', callback_data='rating'),
            InlineKeyboardButton('â¤ī¸ Source', callback_data='source'),
            ],[
            InlineKeyboardButton('đ Back', callback_data='home'),
            InlineKeyboardButton('đ¤ Donate', callback_data='donate')
        ]]
    )
RATING_BUTTONS = InlineKeyboardMarkup(
        [[
            InlineKeyboardButton('đ Back', callback_data='about'),
            InlineKeyboardButton('đ  Home', callback_data='home')
            ]]
    )
SOURCE_BUTTONS = InlineKeyboardMarkup(
        [[
            InlineKeyboardButton('đ Back', callback_data='about'),
            InlineKeyboardButton('đ  Home', callback_data='home')
            ]]
    )
DONATE_BUTTONS = InlineKeyboardMarkup(
        [[
            InlineKeyboardButton('đ Back', callback_data='about'),
            InlineKeyboardButton('đ  Home', callback_data='home')
            ]]
    )

@StreamBot.on_callback_query()
async def cb_data(bot, update):
    if update.data == "home":
        await update.message.edit_text(
            text=START_TEXT,
            disable_web_page_preview=True,
            reply_markup=START_BUTTONS
        )
    elif update.data == "help":
        await update.message.edit_text(
            text=HELP_TEXT,
            disable_web_page_preview=True,
            reply_markup=HELP_BUTTONS
         )
    elif update.data == "howtouseme":
       await update.message.edit_text(
            text=HOWTOUSEME_TEXT,
            disable_web_page_preview=True,
            reply_markup=HOWTOUSEME_BUTTONS
        )
    elif update.data == "instructions":
        await update.message.edit_text(
            text=INSTRUCTIONS_TEXT,
            disable_web_page_preview=True,
            reply_markup=INSTRUCTIONS_BUTTONS
        )
    elif update.data == "about":
        await update.message.edit_text(
            text=ABOUT_TEXT,
            disable_web_page_preview=True,
            reply_markup=ABOUT_BUTTONS
        )
    elif update.data == "tutorials":
        await update.message.edit_text(
            text=TUTORIALS_TEXT,
            disable_web_page_preview=True,
            reply_markup=TUTORIALS_BUTTONS
        )
    elif update.data == "rating":
        await update.message.edit_text(
            text=RATING_TEXT,
            disable_web_page_preview=True,
            reply_markup=RATING_BUTTONS
        )
    elif update.data == "source":
        await update.message.edit_text(
            text=SOURCE_TEXT,
            disable_web_page_preview=True,
            reply_markup=SOURCE_BUTTONS
        )
    elif update.data == "donate":
        await update.message.edit_text(
            text=DONATE_TEXT,
            disable_web_page_preview=True,
            reply_markup=DONATE_BUTTONS
        )
        
@StreamBot.on_message(filters.command('start'))
async def command(b, m:Message):
    await m.reply_text(
        text="""đ <b>Hello</b>,

đ¤ My Name is Hagadmansa Mega Bot, I can stream Telegram Files over HTTP.

đ§ Don't know how to do? No worries, just press the help button.

đ¨âđģ My Creator is <a href=https://t.me/hagadmansa>Hagadmansa</a>.""",
        reply_markup=InlineKeyboardMarkup
        ([[
            InlineKeyboardButton('đ Website', url='https://hagadmansa.com'),
            InlineKeyboardButton('đŖ Updates', url='https://t.me/hagadmansa')
            ],[
            InlineKeyboardButton('âšī¸ Help', callback_data='help'),
            InlineKeyboardButton('đ About', callback_data='about')
        ]]),
        disable_web_page_preview=True,
    )
     
