class script(object):
    START_TXT ="""<b>Hᴇʏ {}, ɪᴍ  ᴀɴ Aᴡᴇsᴏᴍᴇ Aᴜᴛᴏ + Mᴀɴᴜᴀʟ Fɪʟᴛᴇʀ + Gʀᴏᴜᴘ Mᴀɴᴀɢᴇʀ Bᴏᴛ.
    
Aᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ ᴛᴏ sᴇᴇ ᴛʜᴇ ᴍᴀɢɪᴄ ᴏʀ ʀᴇᴀᴅ ᴍᴏʀᴇ ғʀᴏᴍ ᴛʜᴇ ᴍᴇɴᴜ ʙᴇʟᴏᴡ<b>"""
    HELP_TXT = """<b>ʜᴇʏ {}
ʜᴇʀᴇ ɪs ᴛʜᴇ ʜᴇʟᴘ ꜰᴏʀ ᴍʏ ᴇxᴛʀᴀ ғᴇᴀᴛᴜʀᴇs.</b>"""

    HELPER_TXT = """<b>ʜᴇʏ {}
ʜᴇʀᴇ ɪs ᴛʜᴇ ʜᴇʟᴘ ꜰᴏʀ ᴍʏ ᴄᴏᴍᴍᴀɴᴅs.</b>"""


