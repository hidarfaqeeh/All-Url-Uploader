# MIT License

# Copyright (c) 2022 Hash Minner

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton


class Translation(object):

    START_TEXT = """
▪︎مرحبا ياسيدي  {} 

أنا بوت تحميل الملفات من الروابط
فقط قم بارسال لي أي رابط ملف أو اي فديو مباشر وسأقوم بإرساله لك هنا 
 
"""

    HELP_TEXT = """

# ارسل للبوت أي رابط ملف مباشر او فديو او يوتيوب وغيره  | ytdl | direct links.

# بعدين اختيار للصيغه الي تشتي البوت يرسل لك بها الملف.

# ارتاح قليل لحد ما احمل لك الملف المطلوب ..
 
"""

# give credit to developer

    ABOUT_TEXT = """
<b>♻️ اسم البوت</b> : بوت تحميل  الملفات  من الروابط

<b>🌀 قناة البوت </b> : <a href="https://t.me/yebotats">@yebotats</a>

<b>🌺 Heruko </b> : <a href="https://heroku.com/">Heroku</a>

<b>📑 لغة البوت  :</b> <a href="https://www.python.org/">Python 3.10.5</a>

<b> حمزة البوت :</b> <a href="https://docs.pyrogram.org/">Pyrogram 2.0.30</a>

<b>👲 مطور البوت  :</b> <a href="https://t.me/AKM100YE">@AKM100YE</a>


"""

    PROGRESS = """
🔰 سرعة التحميل : {3}/s\n\n
🌀 تم تحميل  : {1}\n\n
🎥 الحجم الكلي   : {2}\n\n
⏳ المتبقي  : {4}\n\n
"""
    ID_TEXT = """
🆔 Your Telegram ID 𝐢𝐬 :- <code>{}</code>
"""

    INFO_TEXT = """

 🤹 First Name : <b>{}</b>

 🚴‍♂️ Second Name : <b>{}</b>

 🧑🏻‍🎓 Username : <b>@{}</b>

 🆔 Telegram Id : <code>{}</code>

 📇 Profile Link : <b>{}</b>

 📡 Dc : <b>{}</b>

 📑 Language : <b>{}</b>

 👲 Status : <b>{}</b>
"""

    START_BUTTONS = InlineKeyboardMarkup(
        [[
            InlineKeyboardButton('❓ مساعدة', callback_data='help'),
            InlineKeyboardButton('🦊 حول البوت', callback_data='about')
        ], [
            InlineKeyboardButton('📛 اغلاق القائمة', callback_data='close')
        ]]
    )
    HELP_BUTTONS = InlineKeyboardMarkup(
        [[
            InlineKeyboardButton('🏠 الرئيسية', callback_data='home'),
            InlineKeyboardButton('🦊 حول البوت', callback_data='about')
        ], [
            InlineKeyboardButton('📛 اغلاق القائمة', callback_data='close')
        ]]
    )
    ABOUT_BUTTONS = InlineKeyboardMarkup(
        [[
            InlineKeyboardButton('🏠 الرئيسية', callback_data='home'),
            InlineKeyboardButton('❓ مساعدة', callback_data='help')
        ], [
            InlineKeyboardButton('📛 اغلاق القائمة', callback_data='close')
        ]]
    )
    BUTTONS = InlineKeyboardMarkup(
        [[
            InlineKeyboardButton('📛 اغلاق القائمة', callback_data='close')
        ]]
    )
    FORMAT_SELECTION = "اختار صيغة ودقة الملف الي تشتي احمله لك "
    SET_CUSTOM_USERNAME_PASSWORD = """"""
    DOWNLOAD_START = " بنحاول أحمله لك ياسيدي اصبر عليا شويه ⌛\n\n <i>{} </i>"
    UPLOAD_START = "<i>{} </i>\n\n📤 حملته والان بنرفعه لك  "
    RCHD_TG_API_LIMIT = "استغرق التحميل  {} ثانية .\nحجم الملف : {}\nسامحني ياسيدي ماقدرش احمل ملف حجمه اكثر من ٢ جيجا بسبب قيود شركة تلقرام ."
    AFTER_SUCCESSFUL_UPLOAD_MSG_WITH_TS = "  الوقت المستغرق للتحميل   {} ثانية .\n\nشكرا لاستخدامي \n\nالوقت المستغرق للرفع  {} ثانية"
    FF_MPEG_DEL_ETED_CUSTOM_MEDIA = "✅ Media cleared succesfully."
    CUSTOM_CAPTION_UL_FILE = " "
    NO_VOID_FORMAT_FOUND = "حدث خطأ ... <code>{}</code>"
    SLOW_URL_DECED = "اووووه هذا الرابط مبين التحميل منه بطي . واللهه مافي مزاج اجلس انتظر احمله ايش رايك:==> https://shrtz.me/PtsVnf6  وقم بتسريع الرابط وثم ارساله لي واحمله لك بسرعة ."
