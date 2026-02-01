import random
import time
from dataclasses import dataclass
from typing import Generator, List, Optional

from app.exercises._exercise import Exercise
from app.music.chord import Chord


@dataclass
class DifficultyConfig:
    roots: List[str]
    qualities: List[str]
    extension_chance: float = 0.0
    alteration_chance: float = 0.0
    extension_choices: Optional[List[List[int]]] = None
    alteration_choices: Optional[List[List[str]]] = None


# Core root and quality sets
_ALL_ROOTS = [
    'Ab', 'A', 'A#', 'Bb', 'B', 'C', 'C#', 'Db', 'D', 'D#', 'Eb', 'E', 'F', 'F#', 'Gb',
    'G', 'G#'
]
_EASY_ROOTS = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
_MEDIUM_ROOTS = _EASY_ROOTS + ['Bb', 'C#','D#', 'F#', 'G#']

_EASY_QUALITIES = ["", "m"]
_MEDIUM_QUALITIES = ["", "m", "7"]
_HARD_QUALITIES = ["", "m", "7", "maj7", "m7", "dim", "sus2", "sus4"]

# Configuration for available difficulties. Add a new entry to support more levels.
LEVELS = {
    1: DifficultyConfig(
        roots=_EASY_ROOTS,
        qualities=_EASY_QUALITIES
    ),
    2: DifficultyConfig(
        roots=_MEDIUM_ROOTS,
        qualities=_EASY_QUALITIES
    ),
    3: DifficultyConfig(
        roots=_MEDIUM_ROOTS,
        qualities=_MEDIUM_QUALITIES
    ),
    4: DifficultyConfig(
        roots=_ALL_ROOTS,
        qualities=_MEDIUM_QUALITIES
    ),
    5: DifficultyConfig(
        roots=_ALL_ROOTS,
        qualities=_HARD_QUALITIES,
        extension_chance=0.4,
        alteration_chance=0.2,
        extension_choices=[[7], [9], [11], [13], [7, 9]],
        alteration_choices=[["b5"], ["#5"], ["b9"], ["#9"], ["b5", "b9"]],
    ),
}


def chord_practice(difficulty: int) -> Generator[Chord, None, None]:
    """Generate chords at a given interval using a difficulty configuration.

    The function uses the `LEVELS` mapping to obtain a `DifficultyConfig` for the
    requested `difficulty`. To add new difficulty levels in the future, add a new
    key/value to the `LEVELS` dict with a `DifficultyConfig` describing the behavior.

    Args:
        difficulty (int): Difficulty level (must be a key in `LEVELS`).

    Yields:
        Generator[Chord, None, None]: An infinite generator yielding `Chord` instances.

    Raises:
        ValueError: If `difficulty` is not present in the `LEVELS` mapping.
    """

    config = LEVELS.get(difficulty)
    if config is None:
        raise ValueError("unknown difficulty; add a matching entry to LEVELS")

    while True:
        root = random.choice(config.roots)
        quality = random.choice(config.qualities)

        extensions: Optional[List[int]] = None
        alterations: Optional[List[str]] = None

        if config.extension_choices and random.random() < config.extension_chance:
            extensions = random.choice(config.extension_choices)

        if config.alteration_choices and random.random() < config.alteration_chance:
            alterations = random.choice(config.alteration_choices)

        chord = Chord(root=root, quality=quality, extensions=extensions, alterations=alterations)
        yield chord


@dataclass
class ChordPractice(Exercise):

    def __init__(self, difficulty: int):
        self.difficulty = difficulty

    def name(self) -> str:
        return "Chord Practice"
    
    def category(self) -> str:
        return "Basics"

    def generate_exercise(self) -> Generator[Chord, None, None]:
        return chord_practice(self.difficulty)