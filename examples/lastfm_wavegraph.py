#!/usr/bin/python

from __future__ import absolute_import
from __future__ import print_function
import os
import sys
import time
import random
import datetime
from graphication import SeriesSet, Series, css, Colourer, FileOutput, AutoWeekDateScale, Label
from graphication.wavegraph import WaveGraph


def p(x):
    print("%3.0f%% complete" % (x*100,))


def get_fake_lastfm_data():
    ts1 = datetime.datetime(2018, 4, 1).timestamp()
    ts2 = datetime.datetime(2018, 4, 7).timestamp()
    ts3 = datetime.datetime(2018, 4, 14).timestamp()

    return {
        'Artist 1': [(ts1, 100), (ts2, 200), (ts3, 10)],
        'Artist 2': [(ts1, 200), (ts2, 100), (ts3, 80)],
        'Artist 3': [(ts2, 200), (ts3, 100)],
    }


def main():
    artists = get_fake_lastfm_data().items()

    # Create the series set and throw in the artists

    series_set = SeriesSet()
    for artist, plays in artists:
        series_set.add_series(Series(
            artist,
            dict(plays),
        ))

    # Initialise our style
    style = css.CssStylesheet.from_css(os.path.join(os.path.dirname(__file__), './lastgraph.css'))

    # Colour that set!
    cr = Colourer(style)
    cr.colour(series_set)

    # Create the output
    output = FileOutput(style)

    # Weeky scale
    scale = AutoWeekDateScale(series_set)

    # OK, render that.
    wg = WaveGraph(series_set, scale, style, label_curves=True)
    lb = Label("username", style)

    width = 30*len(list(series_set.keys()))
    output.add_item(lb, x=10, y=5, width=width-20, height=20)
    output.add_item(wg, x=0, y=30, width=width, height=200)

    # Save the images
    output.write("pdf", "fake_lastfm.pdf")


if __name__ == '__main__':
    main()
