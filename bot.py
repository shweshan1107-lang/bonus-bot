import os
from dotenv import load_dotenv
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup, InputMediaPhoto
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, MessageHandler, ContextTypes, filters

load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")

BONUS_TEXT = """Bonus Time!

━━━━━━━━━━━━
🎉 ကြိုက်နှစ်သက်ရာ gameအားရွှေးချယ်ဆော့ကစားနိုင်ပါသည်။ 🎉
━━━━━━━━━━━━
"""
CONTACT_TEXT = """⏱️ 24 နာရီအချိန်မရွေးဝန်ဆောင်မှုဖြစ်လို့ 
အသေးစိတ် သိရှိလိုပါက ☎️Viber / ☎️Telegram တိုမှာ 
ဆက်သွယ်မေးမြန်းနိုင်တယ်နော်။

💌 Ngwe99 MM
✅ အလျော်အစားမှန်ကန်ပြီး ဆာဗာထိန်းချုပ်မှုလုံးဝမရှိ ၊ ငွေကြေးအာမခံချက် ၁၀၀% အပြည့် 
   မြန်မာ့ နံပါတ် ၁ တိုက်ရိုက်ဂိမ်းဝက်ဆိုက်ကြီး
   
👇🏻အက်မင်များထံသိုဆက်သွယ်ရန်အောက်ကခလုတ်တွေကိုနှိပ်လိုက်နော်။"""

HELP_TEXT = "☎️ အကောင့်အကူအညီလိုအပ်ပါက admin ကိုဆက်သွယ်ပါ။"

HOME_TEXT = "🏠 Main Menu"

