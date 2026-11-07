"""Waves advancing into shallow water, lecture section 3.

Assumes slowly varying depth and no energy losses: T constant,
(a^2/k) [1 + 2kd/sinh(2kd)] = constant (eq 3.1).
"""


def shoaling_coefficient(T, d, g=9.81):
    """a / a0 at depth d for a wave of period T."""
    raise NotImplementedError


def shoal(a0, T, d, g=9.81):
    """Return (k, wavelength, a) at depth d given deep-water amplitude a0 and period T."""
    raise NotImplementedError
