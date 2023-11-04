import asyncio
import aiohttp
import random
import discord
from discord import channel
from discord.ext import commands
import time
import threading
import youtube_dl
import os

import subprocess as sp
from discord.ext import tasks
import datetime

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='E_', intents=intents)
PATH_SELF = os.path.dirname(os.path.realpath(__file__))
# sp_obj = sp.Popen('where ffmpeg', shell=True, stdout=sp.PIPE)
PATH_FFMPEG = 'ffmpeg'

TORTURE_ROOM_ID = '935871952680263740'
TORTURE_CHANNEL = bot.get_channel(TORTURE_ROOM_ID)


class Eris:

    def __init__(self) -> None:
        self.PATH_self_dir = os.path.dirname(os.path.realpath(__file__))
        self.PATH_config = os.path.join(self.PATH_self_dir, 'config.conf')
        self.PATH_media = os.path.join(self.PATH_self_dir, 'media')

        self.load_soul()

    def load_soul(self):
        
        with open(self.PATH_config, 'r') as f:
            lines = f.readlines()
            self.ERIS_CONFIG = {}
            for line in lines:
                key, value = line.split(' = ')
                self.ERIS_CONFIG[key] = value


jarvis_soul = 'MTE3MDIxNzcyNzM1MzQzMDA2Nw.GBh_-P.CauimRfbZE1t9opmAy092-iOuCu8G02JwPrmIA'
dalit_role = 'Dalit'


pinged_people = {}
class who_is_pinged:

    def __init__(self) -> None:
        self.the_pinged_one = None
        self.the_pinger = None
        self.the_pinged_one_counter = 0
        self.limit = 1
        self.timer_limit_in_seconds = 40        
    
    def start_timer(self):
        
        while self.timer_limit_in_seconds >= 0:
            time.sleep(1)
            # print("ping timer: ", self.timer_limit_in_seconds)
            self.timer_limit_in_seconds -= 1
            

class targets:
    def __init__(self) -> None:
        self.targets = {}


class JSUP_STATUS:
    def __init__(self) -> None:
        self.VC_BUSY = False

class moving_members:
    def __init__(self) -> None:
        self.moving_members = {}
        self.last_member_was_moved_at = time.time()
        self.max_moved_duration = 60

    def reset(self):
        self.moving_members = {}
        self.last_member_was_moved_at = time.time()
        self.max_moved_duration = 60

class target_spammer:
    def __init__(self) -> None:
        self.target_spammer_dict = {}
        self.max_spam_timer = 300
        self.dalit_timer = 180
        self.max_target_count = 4
        self.warning_count = 2

OBJ_target_spammer = target_spammer()
OBJ_Jsup_Status = JSUP_STATUS()
OBJ_targets = targets()
OBJ_moving_members = moving_members()

@bot.event
async def on_ready():
    print('Jsup is at your service')



