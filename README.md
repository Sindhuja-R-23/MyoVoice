# MyoVoice

**Silent-Speech Recognition Using Surface Electromyography (sEMG)**

MyoVoice is a research and development project that aims to recognize silently mouthed speech using muscle activity signals captured by surface electromyography (sEMG). The project explores how machine learning can interpret these signals and convert the predicted words into visible text and audible speech.

The goal is to develop an alternative communication interface for situations where conventional audible speech may not be practical.

## Project Vision

To develop a silent-speech communication system that interprets relevant muscle activity associated with attempted speech and produces understandable text and audio output without depending on audible speech during inference.

## Objectives

- Acquire and study sEMG signals associated with speech-related muscle activity.
- Preprocess EMG signals to reduce noise and prepare them for machine learning.
- Develop and evaluate a model for predicting silently mouthed words or phrases.
- Display the model's predictions on a user-friendly dashboard.
- Convert predicted text into audible speech through a separate audio-output module.
- Explore integration with an EMG sensor and an ESP32-based hardware system.
- Evaluate the system's performance, limitations, and suitability for future real-time use.

## Proposed System Architecture

1. **Signal acquisition:** Capture speech-related muscle activity using an EMG sensor.
2. **Signal processing:** Filter, normalize, and prepare the acquired signals.
3. **Machine learning:** Learn patterns in EMG signals and predict the intended word or phrase.
4. **Text visualization:** Display the predicted output on a dashboard.
5. **Audio output:** Convert the predicted text into speech using a speech-synthesis module.
6. **Hardware integration:** Explore acquisition and inference using an EMG sensor connected to an ESP32.

A microphone may be used during data collection and validation to provide reference audio and help establish the correct labels. The intended silent-speech inference pathway must use EMG signals rather than microphone-based speech recognition.

## Technology Stack

- Python
- PyTorch
- NumPy and SciPy
- Matplotlib
- Google Colab
- EMG sensor and ESP32
- Python-based dashboard
- Text-to-speech engine

The final technology stack may change as development and compatibility testing progress.

## Repository Structure

```text
MyoVoice/
├── README.md
├── .gitignore
├── requirements.txt
├── notebooks/
├── data_processing/
├── model/
├── dashboard/
├── audio_output/
├── hardware/
├── evaluation/
└── docs/
```

These directories will be populated as the corresponding modules are implemented.

## Dataset and Research

The initial experiments use an existing research dataset containing EMG recordings and associated speech data.

Dataset source: [Voicing Silent Speech — Zenodo](https://doi.org/10.5281/zenodo.4064409)

Dataset access, attribution, and usage must follow the applicable license and terms. The dataset itself is not included in this repository.

## Evaluation

The model will be evaluated using held-out data and appropriate recognition metrics. Evaluation will distinguish between results on the research dataset and performance on the intended EMG hardware.

Results and limitations will be documented based on actual experiments.

## Current Development Status

**Stage:** Prototype development

- [ ] Organize the project repository and development environment.
- [ ] Implement and validate EMG preprocessing.
- [ ] Establish a reproducible machine-learning baseline.
- [ ] Evaluate word or phrase recognition on held-out data.
- [ ] Build the text-display dashboard.
- [ ] Integrate speech output.
- [ ] Test EMG sensor and ESP32 acquisition.
- [ ] Evaluate the integrated system and document its limitations.

Milestones will be updated as each component is implemented and tested.

## Limitations

Surface EMG measures electrical activity associated with muscle activation; it does not directly measure vocal-cord vibration. Performance may vary with sensor placement, individual differences, signal quality, and the speech task.

Results obtained using a research dataset do not establish that a model will work with a different sensor configuration without further validation. Real-time hardware performance and generalization remain to be experimentally evaluated.

## Project Purpose

MyoVoice explores the potential of EMG-based silent-speech recognition as an alternative communication interface. The project combines signal processing, machine learning, user-interface development, audio output, and embedded hardware exploration.

*This repository is under active development. Its documentation and implementation will evolve as experiments and validation progress.*
