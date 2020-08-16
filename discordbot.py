import discord
import os
import traceback

token = os.environ['DISCORD_BOT_TOKEN']

client = discord.Client()


@client.event
async def on_ready():
    print('Connected.')
    print(client.user.name)
    print('------')


@client.event
async def on_ready():
    client.global_list = []


@client.event
async def on_message(message):
    if message.author == message.guild.me:
        return

    if message.webhook_id:
        return

    global_tmp = [w for w in await message.channel.webhooks() if w in client.global_list]

    if message.content == "!global":
        if global_tmp:
            await message.channel.send("既に登録されています。")
            return

        new_w = await message.channel.create_webhook(name="global")
        client.global_list.append(new_w)
        await message.channel.send("登録処理が完了しました。この機能が停止または再起動するまでグローバルチャットをご利用いただけます。定期的に`!mglobal`の送信を実行してください。")
        return

    for webhook in client.global_list:
        if message.channel != webhook.channel: ()

    if not global_tmp:
        return
    for webhook in client.global_list:
        if message.channel != webhook.channel:
            await webhook.send(content=message.content, username=message.author.name + message.author.discriminator,
                               avatar_url=message.author.avatar_url)




bot.run(token)
