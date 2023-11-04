import discord
from discord.ext import commands
import os
import random
import traceback

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='E!', intents=intents)
PATH_self_dir = os.path.dirname(os.path.realpath(__file__))
PATH_config = os.path.join(PATH_self_dir, 'config.conf')
# sp_obj = sp.Popen('where ffmpeg', shell=True, stdout=sp.PIPE)
PATH_FFMPEG = 'ffmpeg'

ERIS_Throne_room_ID = '1170214275642556516'         # kana's server
# ERIS_Throne_room_ID = '1037787782761947219'         # test server


johns = ["I live far away ...", "It's so Laggy ...", "My goldfish is dying ...", "I didn't have concent smh ...",
         "The monitor is bigger than I'm used to", "My door was open", "My keyboard was upside down", 
         "You stopped me from sneezing", "Shut The FUCK UP YOU DUMB BITCH", "My mic turn off broo", "I forgot ...",
         "I am not used to controller", "The sun was in my eyes", "I rolled shit tbh", "Tap jump was on", "Skill Issue",
         "This isn't my skin", "Stark's near me", "That was accidently Gay ..."]


def load_soul():
        
    with open(PATH_config, 'r') as f:
        lines = f.readlines()
        ERIS_CONFIG = {}
        for line in lines:
            key, value = line.split(' = ')
            ERIS_CONFIG[key] = value

    return ERIS_CONFIG


class CustomHelp(commands.HelpCommand):
    def command_not_found(self, command_name):
        return f"Command '{command_name}' not found."

    def get_command_signature(self, command):
        return f"{self.context.prefix}{command.qualified_name} {command.signature}"


@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')
    channel = bot.get_channel(int(ERIS_Throne_room_ID))  # Replace CHANNEL_ID with the target channel ID
    if channel:
        await channel.send('I am Alive !!')
    else:
        print('Channel not found. Make sure the provided channel ID is correct.')


@bot.command()
async def john(ctx):
    await ctx.send(random.choice(johns))


@bot.command()
async def whoami(ctx):
    if (str(ctx.author.name).lower() == 'stark42'):
        await ctx.channel.send(random.choice(["You're a dumb bitch", "BOTTOM BITCH BOII", "BITCH BOI"]))
    elif (str(ctx.author.name).lower() == 'kana.ry'):
        await ctx.channel.send(random.choice(["You're Me! I think", "Kanaa!!", " Uhh, THE BEST? DUH..", "The QUEEN Obvi ..."]))
    elif (str(ctx.author.name).lower() == 'scrumpo.'):
        await ctx.channel.send(random.choice(["You are that who don't give a shit about concent", "Uhh.. Solace I guess"]))
    elif (str(ctx.author.name).lower() == 'siwapyra'):
        await ctx.channel.send(random.choice(["You're Siwa, You're kinda new here, and new people bow before me you know?"]))
    elif (str(ctx.author.name).lower() == 'atzaell'):
        percentage = random.randint(10, 100)
        await ctx.channel.send(random.choice([f"You're {percentage}% Mexican", "You're Matt?"]))
    elif (str(ctx.author.name).lower() == 'juicybootypipes'):
        await ctx.channel.send(random.choice(["You remeber me don't you?", "Just cause you wield me dosn't mean you own me", "Get me a Wishing Cube and then I'll tell you for sure"]))
    elif (str(ctx.author.name).lower() == 'hanahakisyndrome'):
        await ctx.channel.send(random.choice(["You're not so bad", "You're sweet"]))

@bot.command()
async def wrap_up(ctx, n=2):
    try:
        n = int(n)
        if ctx.channel == bot.get_channel(int(ERIS_Throne_room_ID)):
            await ctx.message.delete()
            deleted = await ctx.channel.purge(limit=50)
            await ctx.send(f"Deleted {50} message(s).", delete_after=2)

        else:
            await ctx.message.delete()
            deleted = await ctx.channel.purge(limit=n)
            await ctx.send(f"Deleted {n} message(s).", delete_after=2)
    except:
        traceback.print_exc()


ERIS_CONFIG = load_soul()

bot.run(ERIS_CONFIG['dark_wishing_cube'])