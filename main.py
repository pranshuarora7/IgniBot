# This example requires the 'message_content' intent.
# application id
#1140999498559131728

# public key
# 7c7e04a461cf4c6cd21b49f62254c833b680e1be230ab8078304d4652d21d422


import discord
import os
from dotenv import load_dotenv
import openai


def configure():
    load_dotenv()

configure()


class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
      print(f'Message from {message.author}: {message.content}')
      channel = message.channel
      await channel.send("Hello!")    

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)

token = os.getenv("Token")
client.run(token)
