# Autoban (typing)
# Made by Xornotor
# Let's defeat this bots!

from os import getcwd
from time import sleep

from autoban.logger import logging
from autoban.tools import read_file, type_these


logger = logging.getLogger(__name__)

FILENAME = "banlist.txt"


def main():

    logger.warning("Starting bot, please put your cursor on the Twitch chat")
    sleep(5)

    logger.warning("Reading `%s`" % FILENAME)
    lines = read_file(getcwd() + "/" + FILENAME)

    logger.warning("Applying `%s` to chat, please wait..." % FILENAME)
    type_these(lines)

    logger.warning("Done.")
