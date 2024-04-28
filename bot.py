import os

# import discord
from discord.ext import commands
import requests

TOKEN = os.environ['DISCORD_TOKEN']

bot = commands.Bot(command_prefix='!')


@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}!')


@bot.command(name='stats', help='Displays Warzone stats for a player')
async def fetch_stats(ctx, username: str):
    # Placeholder for the API call
    stats = get_warzone_stats(username)
    await ctx.send(stats)


def get_warzone_stats(username):
    # API call to fetch stats
    # Example URL and headers (you'll need to adjust this based on the actual API)
    url = f'https://api.tracker.gg/api/v2/warzone/standard/profile/{platform}/{username}'
    headers = {'TRN-Api-Key': 'YOUR_API_KEY'}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        data = response.json()
        # Parse and format the data as you want
        return data
    else:
        return 'Failed to retrieve stats.'


if __name__ == '__main__':
    bot.run(TOKEN)