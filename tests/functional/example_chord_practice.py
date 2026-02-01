"""
Example usage of the chord_practice function for testing and debugging.
Run this file to see the chord_practice generator in action.

Run from the project root with: python -m tests.functional.example_chord_practice
"""

import itertools
import time

from app.exercises.chord_practice import ChordPractice


def test_exercise():
    """Basic example: Generate 5 chords with 1-second intervals."""
    print("=== Testing Chord Practice Exercise ===")

    frequency = int(input("Enter frequency in seconds: "))
    difficulty = int(input("Enter difficulty level (1-5): "))
    n = int(input("Enter number of chords to generate: "))

    exercise = ChordPractice(difficulty)
    
    # Take only the first n chords using itertools.islice
    for i, chord in enumerate(itertools.islice(exercise.generate_exercise(), n)):
        print(f"Chord {i+1}: {chord.display_name()}")
        time.sleep(frequency)

if __name__ == "__main__":
    test_exercise()
