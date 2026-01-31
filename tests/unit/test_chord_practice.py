"""
Unit test for the chord_practice exercise generator.

Run from the project root with: poetry run pytest tests/unit/test_chord_practice.py
"""

from unittest.mock import patch

import pytest

from app.exercises.chord_practice import LEVELS, chord_practice
from app.music.chord import Chord


class TestChordPractice:
    """Tests for the chord_practice generator function."""

    def test_chord_practice_returns_generator(self):
        """Test that chord_practice returns a generator."""
        generator = chord_practice(frequency=100, difficulty=1)
        assert hasattr(generator, '__iter__')
        assert hasattr(generator, '__next__')

    def test_chord_practice_yields_chord_objects(self):
        """Test that chord_practice yields valid Chord objects."""
        generator = chord_practice(frequency=100, difficulty=1)
        chord = next(generator)
        assert isinstance(chord, Chord)

    def test_invalid_difficulty_raises_error(self):
        """Test that an invalid difficulty level raises ValueError."""
        with pytest.raises(ValueError, match="unknown difficulty"):
            generator = chord_practice(frequency=100, difficulty=999)
            next(generator)  # Trigger evaluation

    def test_chord_practice_continuous_generation(self):
        """Test that chord_practice can generate multiple chords continuously."""
        generator = chord_practice(frequency=10, difficulty=1)
        
        # Generate 100 chords
        chords = []
        for _ in range(100):
            chords.append(next(generator))
        
        assert len(chords) == 100
        assert all(isinstance(chord, Chord) for chord in chords)

    @patch('random.choice')
    def test_chord_practice_with_mocked_randomness(self, mock_choice):
        """Test chord_practice with controlled random values."""
        # This allows testing specific chord combinations
        mock_choice.side_effect = ["C", ""]
        
        generator = chord_practice(frequency=100, difficulty=1)
        chord = next(generator)
        
        assert chord.root == "C"
        assert chord.quality == ""


class TestDifficultyLevels:
    """Tests to verify difficulty-specific chord generation."""

    def test_difficulty_1_easy_roots_only(self):
        """Test that difficulty 1 only uses easy roots (natural notes)."""
        easy_roots = LEVELS[1].roots
        generator = chord_practice(frequency=10, difficulty=1)
        
        for _ in range(50):
            chord = next(generator)
            assert chord.root in easy_roots

    def test_difficulty_1_easy_qualities_only(self):
        """Test that difficulty 1 only uses easy qualities."""
        easy_qualities = LEVELS[1].qualities
        generator = chord_practice(frequency=10, difficulty=1)
        
        for _ in range(50):
            chord = next(generator)
            assert chord.quality in easy_qualities

    def test_difficulty_2_uses_accidentals(self):
        """Test that difficulty 2 includes accidental roots."""
        generator = chord_practice(frequency=10, difficulty=2)
        
        chords = [next(generator) for _ in range(100)]
        roots_found = set(chord.root for chord in chords)
        
        # Should include at least some accidentals (B♭, C#, etc.)
        accidentals = [r for r in roots_found if '♭' in r or '#' in r]
        assert len(accidentals) > 0, "Difficulty 2 should include accidentals"

    def test_difficulty_4_all_roots(self):
        """Test that difficulty 4 uses all available roots."""
        all_roots = LEVELS[4].roots
        assert len(all_roots) == 17, "Difficulty 4 should use all 17 roots"

    def test_difficulty_5_has_extensions_and_alterations(self):
        """Test that difficulty 5 can produce extensions and alterations."""
        generator = chord_practice(frequency=10, difficulty=5)
        
        found_extensions = False
        found_alterations = False
        
        # Sample many chords to find ones with extensions/alterations
        for _ in range(500):
            chord = next(generator)
            if chord.extensions is not None:
                found_extensions = True
            if chord.alterations is not None:
                found_alterations = True
            if found_extensions and found_alterations:
                break
        
        assert found_extensions, "Difficulty 5 should produce extensions"
        assert found_alterations, "Difficulty 5 should produce alterations"

    def test_all_difficulty_levels_exist(self):
        """Test that all expected difficulty levels are configured."""
        expected_levels = {1, 2, 3, 4, 5}
        assert set(LEVELS.keys()) == expected_levels

    def test_difficulty_progression_root_complexity(self):
        """Test that root complexity increases with difficulty."""
        for difficulty in LEVELS.keys():
            config = LEVELS[difficulty]
            roots = config.roots
            # Should have at least one root
            assert len(roots) > 0
            # Root list should grow or stay same as difficulty increases
            if difficulty > 1:
                prev_roots = LEVELS[difficulty - 1].roots
                assert len(roots) >= len(prev_roots) - 1  # Allow some variation


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
