from aiogram import types, Bot, Dispatcher, filters, F
import asyncio
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


bot = Bot(token="")
dp = Dispatcher(bot=bot)


class Registration(StatesGroup):
    first_name = State()
    phone_number = State()


orders = []

contact_button = types.ReplyKeyboardMarkup(keyboard=[
    [types.KeyboardButton(text="Kontakt jo'natish", request_contact=True)]
])


keyboard = [
    [KeyboardButton(text="UZ"), KeyboardButton(text="Rus")]
]
keyboards = ReplyKeyboardMarkup(keyboard=keyboard, resize_keyboard=True)

keyboard1 = [
    [KeyboardButton(text="Курс"), KeyboardButton(text="Корзинка"), KeyboardButton(text="О нас")],
    [KeyboardButton(text="Поддержка"), KeyboardButton(text="Поменять язык")]
]
keyboards1 = ReplyKeyboardMarkup(keyboard=keyboard1, resize_keyboard=True)


keyboard2 = [
    [KeyboardButton(text="Kurs"), KeyboardButton(text="Korzinka"), KeyboardButton(text="Biz haqimizda")],
    [KeyboardButton(text="Yordam"), KeyboardButton(text="Tilni o'zgartirish")]
]
keyboards3 = ReplyKeyboardMarkup(keyboard=keyboard2, resize_keyboard=True)

korzinka = [
    [KeyboardButton(text="Hammasini sotib olish"), KeyboardButton(text="Hammasini bekor qilish"), KeyboardButton(text="Ortga")]
]
korzinka1 = ReplyKeyboardMarkup(keyboard=korzinka, resize_keyboard=True)


korzinka2 = [
    [KeyboardButton(text="Купить все товары"), KeyboardButton(text="Отменить все товары"), KeyboardButton(text="Назад")]
]
korzinka3 = ReplyKeyboardMarkup(keyboard=korzinka2, resize_keyboard=True)

kurs = [
    [KeyboardButton(text="backend"), KeyboardButton(text="frontend"), KeyboardButton(text="python")],
    [KeyboardButton(text="html"), KeyboardButton(text="C++"), KeyboardButton(text="Sql"), KeyboardButton(text="Ortga")]
]
kurs1 = ReplyKeyboardMarkup(keyboard=kurs, resize_keyboard=True)


sale = [
    [KeyboardButton(text="Купить"), KeyboardButton(text="Отменить")]
]
sale1 = ReplyKeyboardMarkup(keyboard=sale, resize_keyboard=True)


inline_keyboard = [
    [InlineKeyboardButton(text="Краткое видео компании",  url="https://youtu.be/-euDGRWywc0?si=cUbzDg_-SjJhYHMb"), InlineKeyboardButton(text="Второй сайт компании", url="https://openai.com/index/chatgpt/")]
]
inline_keyboards = InlineKeyboardMarkup(inline_keyboard=inline_keyboard)

inline_keyboard1 = [
    [InlineKeyboardButton(text="Kompaniya haqida qisqacha video",  url="https://youtu.be/-euDGRWywc0?si=cUbzDg_-SjJhYHMb"), InlineKeyboardButton(text="Ikkinchi kompaniya veb-sayti", url="https://openai.com/index/chatgpt/")]
]
inline_keyboards2 = InlineKeyboardMarkup(inline_keyboard=inline_keyboard1)


@dp.message(filters.Command("start"))
async def start_function(message: types.Message, state: FSMContext):
    await state.set_state(Registration.first_name)
    await message.answer("Xush kelibsiz Ismingizni kiriting")


@dp.message(Registration.first_name)
async def first_name_function(message: types.Message, state: FSMContext):
    await state.update_data(first_name=message.text)
    await state.set_state(Registration.phone_number)
    await message.answer("Endi raqamni kiriting", reply_markup=contact_button)


@dp.message(Registration.phone_number)
async def phone_number_function(message: types.Message, state: FSMContext):
    await state.update_data(phone_number=message.contact.phone_number)
    data = await state.get_data()
    await message.answer(f"O'xshadi {data}", reply_markup=keyboards)
    await state.clear()


@dp.message(F.text == "Tilni o'zgartirish")
async def language_function(message: types.Message):
    await message.answer("Tilni o'zgartirish", reply_markup=keyboards)


