token = ""

prefix = "&"

import asyncio
from discord.ext import commands
import random

print("Loading..")

words = [
    '-',
    '.',
    '!',
    '#',
    '-',
    '.',
]

loop = asyncio.get_event_loop()

bot = commands.Bot(command_prefix=prefix, self_bot=True)
bot.remove_command("help")


@bot.event
async def on_ready():
    print("Bot Online.")


async def do_smth():
    await bot.wait_until_ready()
    print("Bot Ready!")
    guild = bot.get_guild(813245078340501557)
    textt = guild.get_channel(878700514987110480)
    print("Started...")
    while not bot.is_closed():
        message = await textt.send(random.choice(words))
        print("Habe Nachricht versendet.")
        await asyncio.sleep(random.uniform(0, 0))
        await message.delete()
        await asyncio.sleep(random.uniform(30,50))


loop.create_task(do_smth())

bot.run(token, bot=False)

if __name__ == '__main__':
    client = disClient()
    keep_alive.keep_alive()
    client.run()
