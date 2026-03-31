import pytest

from sensor_fusion_toolkit.fusion import SensorReading, fuse_readings


def test_fuse_single_reading() -> None:
    readings = [SensorReading("lidar", 1.5, 1000.0)]
    assert fuse_readings(readings) == 1.5


def test_fuse_multiple_readings() -> None:
    readings = [
        SensorReading("lidar", 1.0, 1000.0),
        SensorReading("radar", 2.0, 1000.1),
        SensorReading("camera", 3.0, 1000.2),
    ]
    assert fuse_readings(readings) == pytest.approx(2.0)


def test_fuse_empty_raises() -> None:
    with pytest.raises(ValueError, match="Cannot fuse empty"):
        fuse_readings([])
