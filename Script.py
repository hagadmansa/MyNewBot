class script(object):
    START_TXT = """ð Hello {},
    
ð¤ My Name is <a href=https://t.me/{}>{}</a>, I can provide you movies, Just visit my website <i><b>www.hagadmansa.com</b></i>. 

ð§ Don't know how to watch or download? No worry just <a href=https://t.me/hagadmansa/2>Click here</a> to watch a tutorial on YouTube.
    
ð¨âð» My Creator is <a href=https://t.me/himanshurastogiofficial>Himanshu Rastogi</a>."""
    HELP_TXT = """ð Hey {}
Here is the help for my commands"""
    ABOUT_TXT = """â¯ My Name: {}
â¯ Creator: <a href=https://t.me/himanshurastogiofficial>Himanshu Rastogi</a>
â¯ Library: <a href=https://pyrogram.org>Pyrogram</a>
â¯ Language: <a href=https://python.org>Python 3</a>
â¯ Database: <a href=https://mongodb.com/>MongoDB</a>
â¯ Server: <a href=https://heroku.com/>Heroku</a>
â¯ Build Status: v1.0.1 [Beta]"""
    SOURCE_TXT = """<b>âï¸NOTE:</b>
    
- Get my source code <a href=https://github.com/HagadMansa/EvaMaria>here</a>.
- Eva Maria is a open source project.

<b>ð¨âð» My Creator </b> is <a href=https://t.me/himanshurastogiofficial>Himanshu Rastogi</a>.

<b>ð¨âð» My Devoloper</b> is <a href=https://t.me/TeamEvamaria>Team Eva Maria</a>"""
    MANUELFILTER_TXT = """<b>â¹ï¸ Help</b> > Manual Filters

ð Filter is the feature were users can set automated replies for a particular keyword and EvaMaria will respond whenever a keyword is found the message.
<bâï¸NOTE:</b>

1. Your Bot should have admin privillage.
2. Only admins can add filters in a chat.
3. Alert buttons have a limit of 64 characters.

<b>ð§© Commands and Usage:</b>

â¢ /filter - add a filter in chat
â¢ /filters - list all the filters of a chat
â¢ /del - delete a specific filter in chat
â¢ /delall - delete the whole filters in a chat (chat owner only)"""
    BUTTON_TXT = """<b>â¹ï¸ Help</b> > Manual Filters > Buttons

- This Bot Supports both url and alert inline buttons.

<b>âï¸NOTE:</b>

1. Telegram will not allows you to send buttons without any content, so content is mandatory.
2. This Bot supports buttons with any telegram media type.
3. Buttons should be properly parsed as markdown format.

<b>ð URL buttons:</b>
<code>[Button Text](buttonurl:https://t.me/hagadmansa)</code>

<b>ð Alert buttons:</b>
<code>[Button Text](buttonalert:This is an alert message)</code>"""
    AUTOFILTER_TXT = """<b>â¹ï¸ Help</b> > Auto Filter

<b>âï¸NOTE:</b>

1. Make me the admin of your channel if it's private.
2. make sure that your channel does not contains camrips, porn and fake files.
3. Forward the last message to me with quotes.
 I'll add all the files in that channel to my db."""
    CONNECTION_TXT = """<b>â¹ï¸ Help</b> > Connections

- Used to connect bot to PM for managing filters 
- It helps to avoid spamming in groups.

<b>âï¸NOTE:</b>

1. Only admins can add a connection.
2. Send <code>/connect</code> for connecting me to ur PM

<b>ð§© Commands and Usage:</b>

â¢ /connect  - connect a particular chat to your PM.
â¢ /disconnect  - disconnect from a chat.
â¢ /connections - list all your connections."""
    EXTRAMOD_TXT = """<b>â¹ï¸ Help</b> > Extra Mods

<b>âï¸NOTE:</b>

- These are the extra features of This Bot.

<b>ð§© Commands and Usage:</b>

â¢ /id - get id of a specified user.
â¢ /info  - get information about a user.
â¢ /imdb  - get the film information from IMDb source.
â¢ /search  - get the film information from various sources."""
    ADMIN_TXT = """<b>â¹ï¸ Help</b> > Extra Mods > Admin

<b>âï¸NOTE:</b>

- This module only works for my admins

<b>ð§© Commands and Usage:</b>

â¢ /logs - to get log file, you can check recent errors.
â¢ /stats - to get status of all files in all databases.
â¢ /delete - to delete a specific file from database.
â¢ /users - to get list of all users and ids.
â¢ /chats - to get list of all chats and ids.
â¢ /leave  - to leave from a chat.
â¢ /disable  -  do disable a chat.
â¢ /ban  - to ban a user.
â¢ /unban  - to unban a user.
â¢ /channel - to get list of total connected channels.
â¢ /broadcast - to broadcast a message to all users."""
    STATUS_TXT = """â Total Files: {}
â Total Users: {}
â Total Chats: {}
â Used Storage: {} MiB
â Free Storage: {} MiB"""
    LOG_TEXT_G = """#NewGroup
Group = {}(<code>{}</code>)
Total Members = <code>{}</code>
Added By - {}
"""
    LOG_TEXT_P = """#NewUser
ID - <code>{}</code>
Name - {}
"""
