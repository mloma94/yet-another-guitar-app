"""
Script that will be used to run the selected exercise from the list of available exercises.
The list is available in this script and has to be manually updarted when new exercises are added.
It serves as an entry point for executing exercises in the application.

The following arguments can be provided:
- exercise_name: The name of the exercise to run. Mandatory.
- help (-h): Show this help message and exit.
- frequency (-f): The frequency (in milliseconds) at which the exercise prompts should occur.
    Optional (default: 1000 ms).
- difficulty (-d): The difficulty level of the exercise. Optional (default: 1).
- iterations (-n): The number of iterations to run the exercise for. Optional (default: 10).

Usage:
    python -m scripts.run_exercise -h to see help message.
    python -m scripts.run_exercise <exercise_name> [-f FREQUENCY] [-d DIFFICULTY] [-n ITERATIONS]
"""

import argparse
import itertools
import sys
import time

from app.exercises.chord_practice import ChordPractice

exercises = {
    "chord_practice": ChordPractice,
}


def main():
    """Parse arguments and run the selected exercise."""
    parser = argparse.ArgumentParser(
        description="Run a selected guitar exercise with customizable parameters."
    )
    
    parser.add_argument(
        "exercise_name",
        help="The name of the exercise to run. Available: " + ", ".join(exercises.keys())
    )
    parser.add_argument(
        "-f", "--frequency",
        type=int,
        default=1000,
        help="Frequency in milliseconds at which exercise prompts should occur (default: 1000)"
    )
    parser.add_argument(
        "-d", "--difficulty",
        type=int,
        default=1,
        help="Difficulty level of the exercise (default: 1)"
    )
    parser.add_argument(
        "-n", "--iterations",
        type=int,
        default=10,
        help="Number of iterations to run the exercise for (default: 10)"
    )
    
    args = parser.parse_args()
    
    # Validate exercise name
    if args.exercise_name not in exercises:
        print(f"Error: Unknown exercise '{args.exercise_name}'")
        print(f"Available exercises: {', '.join(exercises.keys())}")
        sys.exit(1)
    
    # Instantiate and run the exercise
    exercise_class = exercises[args.exercise_name]
    exercise = exercise_class(
        difficulty=args.difficulty
    )

    n = args.iterations
    
    # Generate and run exercise for specified iterations
    generator = exercise.generate_exercise()
    exercise_name = exercise.name()

    if exercise_name == "Chord Practice":
        for chord in itertools.islice(generator, n):
            print(f"{chord.display_name()}")
            time.sleep(args.frequency / 1000.0)  # Convert ms to seconds


if __name__ == "__main__":
    main()