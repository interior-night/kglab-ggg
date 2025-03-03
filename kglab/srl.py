#!/usr/bin/env python
# -*- coding: utf-8 -*-
# see license https://github.com/DerwenAI/kglab\#license-and-copyright

"""
Support for use of statistical relational learning.
"""

import pathlib
import typing

from icecream import ic  # type: ignore  # pylint: disable=E0401
import pandas as pd  # type: ignore  # pylint: disable=E0401


class PSLModel:
    """
Class representing a
[*probabilistic soft logic*](../glossary/#probabilistic-soft-logic)
(PSL) model.

For PSL-specific terminology used here, see <https://psl.linqs.org/wiki/master/Glossary.html\>

Note: This is a stub implementation. The actual PSL functionality has been removed
to avoid requiring jpype1. If you need PSL functionality, please use the original
kglab package.
    """

    def __init__(self, *args, **kwargs):
        """
        Initialize a PSLModel instance.
        This is a stub implementation that raises NotImplementedError.
        """
        raise NotImplementedError(
            "PSL functionality has been removed from this fork to avoid jpype1 dependency. "
            "If you need PSL support, please use the original kglab package."
        )
