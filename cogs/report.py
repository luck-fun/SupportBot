import disnake
from disnake.ext import commands

class Report(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command()
    async def report(self, inter, member: disnake.Member, reason):
        support_role = inter.guild.get_role(1218472518290243704) #insert the ID of the role that will be responsible for the reports here
        if not disnake.utils.get(inter.guild.channels, name="reports"):
            channel = await inter.guild.create_text_channel("reports") #the channel where reports will be sent for further consideration

            await channel.set_permissions(inter.guild.default_role, view_channel=False, send_messages=False,
                                          read_messages=False)
            await channel.set_permissions(support_role, view_channel=True,
                                          send_messages=True, read_messages=True,
                                          read_message_history=True, attach_files=True, embed_links=True,
                                          add_reactions=True, external_emojis=True, use_external_emojis=True,
                                          use_slash_commands=True)
            embed = disnake.Embed(title=f"Report from {inter.author}",
                                  description=f"""Member: {member}, Reason: {reason}""")
            embed.set_thumbnail(inter.author.avatar)
            await channel.send(embed=embed)
            await inter.response.send_message('Thanks for your report, supports will considerate it',
                                              ephemeral=True)

        elif disnake.utils.get(inter.guild.channels, name="reports"):
            channel = disnake.utils.get(inter.guild.channels, name="reports") #the channel in the server where reports will be sent for further consideration

            await channel.set_permissions(inter.guild.default_role, view_channel=False, send_messages=False,
                                          read_messages=False)
            await channel.set_permissions(support_role, view_channel=True,
                                          send_messages=True, read_messages=True,
                                          read_message_history=True, attach_files=True, embed_links=True,
                                          add_reactions=True, external_emojis=True, use_external_emojis=True,
                                          use_slash_commands=True)
            embed=disnake.Embed(title=f"Report from {inter.author}",
                                                   description=f"""Member: {member}, Reason: {reason}""")
            embed.set_thumbnail(inter.author.avatar)
            await channel.send(embed=embed)
            await inter.response.send_message('Thanks for your report, supports will considerate it',
                                              ephemeral=True)


def setup(bot):
    bot.add_cog(Report(bot))