PROVIDER_CARDS = {
    "pg": [
        {"image": "pg1.jpg", "caption": "PG Soft ငွေထုတ်အများဆုံး ဂိမ်း 5ခု — 1/5", "button_text": "💎 ယခုကစားမည်", "button_url": "https://ngwe99.co/"},
        {"image": "pg2.jpg", "caption": "PG Soft ငွေထုတ်အများဆုံး ဂိမ်း 5ခု — 2/5", "button_text": "💎 ယခုကစားမည်", "button_url": "https://ngwe99.co/"},
        {"image": "pg3.jpg", "caption": "PG Soft ငွေထုတ်အများဆုံး ဂိမ်း 5ခု — 3/5", "button_text": "💎 ယခုကစားမည်", "button_url": "https://ngwe99.co/"},
        {"image": "pg4.jpg", "caption": "PG Soft ငွေထုတ်အများဆုံး ဂိမ်း 5ခု — 4/5", "button_text": "💎 ယခုကစားမည်", "button_url": "https://ngwe99.co/"},
        {"image": "pg5.jpg", "caption": "PG Soft ငွေထုတ်အများဆုံး ဂိမ်း 5ခု — 5/5", "button_text": "💎 ယခုကစားမည်", "button_url": "https://ngwe99.co/"},
    ],

    "joker": [
        {"image": "joker1.jpg", "caption": "Joker ငွေထုတ်အများဆုံး ဂိမ်း 5ခု — 1/5", "button_text": "💎 ယခုကစားမည်", "button_url": "https://ngwe99.co/"},
        {"image": "joker2.jpg", "caption": "Joker ငွေထုတ်အများဆုံး ဂိမ်း 5ခု — 2/5", "button_text": "💎 ယခုကစားမည်", "button_url": "https://ngwe99.co/"},
        {"image": "joker3.jpg", "caption": "Joker ငွေထုတ်အများဆုံး ဂိမ်း 5ခု — 3/5", "button_text": "💎 ယခုကစားမည်", "button_url": "https://ngwe99.co/"},
        {"image": "joker4.jpg", "caption": "Joker ငွေထုတ်အများဆုံး ဂိမ်း 5ခု — 4/5", "button_text": "💎 ယခုကစားမည်", "button_url": "https://ngwe99.co/"},
        {"image": "joker5.jpg", "caption": "Joker ငွေထုတ်အများဆုံး ဂိမ်း 5ခု — 5/5", "button_text": "💎 ယခုကစားမည်", "button_url": "https://ngwe99.co/"},
    ],

    "jili": [
        {"image": "jili1.jpg", "caption": "JILI ငွေထုတ်အများဆုံး ဂိမ်း 5ခု — 1/5", "button_text": "💎 ယခုကစားမည်", "button_url": "https://ngwe99.co/"},
        {"image": "jili2.jpg", "caption": "JILI ငွေထုတ်အများဆုံး ဂိမ်း 5ခု — 2/5", "button_text": "💎 ယခုကစားမည်", "button_url": "https://ngwe99.co/"},
        {"image": "jili3.jpg", "caption": "JILI ငွေထုတ်အများဆုံး ဂိမ်း 5ခု — 3/5", "button_text": "💎 ယခုကစားမည်", "button_url": "https://ngwe99.co/"},
        {"image": "jili4.jpg", "caption": "JILI ငွေထုတ်အများဆုံး ဂိမ်း 5ခု — 4/5", "button_text": "💎 ယခုကစားမည်", "button_url": "https://ngwe99.co/"},
        {"image": "jili5.jpg", "caption": "JILI ငွေထုတ်အများဆုံး ဂိမ်း 5ခု — 5/5", "button_text": "💎 ယခုကစားမည်", "button_url": "https://ngwe99.co/"},
    ],

    "pp": [
        {"image": "pp1.jpg", "caption": "PP ငွေထုတ်အများဆုံး ဂိမ်း 5ခု — 1/5", "button_text": "💎 ယခုကစားမည်", "button_url": "https://ngwe99.co/"},
        {"image": "pp2.jpg", "caption": "PP ငွေထုတ်အများဆုံး ဂိမ်း 5ခု — 2/5", "button_text": "💎 ယခုကစားမည်", "button_url": "https://ngwe99.co/"},
        {"image": "pp3.jpg", "caption": "PP ငွေထုတ်အများဆုံး ဂိမ်း 5ခု — 3/5", "button_text": "💎 ယခုကစားမည်", "button_url": "https://ngwe99.co/"},
        {"image": "pp4.jpg", "caption": "PP ငွေထုတ်အများဆုံး ဂိမ်း 5ခု — 4/5", "button_text": "💎 ယခုကစားမည်", "button_url": "https://ngwe99.co/"},
        {"image": "pp5.jpg", "caption": "PP ငွေထုတ်အများဆုံး ဂိမ်း 5ခု — 5/5", "button_text": "💎 ယခုကစားမည်", "button_url": "https://ngwe99.co/"},
    ],

    "jdb": [
        {"image": "jdb1.jpg", "caption": "JDB ငွေထုတ်အများဆုံး ဂိမ်း 5ခု — 1/5", "button_text": "💎 ယခုကစားမည်", "button_url": "https://ngwe99.co/"},
        {"image": "jdb2.jpg", "caption": "JDB ငွေထုတ်အများဆုံး ဂိမ်း 5ခု — 2/5", "button_text": "💎 ယခုကစားမည်", "button_url": "https://ngwe99.co/"},
        {"image": "jdb3.jpg", "caption": "JDB ငွေထုတ်အများဆုံး ဂိမ်း 5ခု — 3/5", "button_text": "💎 ယခုကစားမည်", "button_url": "https://ngwe99.co/"},
        {"image": "jdb4.jpg", "caption": "JDB ငွေထုတ်အများဆုံး ဂိမ်း 5ခု — 4/5", "button_text": "💎 ယခုကစားမည်", "button_url": "https://ngwe99.co/"},
        {"image": "jdb5.jpg", "caption": "JDB ငွေထုတ်အများဆုံး ဂိမ်း 5ခု — 5/5", "button_text": "💎 ယခုကစားမည်", "button_url": "https://ngwe99.co/"},
    ],

    "askbet": [
        {"image": "ask1.jpg", "caption": "ASK BET ငွေထုတ်အများဆုံး ဂိမ်း 5ခု — 1/5", "button_text": "💎 ယခုကစားမည်", "button_url": "https://ngwe99.co/"},
        {"image": "ask2.jpg", "caption": "ASK BET ငွေထုတ်အများဆုံး ဂိမ်း 5ခု — 2/5", "button_text": "💎 ယခုကစားမည်", "button_url": "https://ngwe99.co/"},
        {"image": "ask3.jpg", "caption": "ASK BET ငွေထုတ်အများဆုံး ဂိမ်း 5ခု — 3/5", "button_text": "💎 ယခုကစားမည်", "button_url": "https://ngwe99.co/"},
        {"image": "ask4.jpg", "caption": "ASK BET ငွေထုတ်အများဆုံး ဂိမ်း 5ခု — 4/5", "button_text": "💎 ယခုကစားမည်", "button_url": "https://ngwe99.co/"},
        {"image": "ask5.jpg", "caption": "ASK BET ငွေထုတ်အများဆုံး ဂိမ်း 5ခု — 5/5", "button_text": "💎 ယခုကစားမည်", "button_url": "https://ngwe99.co/"},
    ],

    "micro": [
        {"image": "mcr1.jpg", "caption": "Microgaming ငွေထုတ်အများဆုံး ဂိမ်း 5ခု — 1/5", "button_text": "💎 ယခုကစားမည်", "button_url": "https://ngwe99.co/"},
        {"image": "mcr2.jpg", "caption": "Microgaming ငွေထုတ်အများဆုံး ဂိမ်း 5ခု — 2/5", "button_text": "💎 ယခုကစားမည်", "button_url": "https://ngwe99.co/"},
        {"image": "mcr3.jpg", "caption": "Microgaming ငွေထုတ်အများဆုံး ဂိမ်း 5ခု — 3/5", "button_text": "💎 ယခုကစားမည်", "button_url": "https://ngwe99.co/"},
        {"image": "mcr4.jpg", "caption": "Microgaming ငွေထုတ်အများဆုံး ဂိမ်း 5ခု — 4/5", "button_text": "💎 ယခုကစားမည်", "button_url": "https://ngwe99.co/"},
        {"image": "mcr5.jpg", "caption": "Microgaming ငွေထုတ်အများဆုံး ဂိမ်း 5ခု — 5/5", "button_text": "💎 ယခုကစားမည်", "button_url": "https://ngwe99.co/"},
    ],

    "live22": [
        {"image": "live1.jpg", "caption": "Live 22 ငွေထုတ်အများဆုံး ဂိမ်း 5ခု — 1/5", "button_text": "💎 ယခုကစားမည်", "button_url": "https://ngwe99.co/"},
        {"image": "live2.jpg", "caption": "Live 22 ငွေထုတ်အများဆုံး ဂိမ်း 5ခု — 2/5", "button_text": "💎 ယခုကစားမည်", "button_url": "https://ngwe99.co/"},
        {"image": "live3.jpg", "caption": "Live 22 ငွေထုတ်အများဆုံး ဂိမ်း 5ခု — 3/5", "button_text": "💎 ယခုကစားမည်", "button_url": "https://ngwe99.co/"},
        {"image": "live4.jpg", "caption": "Live 22 ငွေထုတ်အများဆုံး ဂိမ်း 5ခု — 4/5", "button_text": "💎 ယခုကစားမည်", "button_url": "https://ngwe99.co/"},
        {"image": "live5.jpg", "caption": "Live 22 ငွေထုတ်အများဆုံး ဂိမ်း 5ခု — 5/5", "button_text": "💎 ယခုကစားမည်", "button_url": "https://ngwe99.co/"},
    ],

    "bng": [
        {"image": "bng1.jpg", "caption": "BNG ငွေထုတ်အများဆုံး ဂိမ်း 5ခု — 1/5", "button_text": "💎 ယခုကစားမည်", "button_url": "https://ngwe99.co/"},
        {"image": "bng2.jpg", "caption": "BNG ငွေထုတ်အများဆုံး ဂိမ်း 5ခု — 2/5", "button_text": "💎 ယခုကစားမည်", "button_url": "https://ngwe99.co/"},
        {"image": "bng3.jpg", "caption": "BNG ငွေထုတ်အများဆုံး ဂိမ်း 5ခု — 3/5", "button_text": "💎 ယခုကစားမည်", "button_url": "https://ngwe99.co/"},
        {"image": "bng4.jpg", "caption": "BNG ငွေထုတ်အများဆုံး ဂိမ်း 5ခု — 4/5", "button_text": "💎 ယခုကစားမည်", "button_url": "https://ngwe99.co/"},
        {"image": "bng5.jpg", "caption": "BNG ငွေထုတ်အများဆုံး ဂိမ်း 5ခု — 5/5", "button_text": "💎 ယခုကစားမည်", "button_url": "https://ngwe99.co/"},
    ],

    "kingmaker": [
        {"image": "km1.jpg", "caption": "KingMaker ငွေထုတ်အများဆုံး ဂိမ်း 5ခု — 1/5", "button_text": "💎 ယခုကစားမည်", "button_url": "https://ngwe99.co/"},
        {"image": "km2.jpg", "caption": "KingMaker ငွေထုတ်အများဆုံး ဂိမ်း 5ခု — 2/5", "button_text": "💎 ယခုကစားမည်", "button_url": "https://ngwe99.co/"},
        {"image": "km3.jpg", "caption": "KingMaker ငွေထုတ်အများဆုံး ဂိမ်း 5ခု — 3/5", "button_text": "💎 ယခုကစားမည်", "button_url": "https://ngwe99.co/"},
        {"image": "km4.jpg", "caption": "KingMaker ငွေထုတ်အများဆုံး ဂိမ်း 5ခု — 4/5", "button_text": "💎 ယခုကစားမည်", "button_url": "https://ngwe99.co/"},
        {"image": "km5.jpg", "caption": "KingMaker ငွေထုတ်အများဆုံး ဂိမ်း 5ခု — 5/5", "button_text": "💎 ယခုကစားမည်", "button_url": "https://ngwe99.co/"},
    ],
}

