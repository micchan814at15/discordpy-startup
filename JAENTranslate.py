import discord
import os
import traceback
import googletrans
from googletrans import Translator

token = os.environ['DISCORD_BOT_TOKEN']
client = discord.Client()
translator = Translator()

@client.event
async def on_message(message):
    if message.author.bot:
        return
    print('メッセージ識別中。\n')

    if message.content.startswith('mdb!tra'):
        say = message.content
        say = say[7:]
        if say.find('-') == -1:
            str = say
            detact = translator.detect(str)
            befor_lang = detact.lang
            if befor_lang == 'ja':
                convert_string = translator.translate(str, src=befor_lang, dest='en')
                embed = discord.Embed(title='Translate JPN→ENG', color=0x000080)
                embed.add_field(name='Japanese', value=str)
                embed.add_field(name='English', value=convert_string.text, inline=False)
                await message.channel.send(embed=embed)
                print('ENGへ')
                print('翻訳完了。メッセージ送信実行。')
                print('メッセージ送信完了。\n')
            else:
                convert_string = translator.translate(str, src=befor_lang, dest='ja')
                embed = discord.Embed(title='Translate ENG→JPN', color=0x800000)
                embed.add_field(name='English', value=str)
                embed.add_field(name='Japanese', value=convert_string.text, inline=False)
                await message.channel.send(embed=embed)
                print('翻訳を実行。サーバーとの接続は正常。翻訳レートはENG→JPN。')
                print('翻訳完了。メッセージ送信実行。')
                print('メッセージ送信完了。\n')
        else:
            trans, str = list(say.split('='))
            befor_lang, after_lang = list(trans.split('-'))
            convert_string = translator.translate(str, src=befor_lang, dest=after_lang)
            embed = discord.Embed(title='変換結果', color=0xff0000)
            embed.add_field(name='Befor', value=str)
            embed.add_field(name='After', value=convert_string.text, inline=False)
            await message.channel.send(embed=embed)


    if message.content.startswith('mdb!detect'):
        say = message.content
        s = say[8:]
        detect = translator.detect(s)
        m = 'この文字列の言語はたぶん ' + detect.lang + ' です。'
        await message.channel.send(m)
client.run(token)
