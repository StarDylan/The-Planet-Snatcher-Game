import os
import time
import sys
from pathlib import Path
import logging
import random


import CharacterBuff
import encounters
import Campsite # TODO: Campsite Not needed, keep for story.
import gameMechanics

CharacterBuff = CharacterBuff.buff
gameMechanics = gameMechanics.gameMechanics
encounters = encounters.encounters

logging.basicConfig(format='%(asctime)s:%(levelname)s:%(message)s',filename='GameLog.log',level=logging.INFO)
character = CharacterBuff.buff(25, 25, 0, 25, 10)
