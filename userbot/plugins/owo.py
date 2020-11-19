
  
import logging
import re
import random

from telethon import events

from __main__ import client

logger = logging.getLogger("Kateborg@{}".format(__name__))


def case_matcher(dest_fmt, group=0):
    def wrapped(m):
        src = m.group(group)
        groups = [m.group(0)]
        groups.extend(m.groups())
        dest = dest_fmt.format(*groups)
        if src.isupper():
            return dest.upper()
        elif src.islower():
            return dest.lower()
        return dest
    return wrapped


faces = ['(・`ω´・)', ';;w;;', 'OwO', 'UwU', '>w<', '^w^']
patterns = [
    (r'(?i)r|l', case_matcher('w')),
    (r'(?i)(n)([aeiou])', case_matcher('{1}y{2}', 1)),
    (r'(?i)ove', case_matcher('uv')),
    (r'(?i)(?<=[^aeiou])y\b', case_matcher('ie')),
    (r'(?i)th\B', case_matcher('tw')),
    (r'(?i)too', case_matcher('twoo')),
    ('!', lambda m: ' ' + random.choice(faces))
]
patterns = [(re.compile(pattern), sub) for pattern, sub in patterns]
original_texts = {}


@client.on(events.NewMessage(outgoing=True, pattern=re.compile(r'^[^!]')))
def owo(event):
    new_text = event.text
    for pattern, sub in patterns:
        new_text = pattern.sub(sub, new_text)
    if new_text != event.text:
        original_texts[event.message.id] = event.text
        event.edit(new_text, link_preview=bool(event.message.media))
        raise events.StopPropagation


@client.on(events.MessageRead(inbox=False))
def ninja(event):
    edited = []
    for message_id in original_texts:
        if event.is_read(message_id):
            logger.info('editing {} "{}"'.format(message_id, original_texts[message_id]))
            client.edit_message(event.input_chat, message_id, original_texts[message_id])
            edited.append(message_id)

    for message_id in edited:
        del original_texts[message_id]