def main_menu_keyboard():
    return InlineKeyboardMarkup([
        [InlineKeyboardButton("🔗 လော့အင့်", url="https://www.ngwe99mm.com/login")],
        [InlineKeyboardButton("💬 Telegram ", url="https://tinyurl.com/ngwe99mmk"),
        InlineKeyboardButton("  Viber ", url="https://tinyurl.com/muffu2rx")],
        [
            InlineKeyboardButton("FACEBOOK", url="https://www.facebook.com/Ngwe99mm"),
            
        ],
       
    ])



def bottom_menu_keyboard():
    return ReplyKeyboardMarkup(
        [
            ["⏰ Bonus Time ⏰"],
            ["🏠 မူလသို့သွားမည်", "☎️ အက်မင်အားဆက်သွယ်မယ်"],
        ],
        resize_keyboard=True
    )

def contact_keyboard():
    return InlineKeyboardMarkup([
        [
            InlineKeyboardButton("💬 Telegram", url="https://t.me/ngwe99mmk"),
            InlineKeyboardButton("📱 Viber", url="https://tinyurl.com/muffu2rx"),
        ],
        [InlineKeyboardButton("🏠 Home", callback_data="home")]
    ])

def bonus_menu_keyboard(page=1):
    if page == 1:
        return InlineKeyboardMarkup([
            [InlineKeyboardButton("⏰ Bonus Time ⏰", callback_data="bonus_title")],
            [
                InlineKeyboardButton("PG Soft", callback_data="provider_pg"),
                InlineKeyboardButton("Joker", callback_data="provider_joker"),
            ],
            [
                InlineKeyboardButton("JILI", callback_data="provider_jili"),
                InlineKeyboardButton("PP", callback_data="provider_pp"),
            ],
            [
                InlineKeyboardButton("JDB", callback_data="provider_jdb"),
            ],
            [
                InlineKeyboardButton("◀", callback_data="bonus_prev"),
                InlineKeyboardButton("1/2", callback_data="bonus_page"),
                InlineKeyboardButton("▶", callback_data="bonus_next"),
            ],
            [InlineKeyboardButton("🏠 Home", callback_data="home")],
        ])
    else:
        return InlineKeyboardMarkup([
            [InlineKeyboardButton("⏰ Bonus Time ⏰", callback_data="bonus_title")],
            [
                InlineKeyboardButton("ASK BET", callback_data="provider_askbet"),
                InlineKeyboardButton("Microgaming", callback_data="provider_micro"),
            ],
            [
                InlineKeyboardButton("Live 22", callback_data="provider_live22"),
                InlineKeyboardButton("BNG", callback_data="provider_bng"),
            ],
            [
                InlineKeyboardButton("KingMaker", callback_data="provider_kingmaker"),
            ],
            [
                InlineKeyboardButton("◀", callback_data="bonus_prev"),
                InlineKeyboardButton("2/2", callback_data="bonus_page"),
                InlineKeyboardButton("▶", callback_data="bonus_next"),
            ],
            [InlineKeyboardButton("🏠 Home", callback_data="home")],
        ])

