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
token = os.getenv("Token")
openai.api_key = os.getenv("OPENAI_API_KEY")


class MyClient(discord.Client):

  async def on_ready(self):
    print('Logged on as', self.user)

  async def on_message(self, message):
    print('Message from {message.author}: {message.content}')
    if self.user != message.author:
       if self.user in message.mentions: 
         channel = message.channel
         response = openai.Completion.create(
           model="text-davinci-003",
           prompt= message.content,
           temperature=1,
           max_tokens=256,
           top_p=1,
           frequency_penalty=0,
           presence_penalty=0
         )
         messageToSend = response.choices[0].text
         await channel.send(messageToSend)


intents = discord.Intents.default()
intents.message_content = True
client = MyClient(intents=intents)
client.run(token)
