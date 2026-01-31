"""
Example usage of the chord_practice function for testing and debugging.
Run this file to see the chord_practice generator in action.

Run from the project root with: python -m tests.functional.example_chord_practice
"""

import itertools

from app.exercises.chord_practice import chord_practice


def test_exercise():
    """Basic example: Generate 5 chords with 1-second intervals."""
    print("=== Testing Chord Practice Exercise ===")

    frequency = int(input("Enter frequency in seconds: "))
    difficulty = int(input("Enter difficulty level (1-5): "))
    
    generator = chord_practice(frequency*1000, difficulty)
    
    # Take only the first 5 chords using itertools.islice
    for i, chord in enumerate(itertools.islice(generator, 5)):
        print(f"Chord {i+1}: {chord.display_name()}")


if __name__ == "__main__":
    test_exercise()