@dp.message(F.text == "Поменять язык")
async def language_function(message: types.Message):
    await message.answer("Поменять язык", reply_markup=keyboards)


@dp.message(F.text == "Поддержка")
async def start_function(message: types.Message):
    await message.answer(text="https://chatgpt.com/")


@dp.message(F.text == "Yordam")
async def start_function(message: types.Message):
    await message.answer(text="https://chatgpt.com/")


@dp.message(F.text == "UZ")
async def start_function(message: types.Message):
    await message.answer(text="Uzbek tilini tanladingiz", reply_markup=keyboards3)


@dp.message(F.text == "Rus")
async def start_function(message: types.Message):
    await message.answer(text="Вы выбрали русский язык", reply_markup=keyboards1)


@dp.message(F.text == "Korzinka")
async def start_function(message: types.Message):
    await message.answer(text=f"{orders}", reply_markup=korzinka1)


@dp.message(F.text == "Hammasini bekor qilish")
async def start_function(message: types.Message):
    await message.answer(text="Hammasini bekor qilish")
    orders.clear()


@dp.message(F.text == "Отменить все товары")
async def start_function(message: types.Message):
    await message.answer(text="Вы отменили все товары")
    orders.clear()


@dp.message(F.text == "Ortga")
async def start_function(message: types.Message):
    await message.answer(text="Ortga qaytingiz", reply_markup=keyboards3)


@dp.message(F.text == "Назад")
async def start_function(message: types.Message):
    await message.answer(text="Вы вернулись назад", reply_markup=keyboards1)


@dp.message(F.text == "Корзинка")
async def start_function(message: types.Message):
    await message.answer(text=f"Корзинка {orders}", reply_markup=korzinka3)


@dp.message(F.text == "Kurs")
async def start_function(message: types.Message):
    await message.answer(text="Kurs", reply_markup=kurs1)


@dp.message(F.text == "Курс")
async def start_function(message: types.Message):
    await message.answer(text="Курс", reply_markup=kurs1)


@dp.message(F.text == "backend")
async def start_function(message: types.Message):
    photo = "https://media.licdn.com/dms/image/D4D12AQFnxb2cyB4ExQ/article-cover_image-shrink_600_2000/0/1669297731190?e=2147483647&v=beta&t=T2lOnIsN3NmSEfGUmWqxYnUvk53zOGf-vJac7g-hqCc"
    await message.answer_photo(photo=photo, caption="Dasturiy taʼminot muhandisligida frontend va backend yoki back-end deb ataladi. Ushbu atamalar dasturiy taʼminotning taqdimot qatlami (frontend) va maʼlumotlarga kirish qatlami (backend) oʻrtasidagi farqlarni ajratishni anglatadigan apparat. Server modelida tashqi koʻrinish odatda frontend hisoblanadi va frontendning oʻzida baʼzi taqdimot ishlari amalga oshirilgan boʻlsa ham, backend hisoblanadi.", reply_markup=sale1)
    orders.append("backend")


@dp.message(F.text == "frontend")
async def start_function(message: types.Message):
    photo = "https://media.licdn.com/dms/image/D4D12AQGrErXUNFk7tQ/article-cover_image-shrink_720_1280/0/1694683835221?e=2147483647&v=beta&t=Fe_sr929dOOHtJKof_kFmfkfpeWzHdD5-6nr_rwPkjI"
    await message.answer_photo(photo=photo, caption="Frontend (ing. front end, frontend) - veb-ilovalar, axborot yoki dasturiy tizimlarning taqdimot qismi, uning foydalanuvchi interfeysi va tegishli komponentlar; tizimning asosiy qismiga, uning ichki amalga oshirilishiga nisbatan ishlatiladi, bu holda backend deb ataladi", reply_markup=sale1)
    orders.append("frontend")


@dp.message(F.text == "python")
async def start_function(message: types.Message):
    photo = "https://devblogs.microsoft.com/python/wp-content/uploads/sites/12/2018/08/pythonfeature.png"
    await message.answer_photo(photo=photo, caption="Python yuqori darajadagi, umumiy maqsadli dasturlash tilidir. Uning dizayn falsafasi muhim chekinish yordamida kodning o'qilishiga urg'u beradi.", reply_markup=sale1)
    orders.append("python")


