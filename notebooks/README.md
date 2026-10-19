# MyoVoice Notebooks

This directory contains Jupyter and Google Colab notebooks used for developing and experimenting with the MyoVoice silent-speech recognition system.

## Purpose

The notebooks support experimentation with surface electromyography (sEMG) signals to recognize silently mouthed words or phrases using machine learning.

## Planned Experiments

- Inspect and understand the EMG research dataset.
- Preprocess EMG signals and reduce unwanted noise.
- Extract useful features from EMG recordings.
- Develop and train a machine-learning recognition model.
- Evaluate model predictions using held-out data.
- Visualize experimental results and document observations.

## Main Notebook

- `MyoVoice.ipynb` — Main notebook for dataset inspection, signal-processing experiments, model development, and evaluation.

## Development Environment

The notebooks are developed using Python and Google Colab. GPU acceleration may be used when available, but dataset inspection and suitable lightweight experiments can also run on a CPU.

## Dataset

The initial experiments use an existing research dataset containing EMG recordings and associated speech data.

The dataset is not stored in this repository. Users must obtain it separately and follow its applicable access, attribution, and usage requirements.

## Notes

Experiments and results will be documented as development progresses. Recognition accuracy and hardware compatibility will be reported only after testing.