# ⚠️ Please don't change our credits 𝚃𝙷𝙰𝙽𝙺𝚂 𝚃𝙾 & 𝙳𝙴𝚅 👇🏻

    ABOUT_TXT = """<b>✯ Mʏ Nᴀᴍᴇ: {}
✯ Pᴀʀᴇɴᴛ Bᴏᴛ: <a href=https://t.me/'#botusername'>#botname</a>
✯ Tᴏᴛᴀʟ Uꜱᴇʀꜱ: <code>{}</code>
✯ Tᴏᴛᴀʟ Cʜᴀᴛꜱ: <code>{}</code>"""

    MANUELFILTER_TXT = """Help: <b>Filters</b>

<b>- 𝙵𝙸𝙻𝚃𝙴𝚁 𝙸𝚂 𝚃𝙷𝙴 𝙵𝙴𝙰𝚃𝚄𝚁𝙴 𝚆𝙴𝚁𝙴 𝚄𝚂𝙴𝚁𝚂 𝙲𝙰𝙽 𝚂𝙴𝚃 𝙰𝚄𝚃𝙾𝙼𝙰𝚃𝙴𝙳 𝚁𝙴𝙿𝙻𝙸𝙴𝚂 𝙵𝙾𝚁 𝙰 𝙿𝙰𝚁𝚃𝙸𝙲𝚄𝙻𝙰𝚁 𝙺𝙴𝚈𝚆𝙾𝚁𝙳 𝙰𝙽𝙳 𝙴𝙻𝚂𝙰 𝚆𝙸𝙻𝙻 𝚁𝙴𝚂𝙿𝙾𝙽𝙳 𝚆𝙷𝙴𝙽𝙴𝚅𝙴𝚁 𝙰 𝙺𝙴𝚈𝚆𝙾𝚁𝙳 𝙸𝚂 𝙵𝙾𝚄𝙽𝙳 𝚃𝙷𝙴 𝙼𝙴𝚂𝚂𝙰𝙶𝙴</b>

<b>NOTE:</b>
<b>𝟷.𝚂𝙷𝙾𝚄𝙻𝙳 𝙷𝙰𝚅𝙴 𝙰𝙳𝙼𝙸𝙽 𝙿𝚁𝙸𝚅𝙸𝙻𝙻𝙰𝙶𝙴.
𝟸. 𝙾𝙽𝙻𝚈 𝙰𝙳𝙼𝙸𝙽𝚂 𝙲𝙰𝙽 𝙰𝙳𝙳 𝙵𝙸𝙻𝚃𝙴𝚁𝚂 𝙸𝙽 𝙰 𝙲𝙷𝙰𝚃.
𝟹. 𝙰𝙻𝙴𝚁𝚃 𝙱𝚄𝚃𝚃𝙾𝙽𝚂 𝙷𝙰𝚅𝙴 𝙰 𝙻𝙸𝙼𝙸𝚃 𝙾𝙵 𝟼𝟺 𝙲𝙷𝙰𝚁𝙰𝙲𝚃𝙴𝚁𝚂.</b>

<b>Commands and Usage:</b>
• /filter - <code>add a filter in chat</code>
• /filters - <code>list all the filters of a chat</code>
• /del - <code>delete a specific filter in chat</code>
• /delall - <code>delete the whole filters in a chat (chat owner only)</code>"""

    BUTTON_TXT = """Help: <b>Buttons</b>

<b>𝚂𝚄𝙿𝙿𝙾𝚁𝚃𝚂 𝙱𝙾𝚃𝙷 𝚄𝚁𝙻 𝙰𝙽𝙳 𝙰𝙻𝙴𝚁𝚃 𝙸𝙽𝙻𝙸𝙽𝙴 𝙱𝚄𝚃𝚃𝙾𝙽𝚂.</b>
<b>NOTE:</b>
<b>𝟷. 𝚃𝙴𝙻𝙴𝙶𝚁𝙰𝙼 𝚆𝙸𝙻𝙻 𝙽𝙾𝚃 𝙰𝙻𝙻𝙾𝚆𝚂 𝚈𝙾𝚄 𝚃𝙾 𝚂𝙴𝙽𝙳 𝙱𝚄𝚃𝚃𝙾𝙽𝚂 𝚆𝙸𝚃𝙷𝙾𝚄𝚃 𝙰𝙽𝚈 𝙲𝙾𝙽𝚃𝙴𝙽𝚃, 𝚂𝙾 𝙲𝙾𝙽𝚃𝙴𝙽𝚃 𝙸𝚂 𝙼𝙰𝙽𝙳𝙰𝚃𝙾𝚁𝚈.
𝟸. 𝚂𝚄𝙿𝙿𝙾𝚁𝚃𝚂 𝙱𝚄𝚃𝚃𝙾𝙽𝚂 𝚆𝙸𝚃𝙷 𝙰𝙽𝚈 𝚃𝙴𝙻𝙴𝙶𝚁𝙰𝙼 𝙼𝙴𝙳𝙸𝙰 𝚃𝚈𝙿𝙴.
𝟹. 𝙱𝚄𝚃𝚃𝙾𝙽𝚂 𝚂𝙷𝙾𝚄𝙻𝙳 𝙱𝙴 𝙿𝚁𝙾𝙿𝙴𝚁𝙻𝚈 𝙿𝙰𝚁𝚂𝙴𝙳 𝙰𝚂 𝙼𝙰𝚁𝙺𝙳𝙾𝚆𝙽 𝙵𝙾𝚁𝙼𝙰𝚃</b>
<b>URL buttons:</b>
<code>[Button Text](buttonurl:https://t.me/Example...)</code>

<b>Alert buttons:</b>
<code>[Button Text](buttonalert:This is an alert message)</code>"""

    AUTOFILTER_TXT = """Help: <b>Auto Filter</b>

<b>NOTE:</b>
<b>𝟷. 𝙼𝙰𝙺𝙴 𝙼𝙴 𝚃𝙷𝙴 𝙰𝙳𝙼𝙸𝙽 𝙾𝙵 𝚈𝙾𝚄𝚁 𝙲𝙷𝙰𝙽𝙽𝙴𝙻 𝙸𝙵 𝙸𝚃'𝚂 𝙿𝚁𝙸𝚅𝙰𝚃𝙴.
𝟸. 𝙼𝙰𝙺𝙴 𝚂𝚄𝚁𝙴 𝚃𝙷𝙰𝚃 𝚈𝙾𝚄𝚁 𝙲𝙷𝙰𝙽𝙽𝙴𝙻 𝙳𝙾𝙴𝚂 𝙽𝙾𝚃 𝙲𝙾𝙽𝚃𝙰𝙸𝙽𝚂 𝙲𝙰𝙼𝚁𝙸𝙿𝚂, 𝙿𝙾𝚁𝙽 𝙰𝙽𝙳 𝙵𝙰𝙺𝙴 𝙵𝙸𝙻𝙴𝚂.
𝟹. 𝙵𝙾𝚁𝚆𝙰𝚁𝙳 𝚃𝙷𝙴 𝙻𝙰𝚂𝚃 𝙼𝙴𝚂𝚂𝙰𝙶𝙴 𝚃𝙾 𝙼𝙴 𝚆𝙸𝚃𝙷 𝚀𝚄𝙾𝚃𝙴𝚂.
 𝙸'𝙻𝙻 𝙰𝙳𝙳 𝙰𝙻𝙻 𝚃𝙷𝙴 𝙵𝙸𝙻𝙴𝚂 𝙸𝙽 𝚃𝙷𝙰𝚃 𝙲𝙷𝙰𝙽𝙽𝙴𝙻 𝚃𝙾 𝙼𝚈 𝙳𝙱.</b>
<b>★ /set_template - 𝚂𝙴𝚃 𝙲𝚄𝚂𝚃𝙾𝙼 𝙸𝙼𝙳𝙱 𝚃𝙴𝙼𝙿𝙻𝙰𝚃𝙴 𝙵𝙾𝚁 𝙰𝚄𝚃𝙾 𝙵𝙸𝙻𝚃𝙴𝚁.</b>
<b>★ /get_template - 𝙶𝙴𝚃 𝙲𝚄𝚁𝚁𝙴𝙽𝚃 𝙸𝙼𝙳𝙱 𝚃𝙴𝙼𝙿𝙻𝙰𝚃𝙴 𝙾𝙵 𝙰𝚄𝚃𝙾 𝙵𝙸𝙻𝚃𝙴𝚁.</b>
<b>★ /autofilter on - 𝙴𝙽𝙰𝙱𝙻𝙴 𝙰𝚄𝚃𝙾 𝙵𝙸𝙻𝚃𝙴𝚁 𝙸𝙽 𝚃𝙷𝙴 𝙶𝚁𝙾𝚄𝙿𝚂.</b>
<b>★ /autofilter off - 𝙳𝙸𝚂𝙰𝙱𝙻𝙴𝙳 𝙰𝚄𝚃𝙾 𝙵𝙸𝙻𝚃𝙴𝚁 𝙸𝙽 𝚃𝙷𝙴 𝙶𝚁𝙾𝚄𝙿𝚂.</b>"""

    CONNECTION_TXT = """Help: <b>Connections</b>

- Used to connect bot to PM for managing filters 
- it helps to avoid spamming in groups.

<b>NOTE:</b>
1. Only admins can add a connection.
2. Send <code>/connect</code> for connecting me to ur PM

<b>Commands and Usage:</b>
• /connect  - <code>connect a particular chat to your PM</code>
• /disconnect  - <code>disconnect from a chat</code>
• /connections - <code>list all your connections</code>"""

    STATUS_TXT = """<b>📂 ᴛᴏᴛᴀʟ ғɪʟᴇs: <code>{}</code>
👤 ᴛᴏᴛᴀʟ ᴜsᴇʀs: <code>{}</code>
♻️ ᴛᴏᴛᴀʟ ᴄʜᴀᴛs: <code>{}</code>
🗃️ ᴜsᴇᴅ sᴛᴏʀᴀɢᴇ: <code>{}</code> 𝙼𝚒𝙱
🆓 ғʀᴇᴇ sᴛᴏʀᴀɢᴇ: <code>{}</code> 𝙼𝚒𝙱</b>"""

    LOG_TEXT_G = """#NewUser
 <b>᚛› 𝐆𝐫𝐨𝐮𝐩 ⪼ {a}(<code>{b}</code>)</b>
 <b>᚛› 𝐆 𝐈𝐃 ⪼ @{c}
 <b>᚛› 𝐓𝐨𝐭𝐚𝐥 𝐌𝐞𝐦𝐛𝐞𝐫𝐬 ⪼ {d}</b>
 <b>᚛› 𝐀𝐝𝐝𝐞𝐝 𝐁𝐲 ⪼ {e}</b>
 By {f}
 """

    LOG_TEXT_P = """#NewUser
ID - <code>{}</code>
Name - {}
"""
    SUR_TXT = """
<b>Hᴇʏ {}, ɪᴍ  ᴀɴ Aᴡᴇsᴏᴍᴇ Aᴜᴛᴏ + Mᴀɴᴜᴀʟ Fɪʟᴛᴇʀ + Gʀᴏᴜᴘ Mᴀɴᴀɢᴇʀ Bᴏᴛ.
    
Aᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ ᴛᴏ sᴇᴇ ᴛʜᴇ ᴍᴀɢɪᴄ ᴏʀ ʀᴇᴀᴅ ᴍᴏʀᴇ ғʀᴏᴍ ᴛʜᴇ ᴍᴇɴᴜ ʙᴇʟᴏᴡ
</b>"""
    IMDB_TEMPLATE_TXT = """
<b>🔖 ᴛɪᴛʟᴇ :<a href={url}>{title}</a>

🎭 ɢᴇɴʀᴇs : {genres}
🎖 ʀᴀᴛɪɴɢ : <a href={url}/ratings>{rating}</a> / 10 (ʙᴀsᴇᴅ ᴏɴ {votes} ᴜsᴇʀ ʀᴀᴛɪɴɢ.)

📆 ʏᴇᴀʀ : {release_date}
🗞 ʟᴀɴɢᴜᴀɢᴇ : {languages}
🌎 ᴄᴏᴜɴᴛʀʏ : {countries}

📖 sᴛᴏʀʏ : {Plot}

©{message.chat.title}</b>
"""

    RESTART_TXT = """
<b>Bᴏᴛ Rᴇsᴛᴀʀᴛᴇᴅ !</b>
"""


    MELCOW_ENG = """<b>Hᴇʟʟᴏ {} 😍, Aɴᴅ Wᴇʟᴄᴏᴍᴇ Tᴏ {} Gʀᴏᴜᴘ ❤️"""

    ALRT_TXT = """⚠️ 𝖧ᴇʏ !
    
𝖲ᴇᴀʀᴄʜ 𝖸ᴏᴜʀ 𝖮ᴡɴ 𝖥ɪʟᴇ, 
    
𝖣ᴏɴ'ᴛ 𝖢ʟɪᴄᴋ 𝖮ᴛʜᴇʀ𝗌 𝖱ᴇ𝗌ᴜʟᴛ𝗌 😬
"""

    OLD_ALRT_TXT = """𝐘𝐨𝐮 𝐚𝐫𝐞 𝐮𝐬𝐢𝐧𝐠 𝐨𝐧𝐞 𝐨𝐟 𝐦𝐲 𝐨𝐥𝐝 𝐦𝐞𝐬𝐬𝐚𝐠𝐞𝐬, 𝐩𝐥𝐞𝐚𝐬𝐞 𝐬𝐞𝐧𝐝 𝐭𝐡𝐞 𝐫𝐞𝐪𝐮𝐞𝐬𝐭 𝐚𝐠𝐚𝐢𝐧"""

    TOP_ALRT_MSG = """♻️ ᴄʜᴇᴄᴋɪɴɢ ꜰɪʟᴇ ᴏɴ ᴍʏ ᴅᴀᴛᴀʙᴀꜱᴇ... ♻️"""

    MVE_NT_FND = """<b>𝚃𝙷𝙸𝚂 𝙼𝙾𝚅𝙸𝙴 I𝚂 𝙽𝙾𝚃 𝚈𝙴𝚃 𝚁𝙴𝙻𝙴𝙰𝚂𝙴𝙳 𝙾𝚁 𝙰𝙳𝙳𝙴𝙳 𝚃𝙾 𝙳𝙰𝚃𝚂𝙱𝙰𝚂𝙴</b> """

    NORSLTS = """★ #𝗡𝗼𝗥𝗲𝘀𝘂𝗹𝘁𝘀 ★
𝗜𝗗 <b>: {}</b>
𝗡𝗮𝗺𝗲 <b>: {}</b>
𝗠𝗲𝘀𝘀𝗮𝗴𝗲 <b>: {}</b>"""

    I_CUDNT = """ʜᴇʟʟᴏ {}, ɪ ᴄᴏᴜʟᴅɴ'ᴛ ꜰɪɴᴅ ᴀɴʏ ᴍᴏᴠɪᴇ ɪɴ ᴛʜᴀᴛ ɴᴀᴍᴇ​"""

    I_CUD_NT = """ʜᴇʟʟᴏ {}, ɪ ᴄᴏᴜʟᴅɴ'ᴛ ꜰɪɴᴅ ᴀɴʏᴛʜɪɴɢ​ ʀᴇʟᴀᴛᴇᴅ ᴛᴏ ᴛʜᴀᴛ . ᴄʜᴇᴄᴋ ʏᴏᴜʀ sᴘᴇʟʟɪɴɢ​"""
    
    CUDNT_FND = """ʜᴇʟʟᴏ {}, ɪ ᴄᴏᴜʟᴅɴ'ᴛ ꜰɪɴᴅ ᴀɴʏᴛʜɪɴɢ​ ʀᴇʟᴀᴛᴇᴅ ᴛᴏ ᴛʜᴀᴛ. ᴅɪᴅ ʏᴏᴜ ᴍᴇᴀɴ ᴀɴʏ ᴏɴᴇ ᴏꜰ ᴛʜᴇsᴇ?​"""
    
    REPRT_MSG = """ Reported To Admin"""

    CON_TXT = """<b><u>ᴄᴏᴜɴᴛʀʏ ɪɴғᴏ</b></u>
<b>Tʜɪs ᴍᴏᴅᴜʟᴇ ɪs ᴛᴏ ғɪɴᴅ ɪɴғᴏʀᴍᴀᴛɪᴏɴ ᴀʙᴏᴜᴛ ᴄᴏᴜɴᴛʀɪᴇs</b>
• /country [𝖼𝗈𝗎𝗇𝗍𝗋𝗒 𝗇𝖺𝗆𝖾] 
𝖤𝗑𝖺𝗆𝗉𝗅𝖾 :- <code>/country India</code>"""

    FIlTERS_TXT = """
<b>ʜᴇʏ,
Tʜᴇsᴇ ᴀʀᴇ ᴍʏ ᴛʜʀᴇᴇ ᴛʏᴘᴇs ᴏғ ғɪʟᴛᴇʀs.</b>"""
