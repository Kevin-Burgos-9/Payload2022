import rtlsdr
import numpy as np
import scipy.signal as signal
import sounddevice as sd
import aprslib

# SDR settings
center_frequency = 144.39e6
gain = 20
sample_rate = 48000
f_dev = 1200
nyquist_rate = sample_rate / 2
low_cutoff = 1200 - f_dev
high_cutoff = 1200 + f_dev

# APRS settings
callsign = "YOUR_CALLSIGN"
destination = "APRS"
message = "Hello, world!"

# Open a connection to the SDR device
sdr = rtlsdr.RtlSdr()
sdr.fc = center_frequency
sdr.gain = gain

# Generate the APRS packet string
packet = aprslib.parse(f"{callsign}>{destination}:{message}")
aprs_string = packet.encode()

# Generate the modulating signal
modulating_signal = np.array([1 if c == '1' else -1 for c in aprs_string]).repeat(8)

# Generate the carrier frequency
t = np.linspace(0, len(modulating_signal) / sample_rate, len(modulating_signal), endpoint=False)
carrier_signal = np.sin(2 * np.pi * 1200 * t)

# Modulate the carrier with the modulating signal
modulated_signal = carrier_signal * modulating_signal

# Apply a bandpass filter to remove frequencies outside of the passband
b, a = signal.butter(4, [low_cutoff / nyquist_rate, high_cutoff / nyquist_rate], 'bandpass')
filtered_signal = signal.filtfilt(b, a, modulated_signal)

# Start the audio output stream
sd.default.samplerate = sample_rate
sd.default.channels = 1
stream = sd.OutputStream(blocksize=4800)

# Transmit the filtered signal in chunks
with stream:
    for i in range(0, len(filtered_signal), 4800):
        chunk = filtered_signal[i:i+4800].astype(np.float32)
        stream.write(chunk)

# Close the SDR connection
sdr.close()
