TOKEN = ""

import discord

class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as', self.user)

    async def on_message(self, message):
        # don't respond to ourselves
        if message.author == self.user:
            return

        greeting = ["hello", "hi", "yo", "sup"]
    
        for i in greeting:
            if message.content.lower().startswith(i):
                await message.channel.send(f"Hello {message.author.mention}")

intents = discord.Intents.default()
intents.message_content = True
client = MyClient(intents=intents)
client.run(TOKEN)
