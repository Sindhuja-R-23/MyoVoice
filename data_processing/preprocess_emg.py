
"""
MyoVoice: EMG signal preprocessing utilities.

Input:
    EMG array with shape (samples, channels).

The default sampling rate is 1000 Hz for the research dataset.
For the physical sensor, confirm the actual sampling rate before use.
"""

import numpy as np
from scipy.signal import butter, sosfiltfilt, iirnotch, filtfilt


def preprocess_emg(
    emg,
    sampling_rate=1000,
    highpass_hz=2.0,
    notch_hz=60.0,
    notch_quality=30.0,
):
    """Remove baseline drift and power-line interference from EMG data."""
    emg = np.asarray(emg, dtype=np.float64)

    if emg.ndim == 1:
        emg = emg[:, np.newaxis]

    if emg.ndim != 2:
        raise ValueError("EMG input must have shape (samples, channels).")

    if emg.shape[0] < 20 or emg.shape[1] < 1:
        raise ValueError("EMG input is too short or has no channels.")

    if not np.isfinite(emg).all():
        raise ValueError("EMG input contains NaN or infinite values.")

    if sampling_rate <= 0:
        raise ValueError("Sampling rate must be positive.")

    if not 0 < highpass_hz < sampling_rate / 2:
        raise ValueError("High-pass cutoff must be below Nyquist frequency.")

    processed = emg.copy()

    # Remove slow baseline drift.
    sos = butter(
        4,
        highpass_hz,
        btype="highpass",
        fs=sampling_rate,
        output="sos",
    )
    processed = sosfiltfilt(sos, processed, axis=0)

    # Remove the 50 Hz or 60 Hz mains component when present.
    if notch_hz is not None:
        if not 0 < notch_hz < sampling_rate / 2:
            raise ValueError("Notch frequency must be below Nyquist frequency.")

        b, a = iirnotch(
            w0=notch_hz,
            Q=notch_quality,
            fs=sampling_rate,
        )
        processed = filtfilt(b, a, processed, axis=0)

    return processed


if __name__ == "__main__":
    # Simple synthetic signal for a basic smoke test.
    fs = 1000
    t = np.arange(fs * 2) / fs
    example = (
        np.sin(2 * np.pi * 100 * t)
        + 0.5 * np.sin(2 * np.pi * 60 * t)
        + 2.0
    )

    result = preprocess_emg(example, sampling_rate=fs, notch_hz=60)

    print("Input shape:", example.shape)
    print("Output shape:", result.shape)
    print("Output finite:", np.isfinite(result).all())
