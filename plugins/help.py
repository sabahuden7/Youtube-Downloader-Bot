from pyrogram import Client, Filters


@Client.on_message(Filters.command(["help"]))
async def start(client, message):
    helptxt = f"Just Send Youtube Url to download Videos"
    await message.reply_text(helptxt)
