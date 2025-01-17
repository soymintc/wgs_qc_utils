import numpy as np
from . import input_checker
import pandas as pd
from wgs_qc_utils.utils.empty import empty_plot


def plot_scatter(pos, frac_cn, axis, logistic_y=False):
    if not isinstance(pos, pd.Series) and not isinstance(frac_cn, pd.Series):
        return empty_plot(axis, "Snv Cn", snv_cn=True)

    input_checker.check_input_is_valid([pos, frac_cn],
                                            [input_checker.CheckerTypes.NUMERIC,
                                             input_checker.CheckerTypes.FLOAT])

    if logistic_y:
        squash_coeff = 0.15
        squash_f = lambda a: np.tanh(squash_coeff * a)
        frac_cn = squash_f(frac_cn)
    else:
        frac_cn = frac_cn
    axis.scatter(pos/1000000, frac_cn, color="black", s=2.5, marker="o", alpha=1)
    return axis


def plot_hist(frac_cn, axis, logistic_y=False):
    if not isinstance(frac_cn, pd.Series):
        return empty_plot(axis, "Snv cn", snv_cn=True)
    if frac_cn.empty:
        axis.set_ylim(0, 8)
        axis.set_ylabel("SNV density")
        return axis

    input_checker.check_input_is_valid([frac_cn],
                                            [input_checker.CheckerTypes.FLOAT])
    if logistic_y:
        squash_coeff = 0.15
        squash_f = lambda a: np.tanh(squash_coeff * a)
        frac_cn = squash_f(frac_cn)
        yticks = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 10, 20])
        yticks_squashed = squash_f(yticks)
        ytick_labels = [str(a) for a in yticks]
        axis.set_yticks(yticks_squashed)
        axis.set_yticklabels(ytick_labels)
        axis.set_ylim((-0.01, 1.01))
        axis.spines['left'].set_bounds(0, 1)
    else:
        axis.set_ylim(0, 8)
        frac_cn = frac_cn
    axis.hist(frac_cn, color="black", orientation="horizontal", bins=15)
    axis.set_ylabel("SNV density")
    return axis
