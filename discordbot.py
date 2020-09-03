import discord
import datetime
from discord.ext import commands
from discord.ext.commands import Bot
import os
import traceback

bot = commands.Bot(command_prefix='mdb!')
token = os.environ['DISCORD_BOT_TOKEN']

bot.remove_command("help")


@bot.command(name="help")
async def help01(ctx):
    embed1 = discord.Embed(title='Mermo Help page - Page 1', color=0x0078d7)
    embed1.add_field(name='このBotについて', value='このBotの基本コマンドプレフィックスは`mdb!`です。\n荒らしコマンドプレフィックスは`mdba!`です。\nこのBotの一部機能は常時稼働ではないため、一部の機能が一時的に停止する場合があります。',inline=False)
    embed1.add_field(name='------------------------------------------------------------', value='Mermoと楽しむ',inline=False)
    embed1.add_field(name='じゃんけん', value='Mermoとじゃんけんをします(mdb!は不要です)*1',inline=False)
    embed1.add_field(name='mdb!soudayo', value='そうだよ(便乗)と発言します',inline=False)
    embed1.add_field(name='------------------------------------------------------------', value='Mermoの便利ツール',inline=False)
    embed1.add_field(name='mdb!tra [翻訳する文]', value='日本語⇔英語の翻訳をします',inline=False)
    embed1.add_field(name='現在の時刻', value='現在の時刻を知らせます(mdb!は不要です)*1', inline=False)
    embed1.add_field(name='------------------------------------------------------------', value='Mermoの状態確認',inline=False)
    embed1.add_field(name='mdb!ping', value='MermoとDiscordの接続のPing値を確認します',inline=False)
    embed1.add_field(name='mdb!test', value='Mermoのテスト送信を実行します',inline=False)
    embed1.add_field(name='------------------------------------------------------------', value='Mermoのメンバー管理',inline=False)
    embed1.add_field(name='mdb!kick [キックするメンバーの名前またはユーザーIDまたはメンション]', value='Mermoがメンバーをキックします*3', inline=False)
    embed1.add_field(name='mdb!ban [キックするメンバーの名前またはユーザーIDまたはメンション]', value='MermoがメンバーをBANします*3', inline=False)
    embed1.add_field(name='------------------------------------------------------------', value='Mermo PictureBot',inline=False)
    embed1.add_field(name='mdb!me', value='Mermoが送信できる画像の説明とコマンドを表示します',inline=False)
    embed1.add_field(name='------------------------------------------------------------', value='Mermo Global Chat Service',inline=False)
    embed1.add_field(name='mdb!mrmgc', value='Mermoのグローバルチャット(Embed版)の利用方法について表示します',inline=False)
    embed1.add_field(name='!mglobal', value='Mermoのグローバルチャット(Webhook版)の登録処理をします(グローバルチャットを行うチャンネルで実行してください)*1',inline=False)
    embed1.add_field(name='------------------------------------------------------------', value='Mermo Helpページ',inline=False)
    await ctx.send (embed=embed1)
    embed2 = discord.Embed(title='Mermo Help page - Page 2', color=0x0078d7)
    embed2.add_field(name='------------------------------------------------------------', value='Mermo荒らしコマンド',inline=False)
    embed2.add_field(name='mdba!name50', value='実行者の名前を50回発言します*1 *2', inline=False)
    embed2.add_field(name='mdba!name100', value='実行者の名前を100回発言します*1 *2', inline=False)
    embed2.add_field(name='mdba!mentions100', value='実行者へ100回メンションします*1 *2', inline=False)
    embed2.add_field(name='------------------------------------------------------------', value='Mermoの情報',inline=False)
    embed2.add_field(name='mdb!botver', value='Mermoのバージョンを確認します', inline=False)
    embed2.add_field(name='mdb!pastud', value='過去のアップデートを確認します', inline=False)
    embed2.add_field(name='mdb!invite', value='Mermoをサーバーに招待リンクを送信します', inline=False)
    embed2.add_field(name='mdb!joinserver', value='Mermoのサポートサーバーへ参加します', inline=False)
    embed2.add_field(name='mdb!boti', value='Mermoの動作環境などを表示します', inline=False)
    embed2.add_field(name='------------------------------------------------------------', value='Mermo Helpページ',inline=False)
    embed2.add_field(name='*マークの説明',value='*1:常時稼働の機能ではないため、一時的に停止する場合があります\n*2:荒らし禁止のサーバー・チャンネルでは実行しないでください\n*3:実行するには管理者権限が必要です')
    await ctx.send(embed=embed2)



