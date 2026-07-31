"""Health and Quality of Life Outcomes submission runner (Playwright).

Thin binding for the Springer Nature "Snapp" platform implemented in
:mod:`paperpush.venues.snapp.main`: selects the Health and Quality of Life
Outcomes :class:`~paperpush.venues.snapp.main.Variant` and exposes the uniform
``VENUE`` object plus the ``login_hqlo`` sign-in-and-hold entry point.
"""

from __future__ import annotations

from . import main
from .main import (  # noqa: F401 -- re-exported as this module's public API
    SnappLoginError,
    Variant,
)


class HealthQualityLifeOutcomesVenue(main.SnappVenue):
    """Health and Quality of Life Outcomes on Springer Nature Snapp."""

    slug = "hqlo"
    variant = main.VARIANTS["hqlo"]


VENUE = HealthQualityLifeOutcomesVenue()


def login_hqlo(headless: bool = False, new_session: bool = False) -> None:
    """Open HQLO, sign in, and leave the browser open (see :func:`main.login`)."""
    main.login(VENUE, headless=headless, new_session=new_session)
