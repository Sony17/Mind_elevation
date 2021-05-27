from AccelBrainBeat.brainbeat.binaural_beat import BinauralBeat
from AccelBrainBeat.brainbeat.monaural_beat import MonauralBeat
import sounddevice as sd
import soundfile as sf
import soothingsounds
from gtts import gTTS
from pydub import AudioSegment


# Create Binural Beats
def create_binural_beats(left_frequency, right_frequency):
    """Generate Binural Beats"""
    brain_beat = BinauralBeat()  # for binaural beats.
    brain_beat.save_beat(
        output_file_name="save_binaural_beat.wav",
        frequencys=(left_frequency, right_frequency),
        play_time=10,
        volume=0.01
    )


def create_monaural_beats(left_frequency, right_frequency):
    brain_beat_monaural = MonauralBeat()  # for monaural beats.
    brain_beat_monaural.save_beat(
        output_file_name="save_monaural_beat.wav",
        frequencys=(left_frequency, right_frequency),
        play_time=10,
        volume=0.01
    )


def play_wav(sound_filename):
    data, fs = sf.read(sound_filename, dtype='float32')
    sd.play(data, fs)
    status = sd.wait()


def crete_color_noise(color, sample_rate):
    return soothingsounds.noise(sample_rate, color)


# need to adjust decibel for audio
def adjust_decibels():
    """Adjust sound levels"""
    pass


def text_to_speech(affirmations):
    """Convert text to speech"""
    affirmations = 'Hello ? type the affirmations'
    language = 'en'
    # Support multiple languages
    computer_voice_object = gTTS(text=affirmations, lang=language, slow=False)
    computer_voice_object.save("affirmation.wav")


def upload_your_voice():
    """Upload your voice """
    pass


def overlap_sound_files():
    """Overlap Multiple sound Files"""
    sound1 = AudioSegment.from_file("save_binaural_beat.wav")
    sound2 = AudioSegment.from_file("welcome.wav")
    combined = sound1.overlay(sound2)
    combined.export("combined.wav", format='wav')
    """To test """


create_binural_beats(400, 430)
overlap_sound_files()

# TODO Design the GUI.
# TODO Create GUI using tkinter .
# TODO Get Images/upload images
# TODO Get soothing Audio files.
# TODO Refactor code
# TODO Create Audio Visualization.
# TODO Research more on the topic and document
# TODO: create functionality to detect the frequencies from audio
# TODO: Do file opening and closing properly