@bot.event
async def on_message(message):

    lowercase_msg = message.content.lower()
    senders_roles = []
    role = message.guild.roles

    if (lowercase_msg.startswith('j_target') or lowercase_msg.startswith('j_wakeup') or lowercase_msg.startswith('j_ttarget')):
        await bot.process_commands(message)
        return


    for r in role:
        senders_roles.append((r.name).lower())

    # roles = user.server.roles
    if ('rocco' in message.author.name and random.choice([False, False, True, True])):
        print("uhhgg, can you shut up for a while?")

    # Check Bot Status:
    if lowercase_msg == "j_you_there?" or lowercase_msg == 'j_you_there' or lowercase_msg == 'j_u_there' or lowercase_msg == 'j_u_der':
        
        if ('stark' in message.author.name.lower()):
            await message.channel.send('At Your Service Sir')
        elif('god' in senders_roles or 'Legend' in senders_roles):

            await message.channel.send('Umm, Yeah.. Duh!?')

        else:
            await message.channel.send('Sucka Who is u?')


    # Clear a channel:
    if lowercase_msg == "hey j, could you clean up the mess?" or lowercase_msg == 'jarvis, clean up the mess' or  \
        lowercase_msg == 'blood on my mat, handle it' or lowercase_msg == 'j, clean slate protocol' or \
        lowercase_msg == 'clean slate protocol' or lowercase_msg == 'clean up':
        
        if ('stark' in message.author.name.lower()):
            await message.channel.send('Right Away Sir.')
            
            
            if (message.channel == 'tesxt-arena'):
                await message.channel.purge(limit=1000)

            else:
                await message.channel.purge(limit=30)

        elif ('DRAGONBLADE3K' in message.author.name or 'DRAGONBLADE3K' in message.author.name):
            await message.channel.send('Aight, wait a sec.')
            await message.channel.purge(limit=30)

        else:
            await message.channel.send("I don't understand you or what you mean, maybe we are just not there yet..")


    # if someone pings some one too often:

    if (len(message.mentions) > 0):
        pinged_Id = message.mentions[0].id
        pinger_Id = message.author.id
        pinger = message.author

        if (pinger.name.lower() == 'jsup'):
            return

        if (pinger_Id in pinged_people.keys()):
            
            pinged_obj = pinged_people.get(pinger_Id, None)

            if (pinged_obj):
                print("RE-PING")
                pinged_obj.the_pinged_one_counter += 1

                if (pinged_obj.the_pinged_one_counter >= pinged_obj.limit and pinged_obj.timer_limit_in_seconds > 0):

                    if ('stark' in pinged_obj.the_pinger.name.lower()):
                        await message.channel.send("Sir, You designed me to stop this, please don't force my hand..".format(pinged_obj.the_pinger.name))
                    else:
                        is_in_vc = pinged_obj.the_pinger.voice
                        if (is_in_vc):

                            if(is_in_vc.self_deaf == False):
                                while OBJ_Jsup_Status.VC_BUSY == False:
                                    OBJ_Jsup_Status.VC_BUSY = True
                                    vc = pinged_obj.the_pinger.voice.channel
                                    voice_client = discord.utils.get(bot.voice_clients, guild=pinged_obj.the_pinger.guild)
                                    
                                    if (voice_client is None):                                
                                        await vc.connect()
                                    PATH_audio = os.path.join(PATH_media, 'arau_audio.mp3').replace("\\", "/")
                                    voice_client = discord.utils.get(bot.voice_clients, guild=pinged_obj.the_pinger.guild)
                                    voice_client.play(discord.FFmpegPCMAudio(executable=PATH_FFMPEG, source=PATH_audio))

                                    while voice_client.is_playing():
                                        time.sleep(.5)

                                    await pinged_obj.the_pinger.guild.voice_client.disconnect()

                                OBJ_Jsup_Status.VC_BUSY = False


                            else:
                                await message.channel.send("Undefean ho saale.. darpok <@{}>".format(pinged_obj.the_pinger.id))

                        else:
                            PATH_image = os.path.join(PATH_media, 'arau_img.jpg')

                            with open(PATH_image, 'rb') as f:
                                picture = discord.File(f)
                                await message.channel.send(file=picture)


                elif (pinged_obj.timer_limit_in_seconds <= 0):
                    del pinged_people[pinger_Id]

            
        else:
            print("FOUND NEW PING")
            obj = who_is_pinged()
            obj.the_pinged_one = pinged_Id
            obj.the_pinger = pinger
            obj.the_pinged_one_counter = 0
            pinged_people[pinger_Id] = obj
            t = threading.Thread(target=obj.start_timer)
            t.start()

    # If none of the above are triggered, check for commands:
    await bot.process_commands(message)


