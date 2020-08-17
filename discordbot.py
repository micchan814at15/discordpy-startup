from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='mdb!')
token = os.environ['DISCORD_BOT_TOKEN']

bot.remove_command("help")

@bot.command(name="help")
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
                   f"\n"
                   f"Mermo Infomation\n"
                   f"mdb!botdev    Mermoの開発者を見ます。\n"
                   f"mdb!botver    Mermoのバージョンを確認します。\n"
                   f"mdb!nextud    次のMermoのアップデートの予定の詳細を表示します。\n"
                   f"mdb!pastud    過去のMermoのアップデートの詳細を表示します。\n"
                   f"mdb!invite    Mermoをサーバーに招待するリンクを表示します。\n"
                   f"mdb!joinserver    Mermoのサポートサーバーへの招待リンクを表示します。\n"
                   f"\n\n"
                   f"*1:この機能は常時稼働ではありません。\n"
                   f"*2:この機能は荒らし禁止のサーバーまたはチャンネルで実行しないでください。\n"
                   f"```\n")
    print('helpのコマンドが実行されました。')

@bot.command(name="こんにちは")
async def hello(ctx):
    """こんにちはのあいさつをする"""
    await ctx.send(f"どうも、{ctx.message.author.name}さん！")
    print('こんにちはのコマンドが実行されました。')

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

@bot.command(name="botdev")
async def hello(ctx):
    """Botのバージョンを確認する"""
    await ctx.send(f"> このBotの開発者は、micchandazoだお\n> \n> Discord:`@micchandazo#9669`\n> Twitter @micchandazo( https://twitter.com/micchandazo )")
    print('botdevのコマンドが実行されました。')

@bot.command(name="hel")
async def support(ctx):
    """移行されたコマンド"""
    await ctx.send(f"> コマンド一覧のコマンドはmdb!cmdsに変更されました。今後コマンド一覧を表示する場合はmdb!cmdsと送信してください。")
    print('helのコマンドが実行されました。')


    
#@bot.command(name="cmds")
#async def help(ctx):
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

#@bot.command(name="mehelp")
#async def soudayo(ctx):
#    """画像Botのヘルプページを表示"""
#    print('soudayoのコマンドが実行されました。')

#@bot.command(name="help2")
#async def invite(ctx):
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
    await ctx.send(f"> Mermoのサポートサーバーに参加する\n> micchandazo Botのサポートサーバーに参加するには、以下のURLにアクセスしてください。\nhttps://discord.gg/uKGSxSM")
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
                   f"> Ver.0.03.5[Beta](Latest)    Updated2020/08/17 18:02(JST,GMT +09:00)\n"
                   f"> アップデート内容/n"
                   f"> 【変更】一部のMermoのコマンドのPythonコードをHerokuへ稼働環境を移転しました。"
                   f"> 【変更】Helpページをわかりやすくなるように編集しました。"
                   f"\n"
                   f"> Ver.0.03.2[Beta]    Updated:2020/08/16 19:16(JST,GMT +09:00)\n"
                   f"> アップデート内容\n"
                   f"> 【新規】Ping値が確認可能になりました。`mdb!ping`と送信すると、Ping値が確認ができます。"
                   f"\n"
                   f"> Ver.0.03.1.K1[Beta][緊急アップデート]    Updated:2020/08/12 01:41(JST,GMT +09:00)\n"
                   f"> アップデートされた内容:\n"
                   f"> 荒らしコマンドのコマンドプレフィックスを変更しました。\n"
                   f"> コマンドプレフィックスは`mdba!`です。\n"
                   f"> 現在の荒らしコマンド一覧:`mdba!name50` `mdba!name100`\n"
                   f"\n"
                   f"> バージョン:0.03.1[Beta](Latest)   アップデート日時:2020/08/10 17:55(JST,GMT+09:00)\n"
                   f"> アップデート内容\n"
                   f"> コマンドで画像送信の機能を正式に公開しました。\n"
                   f"> mdb!mehelpでその機能のヘルプページを表示します。\n")
    print('pastudのコマンドが実行されました。')

@bot.command(name="botver")
async def support(ctx):
    """このBotのバージョンを確認する"""
    await ctx.send(f"> **Mermo**(micchandazo Bot)\n> **Ver.0.03.5[Beta]**\n> Updated 2020/08/17 18:02(JST,GMT +09:00)\n> Developer micchandazo")
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
    await ctx.send(f"> Mermo Global Chat Service(MGCS)\n> \n> MGCSを利用する前に次のURLにアクセスして、注意事項と利用方法をお読みください。\n> https://dcmermopj.jimdofree.com/mermo-global-chat/ \n> \n> Public Channelに参加する場合は、「mermo-gc」というチャンネルを作成してください。\n> \n> 「mermo-gc」のチャンネルで発言すると、導入しているすべてのサーバーに発言が表示されます(常時起動ではないため、一時的ご利用できない場合があります)。\n> \n> Private Global Channelを作成する場合は、以下のURLにアクセスしてください。\n> https://docs.google.com/forms/d/e/1FAIpQLSdDCekat2_KFEQapSuhcVShiFeg-iafsQ6uKnDJr6cIkO4kKg/viewform?usp=sf_link")
    print('mrmgcのコマンドが実行されました。')


Ping = bot.latency

@bot.command(name='ping')
async def ping(ctx):
    """Ping値を確認する"""
    await ctx.send('Pong! {0}'.format(round(bot.latency * 1000, 1)))

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
    await ctx.send(f"https://cdn.discordapp.com/attachments/712172035945529374/741461677056327792/image0.png")
    print('Ran tnokmikaeri.')

@bot.command(name="meabesonnani")
async def hello(ctx):
    """安倍の「そんなに興奮しないでください」の画像を送信する"""
    await ctx.send(f"https://cdn.discordapp.com/attachments/712172035945529374/741978273092993024/unknown.png")
    print('Ran abesonnani.')

@bot.command(name="meabeyurusanai")
async def hello(ctx):
    """安倍政権への批判の画像を送信する"""
    await ctx.send(f"https://media.discordapp.net/attachments/712172035945529374/743003950323859506/9k.png?width=242&height=169")
    print('Ran abeyurusanai.')

bot.run(token)
