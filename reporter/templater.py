'''
This module is used to render data into the reports template.
It uses pandoc to convert the files to desired output format: pdf/md/html
'''
import os
import logging
from contextlib import redirect_stdout
from pathlib import Path
import re
from mako.template import Template
from mako.runtime import Context
from reporter.core import plotter
from mako import exceptions
from io import StringIO

from reporter.core.errors import FileNotFound

logger = logging.getLogger("templater")

def create_fig(fig_options, data, path_to_images):
    if fig_options is None:
        return

    keys = fig_options.keys()

    if "x" not in keys or "y" not in keys:
        logger.error(f"graph needs to have x and y values. {example_fig_string}")
        return

    if "graph_type" not in keys:
        logger.error(f"graph needs to have a graph type.  {example_fig_string}")

    fig_options["x"] = fig_options["x"].split('.')
    fig_options["y"] = fig_options["y"].split('.')

    xValues = [d[fig_options["x"][1]] for d in data[fig_options["x"][0]]]
    yValues = [d[fig_options["y"][1]] for d in data[fig_options["y"][0]]]

    if fig_options["graph_type"] == "piechart":
        title = fig_options['title']
        label = fig_options['label']

        plotter.create_pie_chart(xvalues=xValues,
                                 yvalues=yValues, title=title,
                                 path=path_to_images,
                                 label=label
                                 )

    if fig_options["graph_type"] == "piechart-subplots":
        raise NotImplementedError
        # TODO:
        platform_names = ['Github', 'Wikifactory', 'Appropedia', 'OSEGs', 'OSHWA', 'Thingiverse', 'Open-Know-How']
        title = fig_options['title']

        plotter.create_pie_chart_subplots(xvalues=xValues,
                                          yvalues=yValues, title=title,
                                          path=path_to_images,
                                          subplot_labels=platform_names)

    if fig_options["graph_type"] == "barchart":
        title = fig_options['title']
        label = fig_options['label']
        # create and save figures
        plotter.create_bar_chart(xvalues=xValues, yvalues=yValues,
                                 title=title, ylabel=label, path=path_to_images, )


def get_value(dataset, filters, valueKey):
    def filter_by_filters(result):
        filter_keys = filters.keys()
        okay = False;
        for key in filter_keys:
            okay = result[key] == filters[key]

        return okay

    r_list = list(filter(filter_by_filters, dataset))

    if len(r_list) == 0:
        return "N/A"

    result = r_list[0]

    return result[valueKey]


def templating(data, args) -> None:
    '''
    Renders data into the reports template and saves it locally.

    Parameters:
    data (Data): a Dataclass object in which the computed data values for the rendering are stored
    args (argparse.Namespace): object that contains the arguments that were passed as cli-parameters

    Returns:
    None. It saves the requested document on the local machine.

    '''
    report_name = Path(args.report_name)
    out_folder = Path(f'{args.out}/{report_name}')

    # get path where the before generated figures lie
    path_to_images = Path(f'./{out_folder}/img').resolve()

    templ_copy_file = f'./{out_folder}/templ_copy.md'

    # first prepare template file:
    # - ensure md-headings are still recognized ('##' is a comment for Mako)
    # - fill in the the absolut paths for the figure-files
    # for safety reasons: do the changes to a temporary copy of the template file
    with open(Path(f'./reports/{report_name}/template.md'), mode='r', encoding='utf-8') as in_file, \
            open(Path(templ_copy_file), mode='w', encoding='utf-8') as out_file:
        for line in in_file:
            line = line.replace('##', "${'##'}")
            out_file.write(line)

    # read template file
    if Path(templ_copy_file).exists() is False:
        raise FileNotFound(f'template file not found at: "{templ_copy_file}"')
    template = Template(filename=templ_copy_file)

    def figure(type, **fig_options):
        fig_options['graph_type'] = type
        create_fig(fig_options, data, path_to_images)

        title = fig_options['title']

        return f'![{title}]({path_to_images}/{title}.jpg){{#fig:{title}}}'

    data_for_template = data
    data_for_template["get_value"] = get_value
    data_for_template["figure"] = figure

    # create variable for output file
    file = Path(f'./{out_folder}/{report_name}.md')

    # render data into tempate
    try:
        with open(file, 'w', encoding='utf-8') as out_file:
            with redirect_stdout(out_file):
                output = template.render(**data_for_template)
                print(output)
    except AttributeError as err:
        logging.error('The requested attribute is not contained in data object')
        logging.error(err)
    except FileNotFound as err:
        logging.error('The requested file is not found')
        logging.error(err)
    except NameError as err:
        logging.error('Error in the process of rendering the template.')
        logging.error(exceptions.text_error_template().render())

    # convert rendered file to desired format (which we got as cli-argument)
    # and get figures numbered by pandoc-fignos.

    if args.format == 'pdf':
        os.system(f'pandoc {file} --pdf-engine=xelatex -s -o ./{out_folder}/{report_name}.pdf \
                -V geometry:top=2cm,bottom=2cm,left=3cm,right=3cm --filter pandoc-fignos --toc')
        os.remove(file)

    elif args.format == 'html':
        os.system(f'pandoc {file} -f markdown -t html -s -o ./{out_folder}/{report_name}.html \
                --metadata pagetitle=LOSH-Report --filter pandoc-fignos --toc \
                --css ../../reports/{report_name}/styles.css')
        os.remove(file)

    elif args.format == 'md':
        os.system(f'pandoc {file} -f markdown -s -o ./{out_folder}/{report_name}.md \
                --filter pandoc-fignos --toc')

    logger.info(f"Report {report_name} created.")
