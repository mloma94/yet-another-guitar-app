from abc import ABC, abstractmethod
from typing import Generator


class Exercise(ABC):
    """Abstract base class for exercises.
    
    This class defines the skeleton for all exercises with methods for
    naming, categorizing, and generating exercise content.
    """

    def __init__(self, difficulty: int):
        """Initialize an exercise with difficulty settings.
        
        Args:
            difficulty (int): Difficulty level.
        """
        self.difficulty = difficulty

    @abstractmethod
    def name(self) -> str:
        """Return the name of the exercise.
        
        Returns:
            str: The exercise name.
        """
        pass

    @abstractmethod
    def category(self) -> str:
        """Return the category of the exercise.
        
        Returns:
            str: The exercise category (e.g., 'Music Theory', 'Speed').
        """
        pass

    @abstractmethod
    def generate_exercise(self) -> Generator:
        """Generate exercise content.
        
        Returns:
            Generator: A generator yielding exercise items.
        """
        pass
