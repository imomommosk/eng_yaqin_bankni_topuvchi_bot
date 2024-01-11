from aiogram import types
from aiogram.dispatcher.filters import Command
from aiogram.types import InputFile
from keyboards.inline.location_button import location_keys
from loader import dp, bot

@dp.message_handler(content_types=types.ContentType.PHOTO)
async def getfileidPhoto(message: types.Message):
    await message.reply(message.photo[-1].file_id)

@dp.message_handler(Command("bank"))
async def send_test(message: types.Message):
    photo_id="AgACAgIAAxkBAAMwZZ_PxrXWfsRdGZtkKvSgEtU4egQAAvfUMRuEHQABSWAOe7bpb4vRAQADAgADbQADNAQ"
    msg = "<b>Bank</b>"

    await message.reply_photo(photo_id, caption=msg, reply_markup=location_keys)