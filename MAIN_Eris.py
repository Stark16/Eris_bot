import discord
from discord.ext import commands
import os
import time
import random


class Eris(discord.Client):
    def __init__(self) -> None:

        super().__init__(command_prefix='E_', intents = discord.Intents.default())
        
        self.PATH_self_dir = os.path.dirname(os.path.realpath(__file__))
        self.PATH_config = os.path.join(self.PATH_self_dir, 'config.conf')
        self.PATH_media = os.path.join(self.PATH_self_dir, 'media')

        self.johns = ["I live far away ...", "It's so Laggy ...", "My goldfish is dying ...", "I didn't have concent smh ..."]

        self.FFMPEG = 'ffmpeg'

        self.ERIS_Throne_room_ID = '1037787782761947219'

        self.load_soul()


    async def on_ready(self):
        print(f'Logged in as {self.user.name}')
        channel = self.get_channel(int(self.ERIS_Throne_room_ID))  # Replace CHANNEL_ID with the target channel ID
        if channel:
            await channel.send('I am Alive !!')
        else:
            print('Channel not found. Make sure the provided channel ID is correct.')

    
    async def john(self, message):
        if message.author == self.user:
            return

        if message.content.startswith('E_john'):
            response = random.choice(self.random_strings)
            await message.channel.send(response)


    def summon(self):
        self.run(self.ERIS_CONFIG['eris_soul'])


    def load_soul(self):
        
        with open(self.PATH_config, 'r') as f:
            lines = f.readlines()
            self.ERIS_CONFIG = {}
            for line in lines:
                key, value = line.split(' = ')
                self.ERIS_CONFIG[key] = value


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


if __name__ == "__main__":
    OBJ_eris = Eris()
    OBJ_eris.summon()