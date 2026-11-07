import pytest
from fluid import wave


@pytest.mark.skip(reason="not implemented yet")
def test_deep_water_wavelength():
    # Lecture example: lambda0 = 100 m -> T ~ 8.006 s
    assert wave.wavelength(T=8.006, d=1000.0) == pytest.approx(100.0, rel=1e-2)


@pytest.mark.skip(reason="not implemented yet")
def test_shoaling_example_16m():
    # Lecture example: d = 16 m -> k ~ 0.0752 1/m, lambda ~ 83.55 m, a/a0 ~ 0.9127
    k, lam, a = wave.shoal(a0=1.0, T=8.006, d=16.0)
    assert lam == pytest.approx(83.55, rel=1e-2)
    assert a == pytest.approx(0.9127, rel=1e-2)