@bot.command()
async def target(ctx):

    mentions = ctx.message.mentions


    if (len(mentions) <= 0):
        await ctx.message.channel.send("No Target Found. Please ensure the target is a member of the sever and mention them with a '@' at the start.\nLike: J_target @<user>")
        return
    targeted_memmber = ctx.message.mentions[0]
    target_id = ctx.message.mentions[0].id
    target_name = ctx.message.mentions[0].name
    target_author = ctx.author
    target_author_role = discord.utils.find(lambda r: r.name == 'Dalit', ctx.message.guild.roles)
    

    if (target_name.lower() == 'dragonblade3k' and str(ctx.author.name).lower() != 'stark'):
        chance = random.choice([False, False, True, True, True])
        if (chance == False):
            await ctx.message.channel.send("Mr. Stark Warned me that this would Happen. Like, what are the chances? I'll tell you what the chances are: 60%..")
            return

    if (str(ctx.author.name).lower() == 'stark'):

        if ((target_name).lower() == 'stark'):
            await ctx.message.channel.send("Sir, I maybe Jarvis Supreme, but I am no Ultron...")
            return

        if ((target_name).lower() == 'jsup'):
            await ctx.message.channel.send("Sir, Did I do anything wrong? In that case, allow me to apologize")
            return

    if ((target_name).lower() == 'jsup'):
            await ctx.message.channel.send("I am warning you.. Be careful what you ask for and to whome...")
            return

    if ((target_name).lower() == 'stark'):
        await ctx.message.channel.send("Be careful what you wish for...")
        return

    # Check if the auther is spamming:

    if (target_author_role in target_author.roles and str(ctx.author.name).lower() != 'stark'):
        await ctx.message.channel.send("Suckka You Dalit. Go stand in a corner.. \n<@{}> Keep targetting more people, and you'll stay as you are..".format(target_author.id))

        if (target_author in OBJ_target_spammer.target_spammer_dict.keys()):
            OBJ_target_spammer.target_spammer_dict[target_author]['neutralized_timer'] = time.time()

        return


    if (target_author in OBJ_target_spammer.target_spammer_dict.keys()):
        # print("[LOG] Tracked Timer: {}".format(time.time() - OBJ_target_spammer.target_spammer_dict[target_author]['first_target']))
        if (time.time() - OBJ_target_spammer.target_spammer_dict[target_author]['first_target'] <= OBJ_target_spammer.max_spam_timer 
                            and 
            OBJ_target_spammer.target_spammer_dict[target_author]['target_counts'] >= OBJ_target_spammer.max_target_count):
            OBJ_target_spammer.target_spammer_dict[target_author]['timeout'] = True
            OBJ_target_spammer.target_spammer_dict[target_author]['neutralized_timer'] = time.time()

            for victims in OBJ_target_spammer.target_spammer_dict[target_author]['targets']:
                if (victims in OBJ_targets.targets.keys()):
                    del OBJ_targets.targets[victims]

            await ctx.message.channel.send("<@{}> There was a line, And now you have crossed it...".format(target_author.id))
            return

        if (OBJ_target_spammer.target_spammer_dict[target_author]['target_counts'] >= OBJ_target_spammer.warning_count):
            await ctx.message.channel.send("I am warning you <@{}>.. Your actions can have consequences. Which You will regret it.".format(target_author.id))

        if (target_id in OBJ_target_spammer.target_spammer_dict[target_author]['targets'] == False):
            OBJ_target_spammer.target_spammer_dict[target_author]['targets'].append(target_id)
            OBJ_target_spammer.target_spammer_dict[target_author]['target_counts'] += 1
            OBJ_target_spammer.target_spammer_dict[target_author]['timeout'] = False
        
        else:
            OBJ_target_spammer.target_spammer_dict[target_author]['target_counts'] += 1
            OBJ_target_spammer.target_spammer_dict[target_author]['timeout'] = False


    
    else:
        if (str(ctx.author.name).lower() != 'stark'):
            OBJ_target_spammer.target_spammer_dict[target_author] = {}
            OBJ_target_spammer.target_spammer_dict[target_author]['targets'] = [target_id]
            OBJ_target_spammer.target_spammer_dict[target_author]['first_target'] = time.time()
            OBJ_target_spammer.target_spammer_dict[target_author]['target_counts'] = 1
            OBJ_target_spammer.target_spammer_dict[target_author]['timeout'] = False
            OBJ_target_spammer.target_spammer_dict[target_author]['neutralized'] = False
            OBJ_target_spammer.target_spammer_dict[target_author]['ctx'] = ctx

    if (target_id in OBJ_targets.targets.keys()):
        OBJ_targets.targets[target_id] = [targeted_memmber, False, False]
        
        await ctx.message.channel.send('Target Refreshed: @' + target_name)
        
        if (targeted_memmber.voice == None):
            await ctx.message.channel.send('@' + target_name + " Next Time you show yourself, things won't go good for you")

    else:
        OBJ_targets.targets[target_id] = [targeted_memmber,  False, False]
        await ctx.message.channel.send('Target Aquired: @' + target_name)
        if (targeted_memmber.voice == None):
            await ctx.message.channel.send('@' + target_name + " Next Time you show yourself, things won't go good for you")


