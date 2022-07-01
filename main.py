import os
import re
import discord
import api_handler
import scribe
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
DuelComputer = commands.Bot(command_prefix='+')


@DuelComputer.event
async def on_ready(): print(f'Logged in as {DuelComputer.user}.')


# Commands #### #### #### #### #### #### #### #### #### #### #### #### #### #### #### ####


@DuelComputer.command(name='rulebook', help='TCG Rulebook v.10 PDF download')
async def rulebook(ctx): await ctx.send("https://www.yugioh-card.com/en/downloads/rulebook/SD_RuleBook_EN_10.pdf")


@DuelComputer.command(name='tcgop', help='TCG Organized Play documentation')
async def tcgop(ctx): await ctx.send("https://www.yugioh-card.com/en/events/organizedplay/")


@DuelComputer.command(name='tcggp', help='TCG Gameplay documentation')
async def tcggp(ctx): await ctx.send("https://www.yugioh-card.com/uk/gameplay/")


@DuelComputer.command(name='dbocg', help='OCG Q&A database translations')
async def dbocg(ctx): await ctx.send("https://db.ygorganization.com/")


@DuelComputer.command(name='dbude', help='UDE Q&A database (legacy)')
async def dbude(ctx): await ctx.send(
        "https://web.archive.org/web/20090217182013/http://entertainment.upperdeck.com/" +
        "yugioh/en/gameplay/faqs/cardfaqs/default.aspx?first=A&last=C")


@DuelComputer.command(name='fetc', help='Fast Effect Timing Chart')
async def fetc(ctx): await ctx.send(file=discord.File(r"resources\fast_effect_timing_chart.png"))


@DuelComputer.command(name='fll', help=r'TCG Forbidden/Limited List')
async def fll(ctx): await ctx.send("https://www.yugioh-card.com/uk/limited/")


@DuelComputer.command(name='pazim', help=r'Pazim''s resource folder')
async def pazim(ctx): await ctx.send("https://www.dropbox.com/sh/y4yemd7hpk99x6x/" +
                                     "AABFPFPYQA-OuXBqs8HwNpM9a?preview=Judge+Resources.pdf")


@DuelComputer.command(name='cred', help=r'Determining if a ruling answer is valid')
async def cred(ctx): await ctx.send(os.getenv('CREDIBILITY'))


@DuelComputer.command(name='dstep', help=r'Damage Step activation legality')
async def dstep(ctx): await ctx.send(os.getenv('DAMAGE_STEP'))


@DuelComputer.command(name='summon', help=r'Definition of "Summon" in TCG/OCG')
async def summon(ctx): await ctx.send(os.getenv('SUMMON'))


@DuelComputer.command(name='replay', help=r'When battle replays happen')
async def replay(ctx): await ctx.send(os.getenv('REPLAY'))


@DuelComputer.command(name='ssm', help=r'Special Summon Monsters & proper summoning')
async def ssm(ctx): await ctx.send(os.getenv('SPECIAL_SUMMON_MONSTERS'))


@DuelComputer.command(name='rules', help=r'R&P channel rules')
async def rules(ctx): await ctx.send(os.getenv('RULES'))


@DuelComputer.command(name='pendulum', help=r'Moving Pends to the face-up Extra Deck')
async def pendulum(ctx): await ctx.send(os.getenv('pendulum'))


@DuelComputer.command(name='psct', help=r'PSCT formatting')
async def psct(ctx): await ctx.send(os.getenv('psct'))


@DuelComputer.command(name='testing')
@commands.is_owner()
async def testing(ctx):
    api_handler.dbpoke()
    await ctx.send("System check is complete; no problems found.")


# End Commands #### #### #### #### #### #### #### #### #### #### #### #### #### #### #### ####


@DuelComputer.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Welcome, {member.name}. Please introduce yourself and take a seat.'
    )


@DuelComputer.event
async def on_message(message):
    if message.author == DuelComputer.user:
        return

    if re.compile(r"^(good (morning|day|afternoon|evening)|greetings|hello).{1,2}duel.?(bot|machine|comp)",
                  re.IGNORECASE).match(message.content):
        await message.channel.send(f'Greetings, {message.author.display_name}.')

    await DuelComputer.process_commands(message)


@DuelComputer.event
async def on_error(event, *args):
    with open('err.log', 'a') as f:
        if event == 'on_message':
            f.write(f'Unhandled message: {args[0]}\n')
        else:
            raise

# End events #### #### #### #### #### #### #### #### #### #### #### #### #### #### #### ####

DuelComputer.run(os.getenv('TOKEN'))
