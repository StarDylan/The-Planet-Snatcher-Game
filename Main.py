import os
import time
import sys
from pathlib import Path
import logging
import random


from CharacterBuff import character

#import Campsite # TODO: Campsite Not needed, keep for story.

player1 = character(0,0,0,0,0)

logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s',filename='GameLog.log',level=logging.INFO)
