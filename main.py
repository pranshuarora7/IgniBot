
import discord
import os
from dotenv import load_dotenv
import openai
from keep_alive import keep_alive


with open("chat.txt", "r") as f:
  chat = f.read()

def configure():
    load_dotenv()

configure()
token = os.getenv("Token")
openai.api_key = os.getenv("OPENAI_API_KEY")


class MyClient(discord.Client):
  async def on_ready(self):
    print('Logged on as', self.user)

  async def on_message(self, message):
    global chat
    chat += f"{message.author}: {message.content}\n"
    print(f'Message from {message.author}: {message.content}')
    if self.user != message.author:
       if self.user in message.mentions: 
         response = openai.Completion.create(
           model="text-davinci-003",
           prompt= f"{chat}\nigniBOT: ",
           temperature=1,
           max_tokens=256,
           top_p=1,
           frequency_penalty=0,
           presence_penalty=0
         )
         channel = message.channel
         messageToSend = response.choices[0].text
         await channel.send(messageToSend)


intents = discord.Intents.default()
intents.message_content = True
client = MyClient(intents=intents)

keep_alive()
client.run(token)