@dp.message(F.text == "html")
async def start_function(message: types.Message):
    photo = "https://www.cnet.com/a/img/resize/b9b09bd80b3129a6a5da79d9bd17487b977c9677/hub/2014/10/27/40194e6e-2544-419e-a340-f7c17b2e83c5/html5-wow-image-w3c.jpg?auto=webp&width=768"
    await message.answer_photo(photo=photo, caption="HTML (ingliz tilidan HyperText Markup Language - gipermatnni belgilash tili brauzerda veb-sahifalarni ko'rish uchun hujjatlar uchun standartlashtirilgan gipermatn belgilash tilidir. Veb-brauzerlar HTTP/HTTPS protokollari orqali serverdan HTML hujjatini oladi yoki uni mahalliy diskdan ochadi, so'ngra kodni monitor ekranida ko'rsatiladigan interfeysga talqin qiladi., reply_markup=sale1", reply_markup=sale1)
    orders.append("html")


@dp.message(F.text == "C++")
async def start_function(message: types.Message):
    photo = "https://media.geeksforgeeks.org/wp-content/cdn-uploads/20230703144619/CPP-Language.png"
    await message.answer_photo(photo=photo, caption="C++ (talaffuzi c-plus-plus[2][3] kompilyatsiya qilingan statik tarzda terilgan umumiy maqsadli dasturlash tilidir.", reply_markup=sale1)
    orders.append("C++")


@dp.message(F.text == "Sql")
async def start_function(message: types.Message):
    photo = "https://upload.wikimedia.org/wikipedia/commons/8/87/Sql_data_base_with_logo.png"
    await message.answer_photo(photo=photo, caption="SQL (IPA: [ˈɛsˈkjuˈɛl]; ingliz tilidan qisqartma. Structured Query Language – “structured query Language” – “structured query Language”) tegishli maʼlumotlar bazasini boshqarish tizimi tomonidan boshqariladigan relyatsion maʼlumotlar bazasidagi maʼlumotlarni yaratish, oʻzgartirish va boshqarish uchun ishlatiladigan deklarativ dasturlash tilidir.", reply_markup=sale1)
    orders.append("Sql")


@dp.message(F.text == "Отменить")
async def start_function(message: types.Message):
    await message.answer(text="Вы отменили товар", reply_markup=kurs1)
    orders.pop()


@dp.message(F.text == "Bekor qilish")
async def start_function(message: types.Message):
    await message.answer(text="Siz bu tovarni bekor qildingiz", reply_markup=kurs1)
    orders.pop()


@dp.message(F.text == "Sotib olish")
async def start_function(message: types.Message):
    await message.answer(text="Siz bu tovarni sotib oldingiz", reply_markup=kurs1)


@dp.message(F.text == "Купить")
async def start_function(message: types.Message):
    await message.answer(text="Вы купили этот товар", reply_markup=kurs1)


@dp.message(F.text == "О нас")
async def start_function(message: types.Message):
    photo = "https://www.webfx.com/wp-content/uploads/2023/07/what-is-openai.png"
    await message.answer_photo(photo=photo, caption="Мы обучили модель ChatGPT, которая взаимодействует в диалоговом режиме. Формат диалога позволяет ChatGPT отвечать на дополнительные вопросы, признавать свои ошибки, оспаривать неверные предпосылки и отклонять неуместные запросы.", reply_markup=inline_keyboards)


@dp.message(F.text == "Biz haqimizda")
async def start_function(message: types.Message):
    photo = "https://www.webfx.com/wp-content/uploads/2023/07/what-is-openai.png"
    await message.answer_photo(photo=photo, caption="Biz suhbat tarzida o'zaro aloqada bo'lgan ChatGPT nomli modelni o'rgatganmiz. Dialog formati ChatGPT-ga keyingi savollarga javob berish, xatolarini tan olish, noto'g'ri binolarga e'tiroz bildirish va nomaqbul so'rovlarni rad etish imkonini beradi.", reply_markup=inline_keyboards2)


async def main():
    await dp.start_polling(bot)


if __name__ == 'main':
    asyncio.run(main())
