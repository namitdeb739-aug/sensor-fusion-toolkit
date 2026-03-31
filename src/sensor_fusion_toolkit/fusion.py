"""Sensor fusion module."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass
class SensorReading:
    """A single sensor reading with timestamp.

    Args:
        sensor_id: Unique identifier for the sensor.
        value: The sensor measurement value.
        timestamp: Unix timestamp of the reading.
    """

    sensor_id: str
    value: float
    timestamp: float


def fuse_readings(readings: list[SensorReading]) -> float:
    """Fuse multiple sensor readings using simple averaging.

    Args:
        readings: List of sensor readings to fuse.

    Returns:
        The average value across all readings.

    Raises:
        ValueError: If the readings list is empty.
    """
    if not readings:
        msg = "Cannot fuse empty readings list"
        raise ValueError(msg)
    return sum(r.value for r in readings) / len(readings)
