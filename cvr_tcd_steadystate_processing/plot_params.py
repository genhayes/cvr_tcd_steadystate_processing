# G. Hayes 2023
# This file contains the pltting parameters used in the analysis in:
# S. Sparks, G. Hayes, J. Pinto, and D. Bulte, “Characterising cerebrovascular reactivity and the pupillary light response–a comparative study,” Front. Physiol., vol. 15, Aug. 2024, doi: 10.3389/fphys.2024.1384113.

from matplotlib import rcParams
from cycler import cycler

def define_params():
    # print("Setting plot parameters...")
    # -- Figure --
    rcParams['figure.figsize'] = (25.0, 15.0)
    rcParams['figure.dpi'] = 300
    rcParams['figure.facecolor'] = 'white'
    rcParams['figure.edgecolor'] = 'white'
    rcParams['figure.autolayout'] = True

    # -- Axes --
    rcParams['axes.titlesize'] = 20
    rcParams['axes.labelsize'] = 30
    rcParams['xtick.labelsize'] = 20
    rcParams['ytick.labelsize'] = 20
    rcParams['legend.fontsize'] = 20

    # -- Fonts --
    rcParams['font.size'] = 16
    rcParams['font.family'] = 'serif'
    rcParams['text.color'] = 'black'
    rcParams['axes.labelcolor'] = 'black'

    # -- Plot Styles --
    rcParams['lines.linewidth'] = 3
    navy = (56 / 256, 74 / 256, 143 / 256)
    teal = (106 / 256, 197 / 256, 179 / 256)
    pink = [199 / 255, 99 / 255, 150 / 255]
    rcParams['axes.prop_cycle'] = cycler(color=[teal, pink, teal])