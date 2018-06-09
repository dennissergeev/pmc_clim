# -*- coding: utf-8 -*-
"""
Common objects for PMC climatology analysis code
"""
import calendar
import string

import numpy as np


iletters = iter(string.ascii_lowercase)

cat_kw = dict(filt_by_time=True, filt_by_dist=True, filt_by_vort=True,
              filt_by_domain_bounds=True, filt_by_land=True,
              time_thresh0=6, time_thresh1=9,
              dist_thresh=300.0, type_thresh=0.2,
              vort_thresh0=0.0003, vort_thresh1=0.00045, coast_rad=70.)

toponyms = [
    dict(name='Svalbard', lon=14, lat=79),
    dict(name='Greenland', lon=-21, lat=80),
    dict(name='Norway', lon=23, lat=70),
    dict(name='Fram Strait', lon=-5, lat=79),
    dict(name='Barents\nSea', lon=25, lat=73),
    dict(name='Norwegian\nSea', lon=5, lat=70)
]

datasets = ['era5', 'interim']

START_YEAR = 2008
nyr = 9
winters = [f'{START_YEAR+i}_{START_YEAR+i+1}' for i in range(nyr)]
winter_dates = {k: (f"{k.split('_')[0]}-10-01", f"{k.split('_')[1]}-04-30") for k in winters}

ndays_per_month_total = np.zeros((12), dtype=int)
for yr in range(START_YEAR, START_YEAR + nyr):
    ndays_per_month_total += np.array(calendar.mdays[1:])
    if calendar.isleap(yr+1):  # +1 because we start from autumn
        ndays_per_month_total[1] += 1

month_weights = 30 / ndays_per_month_total