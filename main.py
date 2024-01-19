import nextcord
from nextcord import Interaction
from nextcord.ext import commands

bot = commands.Bot(command_prefix="!", intents = nextcord.Intents.all())
token = ""

# Run code
@bot.event
async def on_ready():
    print('Bot has now logged in as: {0.user}'.format(bot))
    await bot.change_presence(activity=nextcord.Activity(type = nextcord.ActivityType.playing, name = f"Pit Price Tracking"))