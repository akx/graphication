#!/usr/bin/python

from __future__ import absolute_import
import random
from graphication import FileOutput, Node, NodeSet, NodeLink, Label, SimpleScale, css, default_css as style
from graphication.forcerel import ForceRelPlot


def main():
    # Create the NodeSet, and add some nodes to it
    nodeset = NodeSet()

    n = 30

    for i in range(n):
        node = Node(random.choice(list(range(10))))
        nodeset.add_node(node)

    # Add some test links
    for i in range(20):
        nodeset.add_link(NodeLink(random.choice(nodeset.nodes), random.choice(nodeset.nodes)))

    # Make a scale
    value_min, value_max, value_range = nodeset.value_range()
    scale = SimpleScale(value_min, value_max, 1, 1)

    # Create the output
    output = FileOutput(style)

    # OK, render that.
    forcerel = ForceRelPlot(nodeset, style, scale)

    output.add_item(forcerel, x=0, y=0, width=200, height=600)

    # Save the images
    #output.write("svg", "forcerel.svg")
    #output.write("png", "forcerel.png")
    output.write("pdf", "forcerel.pdf")


if __name__ == '__main__':
    main()
