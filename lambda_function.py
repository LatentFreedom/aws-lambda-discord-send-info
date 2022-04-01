from discord_webhook import DiscordWebhook, DiscordEmbed
from dotenv import dotenv_values

config = dotenv_values(".env")

webhook = DiscordWebhook(url=config['WEBHOOK_URL'])

# Create Rules embed
embed = DiscordEmbed(
    title="Server Rules",
    description="""**1.** Use appropriate channels.
**2.** No hate speech, scamming, bullying, etc.
**3.** No politics.
**4.** No NSFW content.
**5.** Be respectful to one another.
**6.** If something is unclear, you can always ask one of the admins.
**7.** No personal information (real names, addresses, emails, etc.)""",
    color="008000")

webhook.add_embed(embed)

# Create faq embed
embed = DiscordEmbed(
    title="FAQ",
    description="",
    color="008000")
embed.add_embed_field(name='What is the website url?', value='https://discord.com',inline=False)


webhook.add_embed(embed)

# Send webhook
webhook.execute()

def lambda_handler(event, context):

    return {
        "statusCode": 200,
        "body": {"message": "Info Sent"}
    }