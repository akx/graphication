#!/usr/bin/python

from __future__ import absolute_import
import random
from graphication import FileOutput, Series, SeriesSet, Label, SimpleScale, css
from graphication.linegraph import LineGraph
from six.moves import range


def randomvalues(n):
    return dict([(i, random.choice(list(range(2, 25)))) for i in range(n)])


def main():
    # Create a random multiseries
    num_points = 10

    series_set = SeriesSet()
    for i in range(2):
        series_set.add_series(Series(
            "Series%s" % i,
            randomvalues(num_points),
            "#3366%2xff" % (50*i),
            {0: i % 3, 5: 0},
        ))

    # Create the output
    output = FileOutput()

    # We'll have major lines every integer, and minor ones every half
    scale = SimpleScale(0, num_points-1, 1)

    # OK, render that.
    wg = LineGraph(series_set, scale, None)
    lb = Label("Test Graph", None)

    output.add_item(lb, x=10, y=5, width=490, height=20)
    output.add_item(wg, x=0, y=30, width=500, height=200)

    # Save the images
    output.write("pdf", "random_linegraph.pdf")


if __name__ == '__main__':
    main()
