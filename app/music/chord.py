from dataclasses import dataclass
from typing import List


@dataclass
class Chord:
    """Represents a musical chord with root note, quality, extensions, and alterations.
    
    A chord is defined by its root note (e.g., 'C', 'D#'), quality (e.g., 'maj', 'min'),
    optional extensions (e.g., [7, 9] for a 7add9), and optional alterations (e.g., ['b5', '#9']).
    
    Attributes:
        root (str): The root note of the chord.
            Possible values:
            ['Ab', 'A', 'A#', 'Bb', 'B', 'C', 'C#', 'Db', 'D', 'D#', 'Eb', 'E', 'F', 'F#', 'Gb',
            'G', 'G#']

        quality (str): The chord quality/type.
            Possible values: ['', 'm', 'dim'].

        extensions (List[int], optional): Numeric extensions to the chord (e.g., [7, 9]).
            -- To be implemented --

        alterations (List[str], optional): String representations of altered notes 
            -- To be implemented --
    
    Examples:
        >>> chord = Chord('C', '', extensions=[7])
        >>> chord.display_name()
        'C7'
        
        >>> chord = Chord('D', 'min', alterations=['b5'])
        >>> chord.display_name()
        'Dminb5'
    """

    root: str
    quality: str
    extensions: List[int] = None
    alterations: List[str] = None

    def display_name(self) -> str:
        """Generate a string representation of the chord.
        
        Concatenates the root, quality, extensions, and alterations into a single
        chord name string suitable for display to users.
        
        Returns:
            str: The complete chord name (e.g., 'Cmaj7', 'Dm7b5').
        """
        ext = "".join(str(e) for e in self.extensions or [])
        alt = "".join(str(e) for e in self.alterations or [])
        return f"{self.root}{self.quality}{ext}{alt}"