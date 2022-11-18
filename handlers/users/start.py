from aiogram import types

from keyboards.reply import main_btn
from loader import dp


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer(text="Hello, I'm a bot, I can help you with your health. Choose the service you need.",
                         reply_markup=main_btn)


@dp.message_handler(text='Medical consultation')
async def medical_consultation(message: types.Message):
    await message.answer(text="Medical Consultation: speak with a medical practitioner: "
                              "https://innopolis.com/resident/medicine/medical-center/")


@dp.message_handler(text='Buy medicine')
async def buy_medicine(message: types.Message):
    text = "Purchase Medication: please note all medication purchase requires medical prescription \n\n" \
           "- Pickup at the pharmacy by myself. \n" \
           "- Delivery using robot. \n" \
           "- contact the pharmacist: https://innopolis.com/resident/medicine/pharmacies/ " \
           "-OR- " \
           "https://innopolis.com/resident/medicine/pharmacy-low-price/"
    await message.answer(text=text)


@dp.message_handler(text='Talk to a psychologist')
async def talk_to_psychologist(message: types.Message):
    await message.answer(text="Speak to a Psychologist: speak with our psychologist @Elja11 ")


@dp.message_handler(text='Call on Ambulance')
async def call_on_ambulance(message: types.Message):
    await message.answer(text="Call an Ambulance: tel:+78435226671")