@bot.command(name="oldhelp")
async def support(ctx):
    """Helpページを表示する"""
    await ctx.send(f"```\n"
                   f"Mermoの使い方ガイド\n"
                   f"\n"
                   f"このBotの基本コマンドプレフィックスは mdb! です。\n"
                   f"荒らしコマンドプレフィックスは mdba! です。\n"
                   f"また、このBotの一部機能は常時稼働ではないため、不定期的に一部の機能が使用できなくなる場合があります。\n"
                   f"\n\n"
                   f"Mermo Remarks\n"
                   f"mdb!soudayo    そうだよ(便乗)と発言します。\n"
                   f"mdb!ping    Ping値を確認します。\n"
                   f"mdb!test    テスト発言をします。\n"
                   f"現在の時刻    Mermoが現在の時刻を知らせます。これを実行するとき、mdb!は不要です。*1\n"
                   f"\n"
                   f"Mermo Picturebot\n"
                   f"mdb!meabesonnani    安倍の「そんなに興奮しないでください」の画像を送信します。\n"
                   f"mdb!meabeyurusanai    安倍政権への批判の画像を送信します。\n"
                   f"mdb!metnokmikaeri    TNOKが見返った姿の画像を送信します。\n"
                   f"mdb!merequest    Mermo Picturebotへの画像登録をリクエストをします。\n"
                   f"\n"
                   f"Mermo Functions\n"
                   f"じゃんけん   Mermoとじゃんけんします。これを実行するとき、 mdb! は不要です。*1\n"
                   f"mdb!tra [翻訳する文]    日本語⇔英語の翻訳をします。コマンドの後ろに翻訳する文を入力してください。*1\n"
                   f"mdb!mrmgc    Mermoのグローバルチャットの利用方法などを表示します。\n"
                   f"\n"
                   f"Mermo Arashi\n"
                   f"mdba!name50    送信者の名前を50回発言します。*1 *2\n"
                   f"mdba!name100    送信者の名前を100回発言します。*1 *2\n"
                   f"mdba!mentions100    送信者へ100回メンションします。*1 *2\n"
                   f"\n"
                   f"Mermo Member Management\n"
                   f"mdb!kick [KICKするメンバーの名前]    メンバーのKICK処理を実行します。*3\n"
                   f"mdb!ban [BANするメンバーの名前]    メンバーのBAN処理を実行します。*3\n"
                   f"\n"
                   f"Mermo Global Chat Service(Webhook edition)\n"
                   f"!mglobal    Webhook方式のグローバルチャットに登録します\n"
                   f"\n"
                   f"Mermo Infomation"
                   f"mdb!botdev    Mermoの開発者を見ます。\n"
                   f"mdb!botver    Mermoのバージョンを確認します。\n"
                   f"mdb!nextud    次のMermoのアップデートの予定の詳細を表示します。\n"
                   f"mdb!pastud    過去のMermoのアップデートの詳細を表示します。\n"
                   f"mdb!invite    Mermoをサーバーに招待するリンクを表示します。\n"
                   f"mdb!joinserver    Mermoのサポートサーバーへの招待リンクを表示します。\n"
                   f"mdb!support    Mermo Supportの公式HPへのリンクを表示します。\n"
                   f"\n\n"
                   f"Mermoが受信したメッセージの記録について\n"
                   f"Mermoが受信したメッセージはすべてログに記録されます。\n"
                   f"ログに記録されたメッセージは第三者の申請などがない限り、第三者にデータの提供は行いません。\n"
                   f"ログに記録されたメッセージを閲覧したい場合は、micchandazo#9669に申請を送る必要があります。\n"
                   f"\n\n"
                   f"*1:この機能は常時稼働ではありません。\n"
                   f"*2:この機能は荒らし禁止のサーバーまたはチャンネルで実行しないでください。\n"
                   f"*3:この機能は管理者権限のあるユーザーのみ実行できます。このBotのロールを上位に上げなければこの機能は使用できない場合があります。"
                   f"```\n")
    print('helpのコマンドが実行されました。')