def provider_card_keyboard(provider_key, index, total, button_text, button_url):
    return InlineKeyboardMarkup([
        [InlineKeyboardButton(button_text, url=button_url)],
        [
            InlineKeyboardButton("◀", callback_data=f"card_prev:{provider_key}:{index}"),
            InlineKeyboardButton(f"{index+1}/{total}", callback_data="card_page"),
            InlineKeyboardButton("▶", callback_data=f"card_next:{provider_key}:{index}"),
        ],
        [InlineKeyboardButton("🔙 Provider List", callback_data="bonus_menu")],
        [InlineKeyboardButton("🏠 Home", callback_data="home")],
    ])


async def send_provider_card(chat_id, context, provider_key, index):
    cards = PROVIDER_CARDS[provider_key]
    card = cards[index]

    with open(card["image"], "rb") as photo:
        await context.bot.send_photo(
            chat_id=chat_id,
            photo=photo,
            caption=card["caption"],
            reply_markup=provider_card_keyboard(
                provider_key,
                index,
                len(cards),
                card["button_text"],
                card["button_url"]
            )
        )

async def edit_provider_card(query, provider_key, index):
    cards = PROVIDER_CARDS[provider_key]
    card = cards[index]

    with open(card["image"], "rb") as photo:
        await query.edit_message_media(
            media=InputMediaPhoto(
                media=photo,
                caption=card["caption"]
            ),
            reply_markup=provider_card_keyboard(
                provider_key,
                index,
                len(cards),
                card["button_text"],
                card["button_url"]
            )
        )

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    first_name = update.effective_user.first_name or "မိတ်ဆွေ"

    with open("welcome.mp4", "rb") as video:
        await update.message.reply_video(
            video=video,
            caption=f"""👋 မင်္ဂလာပါ {first_name}!

မြန်မာတို့အတွက်
မြန်မာ-ထိုင်း-မလေးရှား-ကိုရီးယား-ဂျပန် တွင်လိုင်စင် အာမခံချက်ရှိသော
ယုံကြည်စိတ်ချရသည့် ဝန်ဆောင်မှုဖြစ်ပါတယ် ✨✨✨
""",
            reply_markup=main_menu_keyboard(),
            supports_streaming=True
        )

    await update.message.reply_text(
        "အောက်က menu ကိုရွေးပါ။",
        reply_markup=bottom_menu_keyboard()
    )

