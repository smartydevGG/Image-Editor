# By @TroJanzHEX
import pyrogram
from pyrogram import Client 
from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup,InlineKeyboardButton
from script import script


@Client.on_message(filters.command(["start"]) & filters.private)
async def start(client, message):
    await message.reply_text(
        text=script.START_MSG.format(message.from_user.mention),
        disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("HELP", callback_data="help_data"),
                    InlineKeyboardButton("ABOUT", callback_data="about_data"),
                ],
                [
                    InlineKeyboardButton("SOURCE CODE", url="https://github.com/TroJanzHEX/Image-Editor")  
                ]
            ]
        ),
        reply_to_message_id=message.message_id
    )    


@Client.on_message(filters.command(["help"]) & filters.private)
async def help(client, message):
    await message.reply_text(
        text=script.HELP_MSG,
        disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("BACK", callback_data="start_data"),
                    InlineKeyboardButton("ABOUT", callback_data="about_data"),
                ],
                [
                    InlineKeyboardButton("SOURCE CODE", url="https://github.com/TroJanzHEX/Image-Editor")  
                ]
            ]
        ),
        reply_to_message_id=message.message_id
    )

@Client.on_message(filters.command(["about"]) & filters.private)
async def about(client, message):
    await message.reply_text(
        text=script.ABOUT_MSG,
        disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("BACK", callback_data="help_data"),
                    InlineKeyboardButton("START", callback_data="start_data"),
                ],
                [
                    InlineKeyboardButton("SOURCE CODE", url="https://github.com/TroJanzHEX/Image-Editor")  
                ]
            ]
        ),
        reply_to_message_id=message.message_id
    )    