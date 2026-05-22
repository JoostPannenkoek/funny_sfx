#!/usr/bin/env python3

import random
import time
import argparse
from pathlib import Path
import pygame

# =========================
# CONFIG
# =========================

PRJROOT_PATH = Path(__file__).resolve().parent
SFX_PATH = PRJROOT_PATH / "sfx"

DEFAULT_CHANCE = 1000

SUPPORTED_EXTENSIONS = {
    ".mp3",
    ".wav",
    ".ogg",
    ".flac"
}

# =========================
# AUDIO
# =========================

pygame.mixer.init()

def get_random_sound():
    files = [
        f for f in SFX_PATH.rglob("*")
        if f.is_file() and f.suffix.lower() in SUPPORTED_EXTENSIONS
    ]

    if not files:
        return None

    return random.choice(files)

def play_random_sound():
    sound_file = get_random_sound()

    if sound_file is None:
        print("No sound files found.")
        return

    print(f"Playing: {sound_file.name}")

    pygame.mixer.music.load(str(sound_file))
    pygame.mixer.music.play()

# =========================
# MAIN
# =========================

parser = argparse.ArgumentParser(
    description="Random funny sound effect player"
)

parser.add_argument(
    "--now",
    action="store_true",
    help="Play a sound immediately and exit"
)

parser.add_argument(
    "--chance",
    type=int,
    default=DEFAULT_CHANCE,
    help="1/chance probability every second"
)

args = parser.parse_args()

if args.now:
    play_random_sound()

    # Keep process alive while audio plays
    while pygame.mixer.music.get_busy():
        time.sleep(0.1)

    raise SystemExit

print(f"rnd chance: 1/{args.chance}")

while True:
    time.sleep(1)

    if random.randrange(args.chance) == 0:
        play_random_sound()