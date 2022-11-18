from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main_btn = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Medical consultation")],
    [KeyboardButton(text="Buy medicine")],
    [KeyboardButton(text="Talk to a psychologist")],
    [KeyboardButton(text="Call on Ambulance")],
], resize_keyboard=True
)
