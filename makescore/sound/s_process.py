import soundfile as sf


def get_sound_file(sound_file_name):
    data, sr = sf.read(sound_file_name)
    return data, sr