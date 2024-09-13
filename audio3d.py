# audio3d.py
import numpy as np
import pyaudio
from scipy.io.wavfile import read
from scipy.io import loadmat
import threading

class Audio3D:
    def __init__(self):
        self.hrir_l, self.hrir_r, self.azimuths = self.load_hrir_data()
        self.fs, self.audio_data = self.load_wav('sound1.wav')
        self.pyaudio_instance = pyaudio.PyAudio()
        self.stream = self.pyaudio_instance.open(format=pyaudio.paFloat32,
                                                 channels=2,
                                                 rate=self.fs,
                                                 output=True)
        self.lock = threading.Lock()
        self.audio_thread = None

    def load_hrir_data(self):
        hrir = loadmat('cipic_hrir/hrir_final.mat')
        hrir_l = hrir['hrir_l'][:, 49, :] / np.max(hrir['hrir_l'])
        hrir_r = hrir['hrir_r'][:, 49, :] / np.max(hrir['hrir_r'])
        azimuths = np.linspace(-80, 80, len(hrir_l))
        return hrir_l, hrir_r, azimuths

    def load_wav(self, filename):
        fs, data = read(filename)
        if data.ndim > 1:
            data = data.mean(axis=1)
        return fs, data.astype(np.float32) / np.max(np.abs(data))

    def play_3d_sound(self, azimuth):
        if self.audio_thread is not None and self.audio_thread.is_alive():
            return
        self.audio_thread = threading.Thread(target=self.process_audio, args=(azimuth,))
        self.audio_thread.start()

    def process_audio(self, azimuth):
        with self.lock:
            idx = np.argmin(np.abs(self.azimuths - azimuth))
            filtered_l = np.convolve(self.audio_data, self.hrir_l[idx], mode='same')
            filtered_r = np.convolve(self.audio_data, self.hrir_r[idx], mode='same')
            stereo_signal = np.vstack((filtered_l, filtered_r)).T
            self.stream.write(stereo_signal.astype(np.float32).tobytes())

    def close_audio(self):
        if self.audio_thread:
            self.audio_thread.join()
        self.stream.stop_stream()
        self.stream.close()
        self.pyaudio_instance.terminate()