async def timeout_user(*, user_id: int, guild_id: int, until):
    headers = {"Authorization": f"Bot {bot.http.token}"}
    url = f"https://discord.com/api/v9/guilds/{guild_id}/members/{user_id}"
    timeout = (datetime.datetime.utcnow() + datetime.timedelta(minutes=until)).isoformat()
    json = {'communication_disabled_until': timeout}
    async with bot.session.patch(url, json=json, headers=headers) as session:
        if session.status in range(200, 299):
           return True
        return False


@bot.command()
async def wakeup(ctx):
    mentions = ctx.message.mentions

    if (len(mentions) <= 0):

        if(str(ctx.author.name).lower() == 'stark'):
            await ctx.message.channel.send ("Sir, should use the command like this: J_wakeup @<user>. And I'll gladly wake up <user>'s ass up for you.")
            return

        await ctx.message.channel.send("Ummm. WTF is this? Either u mentioned someone that is not a member of the server, \
                             or You are a dumb fuck (most likely it is the latter), In which case here's how u use this command: J_wakeup @<user>")
        return

    if (mentions[0].name.lower() == 'jsup'):
        if(str(ctx.author.name).lower() == 'stark'):
            await ctx.message.channel.send ("I am a program, I am without form, and thus I can never be afk")
            return
        await ctx.message.channel.send ("Nigga You High?")
        return

    sleeping_member = ctx.message.mentions[0]

    if (OBJ_Jsup_Status.VC_BUSY == True):
        return

    if (sleeping_member.voice):
        if (sleeping_member.voice.self_deaf):
            OBJ_Jsup_Status.VC_BUSY = True
            previos_vc = sleeping_member.voice.channel
            await play_audio(sleeping_member, previos_vc, 'getup_getup_uhh.mp3')

            TORTURE_CHANNEL = discord.utils.get(sleeping_member.guild.voice_channels, name = f"torture room")

            for i in range(3):
                await sleeping_member.move_to(TORTURE_CHANNEL)
                await sleeping_member.move_to(previos_vc)
                
            await sleeping_member.move_to(previos_vc)

            OBJ_Jsup_Status.VC_BUSY = False

        else:
            if(str(ctx.author.name).lower() == 'stark'):
                await ctx.message.channel.send ("Sir, @{} is already undeafened".format(mentions[0].name))
                return
            await ctx.message.channel.send ("@{} is already awake you dumbASS. Do I need to come and wake you up instead?".format(mentions[0].name))

    else:
        if(str(ctx.author.name).lower() == 'stark'):
            await ctx.message.channel.send ("Sir, @{} is not in a VC".format(mentions[0].name))
            return
        await ctx.message.channel.send ("@{} is not in a Voice Channel you dumbASS. Do I need to come and wake you up instead?".format(mentions[0].name))

    OBJ_Jsup_Status.VC_BUSY = False


async def declare_target_vc(targeted_memmber):
    vc = targeted_memmber.voice.channel

    voice_client = discord.utils.get(bot.voice_clients, guild=targeted_memmber.guild)

    if (voice_client is None):                                
        await vc.connect()
        
    PATH_audio = os.path.join(PATH_media, 'ruk_tmc.mp3').replace("\\", "/")

    voice_client = discord.utils.get(bot.voice_clients, guild=targeted_memmber.guild)
    voice_client.play(discord.FFmpegPCMAudio(executable=PATH_FFMPEG, source=PATH_audio))
    while voice_client.is_playing():
        time.sleep(.5)
    await targeted_memmber.guild.voice_client.disconnect()


