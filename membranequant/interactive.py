import numpy as np
import matplotlib.pyplot as plt
import ipywidgets as widgets


def plot_fits(target, fit):
    # Detect if single frame or stack
    if type(target) is list:
        stack = True
        target = target
        fit = fit
    elif len(target.shape) == 3:
        stack = True
        target = list(target)
        fit = list(fit)
    else:
        stack = False
        target = [target, ]
        fit = [fit, ]

    # Set up figure
    fig = plt.figure()
    gs = fig.add_gridspec(3, 3)
    ax1 = fig.add_subplot(gs[0, :])
    ax2 = fig.add_subplot(gs[1:, :])

    # Specify ylim
    straight_max = max([np.max(i) for i in target])
    straight_min = min([np.min(i) for i in target])
    fit_max = max([np.max(i) for i in fit])
    fit_min = min([np.min(i) for i in fit])
    ylim_top = max([straight_max, fit_max])
    ylim_bottom = min([straight_min, fit_min])

    if stack:

        @widgets.interact(Frame=(0, len(target) - 1, 1), Position=(0, 1, 0.01))
        def update(Frame=0, Position=0.1):
            position = int(Position * target[int(Frame)].shape[1] - 1)

            ax1.clear()
            ax1.imshow(target[int(Frame)], cmap='gray', vmin=ylim_bottom, vmax=1.1 * ylim_top)
            ax1.axvline(position, c='r')
            ax1.set_yticks([])
            ax1.set_xlabel('Position')
            ax1.xaxis.set_label_position('top')

            ax2.clear()
            ax2.plot(target[int(Frame)][:, position], label='Actual')
            ax2.plot(fit[int(Frame)][:, position], label='Fit')
            ax2.set_xticks([])
            ax2.set_ylabel('Intensity')
            ax2.legend(frameon=False, loc='upper left', fontsize='small')
            ax2.set_ylim(bottom=ylim_bottom, top=ylim_top)

    else:

        @widgets.interact(Position=(0, 1, 0.01))
        def update(Position=0.1):
            position = int(Position * (target[0].shape[1] - 1))

            ax1.clear()
            ax1.imshow(target[0], cmap='gray', vmin=ylim_bottom, vmax=1.1 * ylim_top)
            ax1.axvline(position, c='r')
            ax1.set_yticks([])
            ax1.set_xlabel('Position')
            ax1.xaxis.set_label_position('top')

            ax2.clear()
            ax2.plot(target[0][:, position], label='Actual')
            ax2.plot(fit[0][:, position], label='Fit')
            ax2.set_xticks([])
            ax2.set_ylabel('Intensity')
            ax2.legend(frameon=False, loc='upper left', fontsize='small')
            ax2.set_ylim(bottom=ylim_bottom, top=ylim_top)

    fig.set_size_inches(5, 3)
    fig.tight_layout()

    return fig, (ax1, ax2)
