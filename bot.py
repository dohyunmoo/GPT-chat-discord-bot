import discord
import responses
import json

async def send_message(message, user_msg):
    try: 
        if user_msg == "":
            await message.channel.send("`This bot is made by DM`")
        else:
            response = responses.handle_response(user_msg)
            await message.channel.send(response)

    except Exception as e:
        print(e)

def run_bot():

    with open('data.json') as f:
        data = json.load(f)

    TOKEN = data['BOT-TOKEN']
    client = discord.Client(intents=discord.Intents.all())
    f.close()

    @client.event
    async def on_ready():
        print(f'{client.user} is now running')

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return

        if str(message.content).split(" ")[0] != "!gpt":
            print(str(message.content))
            return

        username = str(message.author)
        user_msg = " ".join(str(message.content).split(" ")[1:]) 
        channel = str(message.channel)

        print(f'"{user_msg}" was written in {channel} channel by {username}')
        await send_message(message, user_msg)

    client.run(TOKEN)
