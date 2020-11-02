from datetime import datetime

from jarvis.utils import admin_cmd, sudo_cmd, edit_or_reply

def get_readable_time(seconds: int) -> str:
    count = 0
    ping_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]

    while count < 4:
        count += 1
        if count < 3:
            remainder, result = divmod(seconds, 60)
        else:
            remainder, result = divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(result))
        seconds = int(remainder)

    for x in range(len(time_list)):
        time_list[x] = str(time_list[x]) + time_suffix_list[x]
    if len(time_list) == 4:
        ping_time += time_list.pop() + ", "

    time_list.reverse()
    ping_time += ":".join(time_list)

    return ping_time


@jarvis.on(admin_cmd(pattern="ping$", outgoing=True))
@jarvis.on(sudo_cmd(pattern="ping$", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    start = datetime.now()
    end = datetime.now()
    ms = (end - start).microseconds / 1000
    await edit_or_reply(event,f"Pong! 🏓 {ms}Secs..")

@jarvis.on(admin_cmd(pattern="pong", outgoing=True))
@jarvis.on(sudo_cmd(pattern="pong", allow_sudo=True))
async def _(event):	
    if event.fwd_from:	
        return	
    await event.delete()
    start = datetime.now()
    end = datetime.now()	
    ms = (end - start).microseconds * 0.00001	
    await edit_or_reply(mone,f"Ping! 🎾 {ms}Secs..")
    
    
CMD_HELP.update(
    {
        "ping": "**Plugin : **`Ping Pong`\
        \n\n**Syntax : **`.ping`\
        \n**Function : **Shows you the ping speed of server`\
        \n\n**Syntax : **`.pong`\
        \n**Function : **Shows you the ping speed of server (Opposite Of Ping)\"
    }
)
