from sound import ncancel
from sound import s_fft
from sound import s_process
import matplotlib.pyplot as plt

if __name__ == "__main__":
    sound_file_name = 'song/s1.wav'
    data, sr = s_process.get_sound_file(sound_file_name)
    x, y, freqs, fft_vals = s_fft.basic_fft(data,sr)
    print(x, y, freqs, fft_vals)
    plt.figure(1)
    plt.plot(x,y)
    plt.figure(2)
    plt.plot(freqs, fft_vals)
    plt.show()
    # noise_cancel
