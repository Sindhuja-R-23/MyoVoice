# MyoVoice Audio Output

This directory contains the audio-output components of the MyoVoice silent-speech recognition system.

Planned features:
- Receive the word or phrase predicted by the EMG-based recognition model.
- Convert the predicted text into audible speech.
- Allow the user to play the generated speech.
- Support future integration with the MyoVoice dashboard.

Audio generation is a separate stage from silent-speech recognition. The system should generate speech from the model's predicted text rather than rely on microphone input during silent-speech inference.

The implementation and selected speech-synthesis technology will be documented as development progresses.