async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "bonus_menu":
        try:
            await query.edit_message_caption(
                caption=BONUS_TEXT,
                reply_markup=bonus_menu_keyboard(1)
            )
        except:
            await query.edit_message_text(
                text=BONUS_TEXT,
                reply_markup=bonus_menu_keyboard(1)
            )

    elif query.data == "bonus_next":
        try:
            await query.edit_message_caption(
                caption=BONUS_TEXT,
                reply_markup=bonus_menu_keyboard(2)
            )
        except:
            await query.edit_message_text(
                text=BONUS_TEXT,
                reply_markup=bonus_menu_keyboard(2)
            )

    elif query.data == "bonus_prev":
        try:
            await query.edit_message_caption(
                caption=BONUS_TEXT,
                reply_markup=bonus_menu_keyboard(1)
            )
        except:
            await query.edit_message_text(
                text=BONUS_TEXT,
                reply_markup=bonus_menu_keyboard(1)
            )       

    elif query.data == "help":
        await query.edit_message_text(
            HELP_TEXT,
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("🏠 Home", callback_data="home")]
            ])
        )

    elif query.data == "home":
        await query.edit_message_text(
            HOME_TEXT,
            reply_markup=main_menu_keyboard()
        )

    elif query.data.startswith("provider_"):
        provider_key = query.data.replace("provider_", "")

        if provider_key in PROVIDER_CARDS:
            await query.answer()
            await send_provider_card(query.message.chat_id, context, provider_key, 0)
        else:
            await query.answer(f"{provider_key.upper()} ကို နောက်မှထည့်မယ်", show_alert=False)

    elif query.data.startswith("card_next:"):
        _, provider_key, index = query.data.split(":")
        index = int(index)

        cards = PROVIDER_CARDS[provider_key]
        new_index = index + 1
        if new_index >= len(cards):
            new_index = 0

        
        await edit_provider_card(query, provider_key, new_index)

    elif query.data.startswith("card_prev:"):
        _, provider_key, index = query.data.split(":")
        index = int(index)

        cards = PROVIDER_CARDS[provider_key]
        new_index = index - 1
        if new_index < 0:
            new_index = len(cards) - 1

        
        await edit_provider_card(query, provider_key, new_index)

