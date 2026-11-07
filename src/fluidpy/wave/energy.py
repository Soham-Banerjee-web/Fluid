"""Wave energy and energy flux, lecture section 4 (per unit area / crest width)."""


def potential_energy(a, rho=1025.0, g=9.81):
    """PE = rho g a^2 / 4 (eq 4.1)."""
    raise NotImplementedError


def kinetic_energy(a, rho=1025.0, g=9.81):
    """KE = rho g a^2 / 4 (eq 4.2)."""
    raise NotImplementedError


def total_energy(a, rho=1025.0, g=9.81):
    """E = rho g a^2 / 2 (eq 4.3)."""
    raise NotImplementedError


def energy_flux(a, T, d, rho=1025.0, g=9.81):
    """Energy flux E * cg."""
    raise NotImplementedError
