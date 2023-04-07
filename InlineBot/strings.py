# Copyright (C) @CodeXBotz - All Rights Reserved
# Licensed under GNU General Public License as published by the Free Software Foundation
# Written by Shahsad Kolathur <shahsadkpklr@gmail.com>, June 2021

from pyrogram import __version__
from InlineBot import (
    OWNER_ID,
    FILTER_COMMAND,
    DELETE_COMMAND,
    CUSTOM_START_MESSAGE
)

if CUSTOM_START_MESSAGE:
    START_MESSAGE = CUSTOM_START_MESSAGE
else:
    START_MESSAGE = """<b>PLUGIN TAMBAHAN UNI</b> 
"""

HELP_MESSAGE = f"""<b><u>Main Available Commands</u></b>

○ <b>/{FILTER_COMMAND.lower()}</b> <i>[kata kunci] [pesan atau balas pesan]</i>
     <i>Tambahkan filter Inline, Anda dapat menggunakan MarkDown untuk pemformatan</i>
    
○ <b>/{DELETE_COMMAND.lower()}</b> <i>[kata kunci]</i>
     <i>Hapus Filter yang ada</i>
    
○ <b>/filter</b>
     <i>Untuk melihat filter</i>
    
○ <b>/ekspor</b>
     <i>Ekspor file Cadangan filter, ini dapat diimpor oleh orang lain</i>
    
○ <b>/stats</b>
     <i>Lihat Statistik Bot</i>
    
○ <b>/broadcast</b> <i>[membalas pesan apa pun]</i>
     <i>Siarkan Pesan apa pun ke pengguna Bot</i>
    
<b><u>Perintah khusus pemilik</u></b>

○ <b>/dell</b>
     <i>Hapus semua filter</i>
    
○ <b>/import</b> <i>[membalas file yang diekspor]</i>
     <i>Impor filter dari file Cadangan</i>
"""

ABOUT_MESSAGE = f"""<b><u>ABOUT ME</u></b>

<b>○ Maintained by : <a href='tg://user?id={OWNER_ID}'>This Person</a>
"""

MARKDOWN_HELP = """<b><u>Markdown Formatting</u></b>

○ <b>Kata Berani</b> :
     format: <code>*Teks Tebal*</code>
     tampilkan sebagai: <b>Teks Tebal</b>
    
○ <b>Teks Miring</b>
     format: <code>_Italic Text_</code>
     tampilkan sebagai: <i>Teks Miring</i>
    
○ <b>Kode Kata</b>
     format: <code>`Teks Kode`</code>
     tampilkan sebagai: <code>Teks Kode</code>
    
○ <b>Garis Bawah</b>
     format: <code>__UnderLine Text__</code>
     tampilkan sebagai: <u>Teks Garis Bawah</u>
    
○ <b>Coret Lewat</b>
     format: <code>~Teks Coret~</code>
     tampilkan sebagai: <s>Teks Coret</s>
    
○ <b>Hyper Link</b>
     format: <code>[Teks](https://t.me/amkeenanx)</code>
     tampilkan sebagai: <a href='https://t.me/amkeenanx'>Teks</a>
    
○ <b>Tombol</b>
     <u>Tombol Url</u>:
     <code>[Teks Tombol](buttonurl:https://t.me/amkeenanx)</code>
     <u>Tombol Peringatan</u>:
     <code>[Teks Tombol](buttonalert:Teks Peringatan)</code>
     <u>Di Sameline</u>:
     <code>[Teks Tombol](buttonurl:https://t.me/amkeenanx:text same line)</code></i>

○ <b>Catatan:</b>
     <i>Simpan setiap Tombol di baris Terpisah saat memformat</i>
     <i>Teks pesan lansiran Anda harus kurang dari 200 karakter, jika tidak, bot akan mengabaikan tombol itu</i>

○ <b>Kiat:</b> <i>Anda dapat menambahkan tombol untuk stiker dan catatan video di perintah /tambahkan</i>"""