async def text_menu_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    if text == "⏰ Bonus Time ⏰":
        await update.message.reply_text(
            BONUS_TEXT,
            reply_markup=bonus_menu_keyboard(1)
        )

    elif text == "🏠 မူလသို့သွားမည်":
        first_name = update.effective_user.first_name or "မိတ်ဆွေ"

        with open("welcome.mp4", "rb") as video:
            await update.message.reply_video(
                video=video,
                caption=f"""👋 မင်္ဂလာပါ {first_name}!

မြန်မာတို့အတွက်
မြန်မာ-ထိုင်း-မလေးရှား-ကိုရီးယား-ဂျပန် တွင်လိုင်စင် အာမခံချက်ရှိသော
ယုံကြည်စိတ်ချရသည့် ဝန်ဆောင်မှုဖြစ်ပါတယ် ✨✨✨
""",
                reply_markup=main_menu_keyboard(),
                supports_streaming=True
            )

        await update.message.reply_text(
            "အောက်က menu ကိုရွေးပါ။",
            reply_markup=bottom_menu_keyboard()
        )

    elif text == "☎️ အက်မင်အားဆက်သွယ်မယ်":
        with open("contact.mp4", "rb") as video:
            await update.message.reply_video(
                video=video,
                caption=CONTACT_TEXT,
                reply_markup=contact_keyboard()
            )    


def main():
    if not BOT_TOKEN:
        print("BOT_TOKEN not found in .env")
        return

    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_handler))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, text_menu_handler))

    print("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()