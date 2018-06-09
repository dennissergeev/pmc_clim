# -*- coding: utf-8 -*-
"""
Paths to data

Depends on path.py package
"""
from pathlib import Path

# Top-level directory containing code and data (one level up)
topdir = Path('.').absolute().parent

# Temporary
phddir = Path.home()/'phd'
plotdir = phddir/'plots'/'climatology'

# Output directories
# plotdir = topdir/'figures'

# Reanalyses
era5_dir = phddir/'reanalysis'/'era5'
interim_dir = phddir/'reanalysis'/'interim'

# Tracking
pmctrackdir = phddir/'pmc_tracking'/'pmctrack'
trackresdir = phddir/'pmc_tracking'/'results'
procdir = phddir/'pmc_tracking'/'results'/'processed_data'
runsgridfile = trackresdir/'runs_grid.json'
