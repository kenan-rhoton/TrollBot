pokes = []

def add_poke(message):
    for mention in message.mentions:
        pokes.append({
            'user_id': mention.id,
            'channel_name': message.channel,
            'message_id': message.id
            })
    
    if message.server is not None:
        for mention in message.role_mentions:
            for member in message.server.members:
                for role in member.roles:
                    if role == mention:
                        pokes.append({
                            'user_id': member.id,
                            'channel_name': message.channel,
                            'message_id': message.id
                            })

def remove_poke(i):
    del pokes[i]
