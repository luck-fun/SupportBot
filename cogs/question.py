import disnake
from disnake.ext import commands

class QuestionModal(disnake.ui.Modal):
    def __init__(self):
        self.question_description = question_description
        self.questioner = questioner #member, who asking the question
        self.message = message
        components = [
            disnake.ui.TextInput(label="Answer", placeholder="Enter answer", custom_id="answer"),
        ]
        super().__init__(title="Answer", components=components)

    async def callback(self, inter: disnake.ModalInteraction):
        answer = inter.text_values["answer"]
        embed = disnake.Embed(title=f"Answer from {inter.user}", description=f"""Question: {self.question_description}
Answer: {answer}""")
        embed.set_thumbnail(url=inter.user.avatar)
        await self.questioner.send(embed=embed)
        new_message = disnake.Embed(title=f"Answer to {self.questioner} ", description=f"""Question: {self.question_description}
Answer: {answer}""")
        new_message.set_footer(text=f"Answered {inter.user}", icon_url=inter.user.avatar)
        new_message.set_thumbnail(url=self.questioner.avatar)
        await inter.response.edit_message(embed=new_message, view=None)

class QuestionView(disnake.ui.View):
    def __init__(self):
        super().__init__(timeout=None)

    @disnake.ui.button(label="Answer", style=disnake.ButtonStyle.grey, custom_id="button1")
    async def main_button(self, button: disnake.ui.Button, inter: disnake.Interaction):
        await inter.response.send_modal(QuestionModal())


class Question(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.persistent_views_added = False

    @commands.slash_command()
    async def question(self, inter, question):
        global question_description
        global questioner
        global message
        view = QuestionView()
        if not disnake.utils.get(inter.guild.channels, name="questions"):
            questioner = inter.author #member, who asking the question
            channel = await inter.guild.create_text_channel("questions")
            await channel.set_permissions(inter.guild.default_role, view_channel=False, send_messages=False,
                                          read_messages=False)
            await channel.set_permissions(inter.guild.get_role(1218472518290243704), view_channel=True,
                                          send_messages=True, read_messages=True,
                                          read_message_history=True, attach_files=True, embed_links=True,
                                          add_reactions=True, external_emojis=True, use_external_emojis=True,
                                          use_slash_commands=True)
            embed = disnake.Embed(title=f"Question from {inter.author}", description=question)
            question_description = embed.description
            embed.set_thumbnail(inter.author.avatar)
            message = await channel.send(embed=embed, view=view)
            await inter.response.send_message(
                "Thanks for your question, supports will considerate it and give you the answer", ephemeral = True)

        elif disnake.utils.get(inter.guild.channels, name="questions"):
            questioner = inter.author #member, who asking the question
            channel = disnake.utils.get(inter.guild.channels, name="questions")
            await channel.set_permissions(inter.guild.default_role, view_channel=False, send_messages=False,
                                          read_messages=False)
            await channel.set_permissions(inter.guild.get_role(1218472518290243704), view_channel=True,
                                          send_messages=True, read_messages=True,
                                          read_message_history=True, attach_files=True, embed_links=True,
                                          add_reactions=True, external_emojis=True, use_external_emojis=True,
                                          use_slash_commands=True)

            embed = disnake.Embed(title=f"Question from {inter.author}", description=question)
            question_description = embed.description
            embed.set_thumbnail(inter.author.avatar)
            message = await channel.send(embed=embed, view=view)
            await inter.response.send_message("Thanks for your question, supports will considerate it and give you the answer", ephemeral = True)


    @commands.Cog.listener()
    async def on_ready(self):
        if self.persistent_views_added:
            return

        self.bot.add_view(QuestionView())

def setup(bot):
    bot.add_cog(Question(bot))