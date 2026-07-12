from typing import Dict, TypedDict
from pygame import mixer
from utils import load_sound

mixer.init()


# ty. will. not. leave. me. ALONE!
class SoundData(TypedDict):
    muted: bool
    sound: mixer.Sound


SOUNDS: Dict[str, SoundData] = {
    "fire": {"muted": False, "sound": load_sound("fire")},
    "background": {"muted": False, "sound": load_sound("background")},
}


def play_sound(name: str, loops: int = 0) -> None:
    sound = SOUNDS[name]["sound"]
    sound.play(loops)


def toggle_mute_all():
    for sound in SOUNDS.values():
        sound["muted"] = not sound["muted"]
        sound["sound"].set_volume(0 if sound["muted"] else 1)
