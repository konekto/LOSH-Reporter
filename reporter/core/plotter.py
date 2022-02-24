'''
This module uses matplotlib to plot figures for the report
'''
import logging
from pathlib import Path
import matplotlib.pyplot as plt

# turn out matplotlib fontmanager debug logger otherwise it writes hunderts of lines in logfile
logging.getLogger('matplotlib.font_manager').disabled = True


def create_bar_chart(xvalues, yvalues, title, ylabel, path)-> None:
    '''
    Plots a bar chart for the given parameters and saves it on local machine.

    Parameters:
    xvalues (list): values to apply to the x-axis
    yvalues (list): values to apply to the y-axis
    title (str): title of the figure
    ylabel (str): label of y-axis of the figure
    path (pathlib.Path): path where figure is saved

    Returns:
    None. It saves the plotted figure.
    '''
    fig = plt.figure()
    plt.bar(xvalues, yvalues)
    plt.title(title)
    plt.xlabel(title, fontsize=12)
    plt.ylabel(ylabel, fontsize=12)
    path = Path.joinpath(path, f'{title}.jpg')
    fig.savefig(path, format='jpg')


def create_pie_chart(xvalues, yvalues, title, label, path) -> None:
    '''
    Plots a pie chart for the given parameters and saves it on local machine.

    Parameters:
    xvalues (list): values to apply to the x-axis
    yvalues (list): values to apply to the y-axis
    title (str): title of the figure
    label (str): label for the figure
    path (pathlib.Path): path where figure is saved

    Returns:
    None. It saves the plotted figures.
    '''
    fig1, ax1 = plt.subplots()
    ax1.pie(yvalues, autopct='%1.1f%%', pctdistance=1.14, radius = 0.8,
        wedgeprops = {'linewidth': 0.5, 'edgecolor':'k'})
    plt.legend(xvalues, bbox_to_anchor=(1,0), loc='lower right',
        bbox_transform=plt.gcf().transFigure)
    ax1.set_title(label)
    path = Path.joinpath(path, f'{title}.jpg')
    fig1.savefig(path)


def create_pie_chart_subplots(xvalues, yvalues, title, subplot_labels, path) -> None:
    '''
    Plots a pie chart with subplots for the given parameters and saves it on local machine.

    Parameters:
    xvalues (list): values to apply to the x-axis
    yvalues (list): values to apply to the y-axis
    title (str): title of the figure
    path (pathlib.Path): path where figure is saved
    subplot_labels (list): list of all subplots labels

    Returns:
    None. It saves the plotted figures.
    '''
    fig = plt.figure(figsize=(12,12))
    for i, value in enumerate(yvalues):
        axe = plt.subplot2grid((4, 2), (i // 2, i % 2))
        axe.pie(value, labels=xvalues[i], wedgeprops = {'linewidth': 0.5, 'edgecolor':'k'})
        axe.set_title(subplot_labels[i], fontsize=12)
    fig.subplots_adjust(wspace=.3, hspace = 0.2)
    path = Path.joinpath(path, f'{title}.jpg')
    fig.suptitle(title, fontsize=16)
    fig.savefig(path)
