# -*- coding: utf-8 -*-
""" Box Plot test

This test plots a box plot with three data series. The causes an empty Line2D
to be plotted.  Without care, this can turn into an empty table in PGFPlot
which crashes latex (due to it treating an empty table as a table with
external data in the file '' or '.tex')
See: https://github.com/nschloe/matplotlib2tikz/pull/134
"""
import os

import matplotlib.pyplot as plt

import matplotlib2tikz as m2t


def plot():
    # plot data
    fig = plt.figure()
    ax = fig.add_subplot(111)

    data = [
        [
            0.8792419963142024,
            0.8842648555256405,
            0.8830545971510088,
            0.8831310510125482,
            0.8839926059865629,
            0.8795815040451961,
            0.8780455489941472,
            0.8785436398314896,
            0.8830947020953477,
            0.8853267660041949,
            0.8888678711018956,
            0.8852975957910832,
            0.8806832729996307,
            0.8757157004574541,
            0.8767001155960863,
            0.8840806038864472,
            0.8817619814119265,
            0.8888364252374024,
            0.8812448127688732,
            0.8831027782255365,
        ],
        [
            0.8977874209274417,
            0.8941751386130553,
            0.8896779411432865,
            0.8971274869048325,
            0.8974081692527065,
            0.8942767272739647,
            0.8875248054826029,
            0.8777267389916926,
            0.8950411839136605,
            0.8927553406630346,
            0.8950822278376636,
            0.8987940094730611,
            0.8921713177345106,
            0.8875512496817447,
            0.8897284821652239,
            0.8910385725900226,
            0.8879321741542129,
            0.889056167587369,
            0.884905350828982,
            0.89214934207348,
        ],
        [
            0.8841888415170959,
            0.8922931655807687,
            0.8896153674950393,
            0.8875992162118492,
            0.890776178375901,
            0.8889109386518265,
            0.8879119743598638,
            0.8912870099488378,
            0.8981046527087161,
            0.8920725720963792,
            0.8841683225315845,
            0.8857539590587772,
            0.8945156112818913,
            0.8894879283167035,
            0.8912651966639861,
            0.8929190818922158,
            0.8943297597492411,
            0.8888594626359189,
            0.8912494597675972,
            0.8917524004164856,
        ],
    ]

    ax.boxplot(data)

    return fig


def test():
    plot()
    code = m2t.get_tikz_code(include_disclaimer=False)
    this_dir = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(this_dir, 'reference.tex'), 'r') as f:
        reference = f.read()[:-1]
    assert code == reference
    return