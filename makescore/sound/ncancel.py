import soundfile as sf
import numpy as np
from . import s_fft

def noise_cancel(data, sr):
    time_space = np.shape(data)[0]

    return

def main():
    sound_file_name = 'song/s1.wav' 
    data, sr = get_sound_file(sound_file_name)


if __name__ == '__main__':
    main()