async def torture(targeted_memmber, TORTURE_CHANNEL, audio_name):
    vc = TORTURE_CHANNEL
    voice_client = discord.utils.get(bot.voice_clients, guild=targeted_memmber.guild)

    if (voice_client is None):                                
        await vc.connect()
        
    PATH_audio = os.path.join(PATH_media, audio_name).replace("\\", "/")

    voice_client = discord.utils.get(bot.voice_clients, guild=targeted_memmber.guild)
    voice_client.play(discord.FFmpegPCMAudio(executable=PATH_FFMPEG, source=PATH_audio))

    if (targeted_memmber in OBJ_moving_members.moving_members.keys()):
        del OBJ_moving_members.moving_members[targeted_memmber]

    while voice_client.is_playing():
        
        if (targeted_memmber in OBJ_moving_members.moving_members.keys()):
            before, after = OBJ_moving_members.moving_members[targeted_memmber]
            if (before.channel != after.channel):
                await targeted_memmber.guild.voice_client.disconnect()
                return False
                
            elif (after.self_deaf):
                await targeted_memmber.guild.voice_client.disconnect()
                return False


        await asyncio.sleep(.5)
    await targeted_memmber.guild.voice_client.disconnect()

    return True


async def play_audio(targeted_memmber, TORTURE_CHANNEL, audio_name):
    vc = TORTURE_CHANNEL
    voice_client = discord.utils.get(bot.voice_clients, guild=targeted_memmber.guild)

    if (voice_client is None):                                
        await vc.connect()
        
    PATH_audio = os.path.join(PATH_media, audio_name).replace("\\", "/")

    voice_client = discord.utils.get(bot.voice_clients, guild=targeted_memmber.guild)
    voice_client.play(discord.FFmpegPCMAudio(executable=PATH_FFMPEG, source=PATH_audio))


    while voice_client.is_playing():
        await asyncio.sleep(.5)

    await targeted_memmber.guild.voice_client.disconnect()



@bot.event
async def on_voice_state_update(member, before, after):

    OBJ_moving_members.moving_members[member] = [before, after]
    OBJ_moving_members.last_member_was_moved_at = time.time()


