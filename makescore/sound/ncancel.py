from scipy.io import wavfile

def noise_cancel(wav_file_name):
    sr, samples = wavfile.read(wav_file_name)
    return sr, samples

def main():
    wav_file_name = './song/s1.wav' 
    print(noise_cancel(wav_file_name))
    print(type(noise_cancel(wav_file_name)))
    
if __name__ == '__main__':
    main()