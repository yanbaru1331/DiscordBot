import logging
import discord
import os

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    logger = logging.getLogger(__name__)

    TOKEN = os.environ.get("DISCORD_TOKEN")
    GUILD_ID = discord.Object(id=int(os.environ.get("GUILD_ID")))

class MyClient(discord.Client):
    def __init__(self, intents: discord.Intents):
        super().__init__(intents=intents)

        self.tree = discord.app_commands.CommandTree(self)

    async def setup_hook(self):
        self.tree.copy_global_to(guild=GUILD_ID)
        await self.tree.sync(guild=GUILD_ID)

intents = discord.Intents.default()
client = MyClient(intents=intents)

@client.event
async def on_ready():
    logger.info("ready")

@client.tree.command()
async def ping(interaction: discord.Interaction):
    latency = round(client.latency * 1e3)
    await interaction.response.send_message(f"pong!!\tLatency: {latency}ms")


client.run(TOKEN)