@bot.command(name="boti")
async def help01(ctx):
    embed1 = discord.Embed(title='Mermoの情報', color=0xffffff)
    embed1.add_field(name='Mermo開発者', value='micchandazo#9669 <@!482849264389586959>',inline=False)
    embed1.add_field(name='開発者のTwitter',value='https://twitter.com/micchandazo',inline=False)
    embed1.add_field(name='開発言語', value='Local:Python 3.8\nHeroku Python 3.8.2', inline=False)
    embed1.add_field(name='稼働開始日時', value='2020/06/07 02:28:47 (JST,GMT +09:00)', inline=False)
    await ctx.send (embed=embed1)

@bot.command(name="helpbeta")
async def hello(ctx):
    embed = discord.Embed(title='Mermo Help page', color=0xFFFFFF)
    embed.add_field(name='Please wait', value='ただいま作成中です')
    embed.add_field(name='ENG', value='Checking...')
    await ctx.send (embed=embed)

@bot.command(name="こんにちは")
async def hello(ctx):
    """こんにちはのあいさつをする"""
    await ctx.send(f"どうも、{ctx.message.author.name}さん！")
    print('こんにちはのコマンドが実行されました。')

#@bot.command(name="time")
#async def hello(ctx):
#    now = datetime.datetime.now()
#    await ctx.send(f"(。´・ω・)ん？現在の時刻？今、{now.hour + }時{now.minute}分{now.second}秒{now.microsecond}だよ")
#    print('こんにちはのコマンドが実行されました。')

@bot.command(name="さようなら")
async def goodbye(ctx):
    """さようならのあいさつをする"""
    await ctx.send(f"{ctx.message.author.name}さん、さよなランクルス害悪駆除")
    print('さようならのコマンドが実行されました。')


@bot.command(name="おはよう")
async def goodmorning(ctx):
    """おはようのあいさつをする"""
    await ctx.send(f"{ctx.message.author.name}さん、おはよウザさMAXキセキサニーゴ")
    print('おはようのコマンドが実行されました。')


@bot.command(name="よろしく")
async def meetyou(ctx):
    """よろしくのあいさつをする"""
    await ctx.send(f"{ctx.message.author.name}さん、よろしクレベース耐久化物")
    print('よろしくのコマンドが実行されました。')


@bot.command(name="こんばんは")
async def noonnight(ctx):
    """こんばんはのあいさつをする"""
    await ctx.send(f"こんばんは、{ctx.message.author.name}さん！")
    print('こんばんはのコマンドが実行されました。')


@bot.command(name="おやすみ")
async def goodnight(ctx):
    """おやすみのあいさつをする"""
    await ctx.send(f"{ctx.message.author.name}さん、おやすミミッキュいのちのたま")
    print('おやすみのコマンドが実行されました。')


# ----------!----------

@bot.command(name="botdev")
async def hello(ctx):
    """Botのバージョンを確認する"""
    await ctx.send(
        f"> Mermoはmicchandazoが開発しています。\n> \n> Discord:`@micchandazo#9669`\n> Twitter @micchandazo( https://twitter.com/micchandazo )\n公式HP: https://dcmermopj.jimdofree.com/ ")
    print('botdevのコマンドが実行されました。')


# @bot.command(name="cmds")
# async def help(ctx):
#    """コマンド一覧を表示する"""
#    await ctx.send(f"> Mermoのコマンド一覧\n\n"
#                   f"> `mdb!こんにちは`　Botがあいさつをします。\n"
#                   f"> `mdb!さようなら`　Botがあいさつをします。\n"
#                   f"> `mdb!おはよう`　Botがあいさつをします。\n"
#                   f"> `mdb!よろしく`　Botがあいさつをします。\n"
#                   f"> `mdb!おやすみ`　Botがあいさつをします。\n"
#                   f"> `mdb!tra [翻訳する文章]`　日本語↔英語の翻訳します。\n"
#                   f"> `mdb!soudayo`　そうだよ(便乗)と発言します。\n"
#                   f"> `mdb!name50`　名前を50回発言します(荒らし禁止のチャンネルでは実行しないでください)。\n"
#                   f"> `mdb!name100`　名前を100回発言します(荒らし禁止のチャンネルでは実行しないでください)。\n"
#                   f"> `mdb!mrmgc`　Global Chatの簡単な説明を表示します。\n"
#                   f"> `mdb!hel`　このメッセージを表示します。\n"
#                   f"> `mdb!invite`　Mermoを他のサーバーに参加するURLを送信します。\n"
#                   f"> `mdb!joinserver`　Mermoのサポートサーバーの参加URLを送信します。\n"
#                   f"> `mdb!nextud`　次のBotのアップデート内容を表示します。\n"
#                   f"> `mdb!pastud`　過去のアップデート情報が確認できます。\n"
#                   f"> `mdb!botdev`　Botの開発者の情報を送信します。\n"
#                   f"> `mdb!verinfo`　このBotのバージョン情報を確認できます。\n"
#                   f"> \n"
#                   f"> 詳しいコマンド一覧はMermo Bot ProjectのHPをご覧ください。\n"
#                   f"> https://micchan814at15.wixsite.com/mermobotpj/commands")
#    print('helのコマンドが実行されました。')

