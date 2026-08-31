"""Placeholder test — keeps CI green until the package has a surface to test."""

import kc


def test_version_is_the_repurposed_series():
    """kc <= 0.0.7 was an unrelated package; the rewrite starts at 0.0.8."""
    major, minor, patch = (int(p) for p in kc.__version__.split("."))
    assert (major, minor, patch) >= (0, 0, 8)
