import numpy as np
import music21

def herremans_chew_spiral(tone_set):
    """
    TODO
    """
    return


def simple_lerdahl(pitch_classes, tonic_class):
    """
    Computes tonal tension based on Lerdahl's model.
    We're ignoring spelling here, taking the "more tense" of either spelling

    Parameters:
    pitch_classes (list): List of pitch classes (0-11, where 0 = C, 1 = C#, ..., 11 = B)
    tonic_class (int): The equivalent MAJOR tonic pitch class (0-11)

    Returns:
    float: The computed tonal tension.
    """

    # Tension values for each pitch class based on their position in Lerdhal's "pitch-space hierarchy"
    tension_values = {
        0: 0,   # Tonic
        1: 6,   # Minor second
        2: 4,   # Major second
        3: 5,   # Minor third
        4: 3,   # Major third
        5: 4,   # Perfect fourth
        6: 6,   # Tritone
        7: 2,   # Perfect fifth
        8: 5,   # Minor sixth
        9: 4,   # Major sixth
        10: 5,  # Minor seventh
        11: 4   # Major seventh
    }

    total_tension = 0.0
    for pitch in pitch_classes:
        distance = (pitch - tonic_class) % 12
        total_tension += tension_values[distance]

    return total_tension