# @bot.command(name="mehelp")
# async def soudayo(ctx):
#    """画像Botのヘルプページを表示"""
#    print('soudayoのコマンドが実行されました。')

# @bot.command(name="help2")
# async def invite(ctx):
#    """Mermoの機能を表示する(Helpの2ページ目)"""
#    await ctx.send(f"```"
#                   f" Mermoの機能\n> \n"
#                   f" ・じゃんけん\n"
#                   f" じゃんけんをすることができます。遊ぶには、「じゃんけん」と送信してください。\n"
#                   f" ソースコード提供者:Sqar#0009\n"
#                   f" \n"
#                   f" ・画像Bot\n"
#                   f"　コマンドを入力して送信すると、Mermoが画像を送信します。コマンドはmdb!helpで確認ができます\n"
#                   f" \n"
#                   f" ・荒らしコマンド\n"
#                   f" 複数のメッセージを一括に送信するコマンドです。荒らし禁止のサーバー・チャンネルでは使用しないでください。\n"
#                   f" `mdba!help`で荒らしコマンドのHelpページを表示します。\n"
#                   f" \n"
#                   f" その他機能は今後追加予定です。お楽しみに。"
#                   f"```")
#    print('inviteのコマンドが実行されました。')

@bot.command(name="invite")
async def invite(ctx):
    """このBotをサーバーに参加する"""
    await ctx.send(f"> Mermoをサーバーに参加する\n"
                   f"> このBotを他のサーバーに参加するには、以下のURLにアクセスしてください。\nhttps://discord.com/oauth2/authorize?client_id=719014969731186758&permissions=8&scope=bot\n"
                   f"> *ただし、Botをサーバーに参加するには管理者権限が必要です。")
    print('inviteのコマンドが実行されました。')


@bot.command(name="tra")
async def nextud(ctx):
    """翻訳を実行(コマンドの後ろに原文を入力)"""
    await ctx.send(f"JPN→ENG,ENG→JPN Translate    Please wait...")
    print('traのコマンドが実行されました。Google Translateのサーバーに接続中です。')


@bot.command(name="joinserver")
async def support(ctx=None):
    """サポートサーバーに参加する"""
    await ctx.send(
        f"> Mermoのサポートサーバーに参加する\n> micchandazo Botのサポートサーバーに参加するには、以下のURLにアクセスしてください。\nhttps://discord.gg/uKGSxSM")
    print('joinserverのコマンドが実行されました。')


@bot.command(name="nextud")
async def nextud(ctx):
    """今後のアップデート予定を表示する"""
    await ctx.send(f"> **次のアップデート**\n"
                   f"> Ver.-.--.-[Beta]　予定日時:----/--/--(JST,GMT +09:00)\n> \n"
                   f"> アップデート内容\n"
                   f"")
    print('nextudのコマンドが実行されました。')



@bot.command(name="pastud")
async def pastud(ctx):
    """過去のアップデートを表示する"""
    await ctx.send(f"> **過去のアップデート**\n"
                   f"\n"
                   f"> Ver.0.04.5[公開Beta](Latest)    Updated:2020/09/03 22:05(JST,GMT +09:00)"
                   f"> アップデート内容"
                   f"> 【変更】HelpページをEmbedへ変更しました。旧Helpページはmdb!oldhelpで確認できます。"
                   f"> 【追加】Mermoの開発者、開発言語、稼働開始日時が確認できるようになりました。mdb!botiで確認可能です。"
                   f"> 【変更】Mermo PictureBotのコマンド一覧はmdb!meで確認できるように変更しました。")
    print('pastudのコマンドが実行されました。')
    
@bot.command(name="botver")
async def support(ctx):
    """このBotのバージョンを確認する"""
    await ctx.send(
        f"> **Mermo**(micchandazo Bot)\n> **Ver.0.04.5[公開Beta]**\n> Updated 2020/09/03 22:05(JST,GMT +09:00)\n> Developer micchandazo#9669")
    print('verinfoのコマンドが実行されました。')


