# LOSH-Reporter

The LOSH reporter is a CLI tool that queries an Apache Jena Fuseki server that contains data about OSH projects. The data extracted by the queries is used to generate a report about selected aspects of the OSH projects. The LOSH reporter generates MD, PDF and HTML reports. 

## Installation

Two system packages are required: Poetry, Pandoc.

To install these packages follow the installation instructions as described on the respective websites:     
https://python-poetry.org/docs/  
https://pandoc.org/installing.html  

For development, you can install docker a run Apache Jena inside a Docker container.

https://docs.docker.com/engine/install/    

A recent Python installation is also required (at least Python 3.9), which can be downloaded here:
https://www.python.org/downloads/  

Once these packages are installed, clone the repository to an empty folder, open a terminal and run:  
`poetry shell`  
to create a new virtual environment. Then run:    
`poetry install`  
to install the required packages into the virtual environment.  

### Development
To test and run the reporter locally you can use a dockerized Apache Jena instance. 

Start the Apache Jena database with `docker-compose up` within the `fuseki` folder.

### Environment variables
To start the reporter this environment variables need to be set:

* FUSEKI_URL
* FUSEKI_DATASET_NAME

An example can be found in `.env.example`. Those values can be used for development.

## Running the reporter

First install all dependencies with `poetry install`.

The reporter is a CLI tool. It is started by the following command (in the root directory):

`poetry run python reporter/cli.py generate --out <OUTFOLDER> --log_to <LOGGINGTARGET> <REPORTNAME> <format>`

* `format` is one of: `html / pdf / md`
* `log_to` is one of: `file / console`
* `REPORTNAME` - Report name is the name of the folder containing the three files needed to create a new report (and at the same time the name of the report to be created)
* `OUTFOLDER` - outfolder is the name of the folder where the created report will be saved.   

Example:
```
poetry run python reporter/cli.py --log_to console --out output generate example html
```
This command will generate a HTML file of the example report.

### Specification of a report

To generate a report, three files must be provided:

- a `query.json` file that contains the SPARQL-queries for an Apache Jena Fuseki instance (see https://jena.apache.org/tutorials/sparql.html for information about SPARQL). There is one query for each figure in the template file. The keys in the JSON-file must be the figure names from the template, the values have to be the sparql queries as strings.
- a mako file `template.md`. The template is the base for the report to be created. For more information see section "Template notes"
- a CSS stylesheet `style.css` for the html file

### Templating

A base for templating we use a markdown file. As templating engine the reporter uses mako (https://www.makotemplates.org/)

The reporter automatically executes the SPARQL queries the adds the result data to the template. Therefore, you can use those variables inside the markdown template.

The data for the Apache Jena instance has to be uploaded with the web interface: (http://localhost:3030)

####  Variables
Often are the results of SPAREQL queries lists of entries.

To get a value of one of those lists you can use a function:

```
get_value(QUERYRESULT,{"KEYTTOFILTER": "FILTERVALUE"}, "VALUEKEY")

```

* QUERYRESULT - the variable of the query result. Identical to the name of the query. Defined in `query.json` 
* FILTERKEY - The filed name you can to compare the FILTERVALUE to (Only equal comparisons are possbile an the moment )
* VALUEKEY - the key of the value to extract

Example:

```

query_result = [{count: 100, name: "Test"},{count: 1000, name: "TestAB"}, {count: 50, name: "TestA"} ]

count_value = get_value(query_result,{"name": "TestAB"}, "count")

count_value == 1000


```

#### Figures 

The reporter provides an easy method to generate different types of figures.

Currently, are those figures supported:

* pie charts
* bar charts

To generate a figure, the `figure` function can be used inside a template:

```
figure("TYPE", x="XVALUESTRING", y="YVALUESTRING", title="TITLE", label="LABEL")
```

* TYPE - `barchart` or `piechart`
* XVALUESTRING - dot-notation string to access query data e.g `repoHosts.count`. That will set all count values of the query `repoHosts` as x values
* YVALUESTRING - dot-notation string to access query data e.g `repoHosts.name`. That will set all name values of the query `repoHosts` as y values
* TITLE - the title of the figure. Blankspaces are not allowed.
* LABEL - the label of the figure.

Example:

```

repoHosts = [{count: 100, name: "Test"},{count: 1000, name: "TestAB"}, {count: 50, name: "TestA"} ]

figure("barchart", x="repoHosts.name", y="repoHosts.count", title="repohosts", label="All repoHost by counts")

That would generate a barchart with names of repoHosts as x-values and counts of the repeHosts as y-values

```

## License 

The LOSH Reporter is licensed under GPLv3, the generated reports are licensed under CC-BY-4.0.

## References

- OKH-LOSH specification: <https://github.com/OPEN-NEXT/OKH-LOSH/>
- LOSH-Krawler: <https://github.com/OPEN-NEXT/LOSH-Krawler/>
- the raw data of LOSH (RDF): <https://gitlab.opensourceecology.de/verein/projekte/losh-rdf>
- Jena-based test implementation: <https://github.com/OPEN-NEXT/LOSH-RDF-DB-tester>
