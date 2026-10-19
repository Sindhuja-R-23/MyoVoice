# MyoVoice Hardware Integration

This directory contains hardware-related code and documentation for integrating the MyoVoice silent-speech recognition system with an EMG sensor and ESP32.

Planned components:
- EMG signal acquisition.
- ESP32-based sensor data collection.
- Serial communication for transferring sensor readings.
- Signal-quality checks and hardware testing.
- Future integration with the MyoVoice recognition pipeline.

The hardware implementation will be documented and tested when the physical components are available. Sensor readings must be validated before connecting them to the trained model.

## Safety

Follow the sensor manufacturer's wiring and power requirements. Protect the ESP32 from excessive input voltage, and use an appropriate battery-powered or isolated arrangement for body-connected measurements.
