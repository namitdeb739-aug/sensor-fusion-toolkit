import pytest

from sensor_fusion_toolkit.main import main


def test_main(capsys: pytest.CaptureFixture[str]) -> None:
    main()
    captured = capsys.readouterr()
    assert "Hello from sensor-fusion-toolkit!" in captured.out