@bot.command(name="soudayo")
async def soudayo(ctx):
    """そうだよ(便乗)と発言する"""
    await ctx.send(f"そうだよ(便乗)")
    print('soudayoのコマンドが実行されました。')


@bot.command(name="test")
async def test(ctx):
    """発信テストをする"""
    await ctx.send(f"> **発信テスト中**")
    print('testのコマンドが実行されました。')


@bot.command(name="comreq")
async def support(ctx):
    """コマンドリクエストの方法を表示する"""
    await ctx.send(f"> **コマンドのリクエストですか？**\n> コマンドをリクエストするには、サポートサーバーまたはmicchandazo#9669までお送りください(発言系のみ)。")
    print('comreqのコマンドが実行されました。')


@bot.command(name="mrmgc")
async def support(ctx):
    """MGCSの利用方法を表示する"""
    await ctx.send(
        f"> Mermo Global Chat Service(MGCS)\n> \n> MGCSを利用する前に次のURLにアクセスして、注意事項と利用方法をお読みください。\n> https://dcmermopj.jimdofree.com/mermo-global-chat/ \n> \n> Public Channelに参加する場合は、「mermo-gc」というチャンネルを作成してください。\n> \n> 「mermo-gc」のチャンネルで発言すると、導入しているすべてのサーバーに発言が表示されます(常時起動ではないため、一時的ご利用できない場合があります)。\n> \n> Private Global Channelを作成する場合は、以下のURLにアクセスしてください。\n> https://docs.google.com/forms/d/e/1FAIpQLSdDCekat2_KFEQapSuhcVShiFeg-iafsQ6uKnDJr6cIkO4kKg/viewform?usp=sf_link")
    print('mrmgcのコマンドが実行されました。')


Ping = bot.latency


@bot.command(name='ping')
async def ping(ctx):
    """Ping値を確認する"""
    await ctx.send('Pong! {0}'.format(round(bot.latency * 1000, 1)))


@bot.command(name="spissue")
async def hello(ctx):
    """こんにちはのあいさつをする"""
    await ctx.send(f"> Mermo support - 機能が動作しないなどの問題が発生した場合\n\n"
                   f"Mermoの機能の停止など問題が発生した場合はサポートサーバーに参加して報告するか、\n"
                   f"`micchandazo#9669`が参加しているサーバーで報告するか、\n"
                   f"`micchandazo#9669`までDMを報告を送信してください。")
    print('こんにちはのコマンドが実行されました。')


@bot.command(name="spbscode")
async def hello(ctx):
    """こんにちはのあいさつをする"""
    await ctx.send(f"> Mermo support - プレイステータスにあるBot Status Codeについて\n\n"
                   f"Mermoのステータスはプレイステータスで確認できます。\n"
                   f"ステータスコードの最初のアルファベット2文字の意味は\n"
                   f"`ER`がエラー\n"
                   f"`MT`がメンテナンス\n"
                   f"`ST`が機能停止\n"
                   f"です。\n"
                   f"詳しくはMermo公式HPを確認をしてください。: https://dcmermopj.jimdofree.com/status-codes/ ")
    print('こんにちはのコマンドが実行されました。')


@bot.command(name="me")
async def namemessage(ctx):
    await ctx.send(f"Mermo PictureBotのコマンド一覧"
                   f"```mdb!meabesonnani    安倍の「そんなに興奮しないでください」の画像を送信する```"
                   f"```mdb!meabeyurusanai    安倍政権への批判画像を送信する```"
                   f"```mdb!tnokmikaeri    TNOKが見返った姿の画像を送信する```"
                   f"\n画像登録はmdb!merequestと送信して確認ください。")
    
@bot.command(name="merequest")
async def hello(ctx):
    """画像登録を申請する"""
    await ctx.send(f"画像登録はサポートサーバーで受け付けています。\n"
                   f"以下の招待からサポートサーバーに参加し、登録を行いたい画像をアップロードしてください。\n"
                   f"> https://discord.gg/uKGSxSM")
    print('Ran request')


@bot.command(name="meraboot01")
async def hello(ctx):
    """ラビフットの画像を送信する"""
    await ctx.send(f"https://cdn.discordapp.com/attachments/719503000263196703/741810037906866226/image0.jpg")
    print('Ran raboot01.')


