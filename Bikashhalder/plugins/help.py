from Bikashhalder import BOT0,SUDO_USERS
from telethon import events, Button
from telethon.tl.custom import button
from time import time
from datetime import datetime
from Bikashhalder import CMD_HNDLR as hl
    
HELP_PIC = "https://te.legra.ph/file/860117bc941734b04265c.jpg"

BGT_Help = "π₯ π§ππ§ πΈπ£ππ  π§π’π§ π₯\n\n"
 
BGT_Help += f"π§ππ§ πΈπ£ππ π§π’π§ πππ ππ ππ¦ βͺ\n\n"

BGT_Help += f" α ππ©ππ¦ ππ¨π­ ππ¨π¦π¦ππ§π'π α\n\n"

BGT_Help += f" `$ping` - α΄Κα΄α΄α΄ α΄ΙͺΙ΄Ι’\n `$alive` - α΄Κα΄α΄α΄ Κα΄α΄ α΄ΚΙͺα΄ α΄/α΄ ΙͺΚsΙͺα΄Ι΄ ( α΄Ι΄ΚΚ 1sα΄ sα΄α΄α΄Κα΄α΄ α΄‘ΙͺΚΚ Κα΄α΄ΚΚ )\n .`$restart` - Κα΄sα΄α΄Κα΄ α΄ΚΚ Κα΄α΄s \n `$addecho` -  α΄α΄ α΄α΄α΄ α΄α΄Κα΄ \n `$rmecho` - α΄α΄ Κα΄α΄α΄α΄ α΄ α΄α΄Κα΄ \n `$addsudo` - α΄α΄ α΄α΄α΄ sα΄α΄α΄ α΄sα΄Κ α΄sΙͺΙ΄Ι’ sα΄α΄α΄ Κα΄α΄s \n\n"
 
BGT_Help += f" α ππππ―π ππ¨π¦π¦ππ§π α\n\n"

BGT_Help += f" `$leave` - α΄α΄ Κα΄α΄α΄ α΄ α΄Ι΄Κ α΄Κα΄Ι΄Ι΄α΄Κ α΄Κ Ι’Κα΄α΄α΄ \n\n"
 
BGT_Help += f" ΰΏππ₯π₯ ππ©ππ¦ ππ¨π¦π¦ππ§π ΰΏ \n\n"

BGT_Help += f" `$raid` - α΄α΄ Κα΄Ιͺα΄\n `$replyraid` - α΄α΄α΄Ιͺα΄ α΄ Κα΄α΄ΚΚ Κα΄Ιͺα΄\n `$dreplyraid` -α΄α΄-α΄α΄α΄Ιͺα΄ α΄ Κα΄α΄ΚΚ Κα΄Ιͺα΄\n `$spam` - α΄α΄  Ι΄α΄Κα΄α΄Κ sα΄α΄α΄\n `$bigspam` - α΄sα΄ α΄α΄ ΚΙͺΙ’ sα΄α΄α΄\n `$uspam` - α΄sα΄ α΄Ι΄ΚΚ α΄Ι΄ΚΙͺα΄Ιͺα΄α΄α΄ sα΄α΄α΄ α΄ α΄‘α΄Ι΄α΄ sα΄α΄α΄ sα΄α΄α΄ α΄Κα΄Ι΄ Κα΄sα΄α΄Κα΄ Κα΄α΄s!!\n `$bgtspam` - α΄ΚΙͺs sα΄α΄α΄ α΄sα΄ α΄Ι΄ΚΚ 18+ Usα΄Κ (α΄α΄ΚΙ΄)\n\n"

BGT_Help += f" `$bgtopspam` -  α΄Ι΄ΚΚ sΚα΄α΄‘ α΄ΚΙͺs Κα΄Κα΄ γ α―Ό\n\n"

BGT_Help += f"βοΈππ«πππ­π¨π«βοΈ @BikashHalder\n"

BGT_Help += f"βοΈππ«πππ­π¨π«βοΈ @AdityaHalder\n"


@BOT0.on(events.NewMessage(incoming=True, pattern=r"\%shelp(?: |$)(.*)" % hl))
async def help(event):               
    if event.sender_id in SUDO_USERS:
      await BOT0.send_file(event.chat_id,
                                  HELP_PIC,
                                  caption=BGT_Help,
                                  buttons=[
        [
        Button.url("πππ", "https://t.me/BikashGedgetsTech"),
        Button.url("ππ", "https://t.me/Kaalware")
        ] 
        ]
        )                                                         
