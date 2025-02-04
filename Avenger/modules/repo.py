from pyrogram import filters

from Avenger import app
from Avenger.core.decorators.errors import capture_err
from Avenger.utils.http import get

__MODULE__ = "Repo"
__HELP__ = "/repo - To Get My Github Repository Link " "And Support Group Link"


@app.on_message(filters.command("repo"))
@capture_err
async def repo(_, message):
    users = await get(
        "https://api.github.com/repos/TeamAvengerBot/AvengerBot/contributors"
    )
    list_of_users = "".join(
        f"**{count}.** [{user['login']}]({user['html_url']})\n"
        for count, user in enumerate(users, start=1)
    )

    text = f"""[Github](https://github.com/TeamAvengerBot/AvengerBot) | [Group](t.me/TeamAvengerSupport)
```----------------
| Contributors |
----------------```
{list_of_users}"""
    await app.send_message(
        message.chat.id, text=text, disable_web_page_preview=True
    )