@tasks.loop(seconds=5)
async def scan_for_targets():
    print("Currently Tracked Targets:", OBJ_targets.targets)
    print("\n")
    print("Currently tracked Spammers: ", OBJ_target_spammer.target_spammer_dict)
    print("\n")
    

    # print("target vc: ", OBJ_targets.targets)
    if (OBJ_Jsup_Status.VC_BUSY == True):
        return

    delete_spammers = []
    for key in OBJ_target_spammer.target_spammer_dict.keys():
        if(OBJ_target_spammer.target_spammer_dict[key]['timeout'] and OBJ_target_spammer.target_spammer_dict[key]['neutralized'] == False):
            # handshake = await timeout_user(user_id=key.id, guild_id=key.guild.id, until=1)
            # if handshake:
            await key.add_roles(discord.utils.get(key.guild.roles, name=dalit_role))
            await OBJ_target_spammer.target_spammer_dict[key]['ctx'].send(f"Threat: <@{key.id}> Status: Neutralized for {1} minute.")
            OBJ_target_spammer.target_spammer_dict[key]['neutralized'] = True
            for victims in OBJ_target_spammer.target_spammer_dict[key]['targets']:
                if (victims in OBJ_targets.targets.keys()):
                    del OBJ_targets.targets[victims]

        if (OBJ_target_spammer.target_spammer_dict[key]['neutralized'] 
                    and 
            time.time() - OBJ_target_spammer.target_spammer_dict[key]['neutralized_timer'] >= OBJ_target_spammer.dalit_timer):
            await key.remove_roles(discord.utils.get(key.guild.roles, name=dalit_role))
            await OBJ_target_spammer.target_spammer_dict[key]['ctx'].send(f"<@{key.id}> Your Dalit Status is revoked, but I'll add it again if you spam more targets...")
            delete_spammers.append(key)

        elif (time.time() - OBJ_target_spammer.target_spammer_dict[key]['first_target'] > OBJ_target_spammer.max_spam_timer 
                            and 
            OBJ_target_spammer.target_spammer_dict[key]['target_counts'] < OBJ_target_spammer.max_target_count):
            delete_spammers.append(key)

    for spammer in delete_spammers:
        del OBJ_target_spammer.target_spammer_dict[spammer]

    to_delete = []
    for target_id, data in OBJ_targets.targets.items():
        # print("Target vc: ", data[0].voice.channel)
        if (OBJ_Jsup_Status.VC_BUSY == True):
            return

        if (OBJ_targets.targets[target_id][2] == True):
            continue
        targeted_memmber = data[0]
        is_currently_totured = data[1]
        
        if (targeted_memmber.voice == None):
            continue
        previos_vc = targeted_memmber.voice.channel
        if (is_currently_totured):
            continue
        
        if (targeted_memmber.voice):
            OBJ_targets.targets[target_id][1] = True
            if(targeted_memmber.voice.self_deaf == False):

                # Set Flags:
                
                OBJ_Jsup_Status.VC_BUSY = True

                await declare_target_vc(targeted_memmber)
                TORTURE_CHANNEL = discord.utils.get(targeted_memmber.guild.voice_channels, name = f"torture room")
                await targeted_memmber.move_to(TORTURE_CHANNEL)
                time.sleep(3)
                torture_status = await torture(targeted_memmber, TORTURE_CHANNEL, 'abe_haram_ke.mp3')

                if (torture_status):
                    OBJ_targets.targets[target_id][2] = True
                    to_delete.append(target_id)

                else:
                    if (OBJ_moving_members.moving_members[targeted_memmber][1].channel != TORTURE_CHANNEL):
                        OBJ_targets.targets[target_id][1] = False
                        OBJ_targets.targets[target_id][2] = False

                    elif (targeted_memmber.voice.self_deaf):
                        while(targeted_memmber.voice.self_deaf):
                            await targeted_memmber.move_to(previos_vc)
                            await targeted_memmber.move_to(TORTURE_CHANNEL)
                        OBJ_targets.targets[target_id][1] = False
                        OBJ_targets.targets[target_id][2] = False

                OBJ_Jsup_Status.VC_BUSY = False
                

            else:
                TORTURE_CHANNEL = discord.utils.get(targeted_memmber.guild.voice_channels, name = f"torture room")
                OBJ_Jsup_Status.VC_BUSY = True
                await targeted_memmber.move_to(TORTURE_CHANNEL)
                time.sleep(2)
                while(targeted_memmber.voice.self_deaf):
                    await targeted_memmber.move_to(previos_vc)
                    await targeted_memmber.move_to(TORTURE_CHANNEL)
                OBJ_targets.targets[target_id][1] = False
                OBJ_targets.targets[target_id][2] = False
                OBJ_Jsup_Status.VC_BUSY = False
                await targeted_memmber.move_to(previos_vc)

    for killed_targets in to_delete:
        del OBJ_targets.targets[killed_targets]


def remove_older_moved_memebers():
    while True:
        if (time.time() - OBJ_moving_members.last_member_was_moved_at >= OBJ_moving_members.max_moved_duration):
            OBJ_moving_members.reset()
        time.sleep(1)

# async def target_spotted():
#     while True:
#         for target_id, data in OBJ_targets.targets.items():
#             target = data[0]
#             duration = data[1]

#             if (target.voice):
#                 if(target.voice.self_deaf == False):
#                     while(OBJ_Jsup_Status.VC_BUSY == False):
#                         OBJ_Jsup_Status.VC_BUSY = True
#                         asyncio.create_task(declare_target_vc(target))
#                         declare_target_vc(target)
#                         # asyncio.set_event_loop(loop1)
#                         # loop1.run_until_complete(declare_target_vc(target))
#                         print("running??")

#                     OBJ_Jsup_Status.VC_BUSY = False

# loop = asyncio.new_event_loop()
# task = loop.create_task(target_spotted)


t1 = threading.Thread(target=remove_older_moved_memebers)
t1.start()
scan_for_targets.start()
bot.run(jarvis_soul)
