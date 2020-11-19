# nickname system and name caching
import re

from telethon import events

from __main__ import client
from katestore import Katestore
from kateutil import get_first_name, get_entity_cached, get_target

import logging
logger = logging.getLogger("Kateborg@{}".format(__name__))


NICK_STORE = Katestore('nicknames.json', str)


def get_name(who):
    # if this entity is nicknamed, return the nickname
    if who in NICK_STORE:
        logger.info('returning nickname for {}'.format(who))
        return NICK_STORE[who]

    # otherwise return the entity's name
    return get_first_name(get_entity_cached(who))


@client.on(events.NewMessage(outgoing=True, pattern=re.compile('^!nick(.*)$')))
def on_message(event):
    if event.forward:
        return

    nickname = event.pattern_match.group(1).strip()
    who = get_target(event)
    if not who:
        return
    if nickname:
        logger.info('setting nickname for {} to {}'.format(who, nickname))
        NICK_STORE[who] = nickname
    else:
        logger.info('clearing nickname for {}'.format(who))
        del NICK_STORE[who]
    raise events.StopPropagation
