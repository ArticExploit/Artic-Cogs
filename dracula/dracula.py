from redbot.core import commands
import aiohttp
from redbot.core.bot import Red

class Dracula(commands.Cog):
    """Cog for fetching random Dracula Flow quotes."""

    __version__ = "1.1"
    __author__ = "Artic"

    def __init__(self, bot: Red):
        self.bot = bot
        self.api_url = "https://articexploit.xyz/dracula/api.php"
        self.session = aiohttp.ClientSession()

    async def cog_unload(self):
        await self.session.close()

    async def red_delete_data_for_user(self, **kwargs):
        """Nothing to delete."""
        pass

    @commands.command(name="dracula")
    async def quote(self, ctx: commands.Context):
        """Get a random quote."""
        await ctx.typing()
        quote_data = await self.fetch_quote()
        if quote_data:
            content = quote_data.get('quote', 'No quote available.')
            await ctx.send(content)
        else:
            await ctx.send("Unable to retrieve a quote at this time.")

    async def fetch_quote(self):
        """Fetch a random quote from the API."""
        try:
            async with self.session.get(self.api_url) as response:
                if response.status == 200:
                    return await response.json()
        except aiohttp.ClientError:
            pass
        return None