@bot.command(name="metnokmikaeri")
async def hello(ctx):
    """TNOKが見返ったの画像を送信する"""
    await ctx.send(f"https://micchandazo.chakin.com/mpmedia/metnokmikaeri.png")
    print('Ran tnokmikaeri.')


@bot.command(name="meabesonnani")
async def hello(ctx):
    """安倍の「そんなに興奮しないでください」の画像を送信する"""
    await ctx.send(f"https://micchandazo.chakin.com/mpmedia/meabesonnani.png")
    print('Ran abesonnani.')


@bot.command(name="meabeyurusanai")
async def hello(ctx):
    """安倍政権への批判の画像を送信する"""
    await ctx.send(f"https://micchandazo.chakin.com/mpmedia/meabeyurusanai.png")
    print('Ran abeyurusanai.')

@bot.command(name="suppoet")
async def hello(ctx):
    """安倍政権への批判の画像を送信する"""
    await ctx.send(
        f"Mermoのサポートページはこちらです:https://sites.google.com/view/mdmbotsp/")
    print('Ran abeyurusanai.')

@bot.command(name='kick')
@commands.has_permissions (administrator=True)
async def kick(ctx, member: discord.Member, *, reason=None):
    await ctx.send(f"{ctx.message.author.name}が{member.mention}のKICK処理を要求しました。ただいまKICK処理中です。お待ちください。")
    print('-------------------------------')
    print('Processing type: Kick member')
    print('Practitioner:' + str(ctx.message.author.name))
    print('Practitioner user ID:' + str(ctx.message.author.id))
    print('Target person user ID:' + str(member.id))
    print('Process ID:MK' + str(id(ctx)))
    print('Server name:' + str(ctx.message.guild.name) + ' Channel name:' + str(ctx.message.channel.name))
    print('Message link:' + 'https://discordapp.com/channels/' + str(ctx.message.guild.id) + '/' + str(ctx.message.channel.id) + '/' + str(ctx.message.id))
    print('-------------------------------')
    await member.kick (reason=reason)
    embed = discord.Embed (title=f'実行者:{ctx.author}', description=f"KICKの処理が完了しました:{member.mention}",color=0xfee101)
    embed.add_field (name=f"KICK対象のユーザーID:{member.id}", value=f"Mermo処理ID:MK{id(ctx)}", inline=False)
    await ctx.send (embed=embed)
    await ctx.send (f"次の情報は今回の処理の情報です:実行ユーザーID:{ctx.message.author.id} 対象ユーザーID:{member.id} 処理ID:MK{id(ctx)}\n実行サーバー:{ctx.message.guild.name}(ID:{ctx.message.guild.id})")




@bot.command (name='ban')
@commands.has_permissions (administrator=True)
async def ban(ctx, member: discord.Member, *, reason=None):
    await ctx.send(f"{ctx.message.author.name}が{member.mention}のBAN処理を要求しました。ただいまBAN処理中です。お待ちください。")
    print('-------------------------------')
    print('Processing type: Ban member')
    print('Practitioner:' + str(ctx.message.author.name))
    print('Practitioner user ID:' + str(ctx.message.author.id))
    print('Target person user ID:' + str(member.id))
    print('Process ID:MB' + str(id(ctx)))
    print('Server name:' + str(ctx.message.guild.name) + ' Channel name:' + str(ctx.message.channel.name))
    print('Message link:' + 'https://discordapp.com/channels/' + str(ctx.message.guild.id) + '/' + str(ctx.message.channel.id) + '/' + str(ctx.message.id))
    print('-------------------------------')
    await member.ban(reason=reason)
    embed=discord.Embed (title=f'実行者:{ctx.author}', description=f"BANの処理が完了しました:{member.mention}", color=0xff0000)
    embed.add_field (name=f"BAN対象のユーザーID:{member.id}", value=f"Mermo処理ID:MB{id(ctx)}", inline=False)
    await ctx.send (embed=embed)
    await ctx.send (f"次の情報は今回の処理の情報です:実行ユーザーID:{ctx.message.author.id} 対象ユーザーID:{member.id} 処理ID:MB{id(ctx)}\n実行サーバー:{ctx.message.guild.name}(ID:{ctx.message.guild.id}")


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.errors.MissingPermissions): #エラーの内容を判別
        await ctx.send("権限がありません")
    else:
        raise error
    
bot.run(token)
