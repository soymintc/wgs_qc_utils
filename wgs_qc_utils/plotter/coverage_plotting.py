from . import input_checker
from . import gene_annotation_plotting


def plot(start, coverage, ylim_min, ylim_max, axis, name, chrom_max, anno_genes=[]):
    """
    plot coverage data on an axis
    :param prepped_coverage: prepped coverage data
    :param ylim_min: min for y axis
    :param ylim_max: max for y axis
    :param axis: axis to plot on
    :param name: name for axis (i.e. normal or tumour coverage)
    :return: axis with plot
    # """

    if coverage.empty:
        return axis
        
    input_checker.check_input_is_valid([start, coverage],
                                     [input_checker.CheckerTypes.NUMERIC,
                                      input_checker.CheckerTypes.FLOAT])

    axis.set_xlim(0, chrom_max)

    axis.spines['top'].set_visible(False)
    axis.spines['right'].set_visible(False)
    axis.set_xticklabels([])

    
    for tic in axis.xaxis.get_major_ticks():
        tic.tick1On = tic.tick2On = False

    axis.fill_between(start / 1000000, ylim_min,
                      coverage, facecolor='black', alpha=0.5)

    axis.set_ylabel(name, fontsize=14, fontname="Arial")

    axis.set_ylim(ylim_min, ylim_max)

    if any(anno_genes):
        axis = gene_annotation_plotting.plot_anno_genes(anno_genes, axis.get_ylim()[0], axis.get_ylim()[1], axis)

    return axis
