---
title: LOSH Data Report
subtitle: |
          | Annual, mostly statistical report on Open Source Hardware based on data from the LOSH knowledge base
          | **${PROJECT_VERSION_DATE}**
          | *version:* [${PROJECT_VERSION}](${PROJECT_VERSION_URL})
version: "${PROJECT_VERSION}"
date: "${PROJECT_VERSION_DATE}"
lang: en-US
charset: UTF-8
license: CC-BY-4.0
keywords:
- Open Source Hardware
- LOSH
- OSHdata
papersize: a4
geometry: "top=2cm,bottom=2cm,left=3cm,right=3cm"
comment: license applies to generated reports; date is automatically generated
...

# Intro

## General

LOSH xxx

<!--- general info about LOSH to be added -->

Efforts partly merged with the [OSHdata project](oshdata.com), which published annually reports based on data crawled from the [list of OSHWA-certified OSH projects](https://certification.oshwa.org/list.html). Since OSHWA published [its API](https://certificationapi.oshwa.org/documentation), no crawling is needed anymore. And since LOSH is here to collect data also from other platforms, we decided to take care of regular OSHdata reports – now also including data from other platforms.

Generally, all data you will find here is also publicly available in the LOSH knowledge base. This report is generated using the [LOSH-Reporter](https://github.com/OPEN-NEXT/LOSH-Reporter/) tool (GPL-3.0-OR-LATER). All we do is running a bunch of pre-defined queries on LOSH's knowledge base using that tool. If you want to look into the raw data yourself, e.g. to run some self-defined queries, find it [here](https://gitlab.opensourceecology.de/verein/projekte/losh-rdf) ([CC0-1.0](https://gitlab.opensourceecology.de/verein/projekte/losh-rdf/-/blob/main/LICENSE)). The report you are reading is licensed under the Creative Commons Attribution 4.0 International License ([CC-BY-4.0](https://creativecommons.org/licenses/by/4.0/legalcode)). This license covers the entire report, including the text and graphics. OSHdata is a project of the [Open Hardware Observatory e.V. (non-profit)](https://en.oho.wiki/wiki/Imprint) since 2021 (before is was a project of Kenny Consulting Group, LLC).

## Scope

xxx

<!--- brief description of scope to be added -->

## Get in contact with us

OSHdata is hosted by the [Open Hardware Repository e.V. (non-profit)](http://oho.wiki/) since 2021. Feel free to reach out to Robert to get in touch: [rm@oho.wiki](mailto:rm@oho.wiki?cc=mh@oho.wiki&subject=from the LOSH report)

LOSH was started inside the EU-H2020-founded [OPEN_NEXT](https://opennext.eu/) project back in 2020 and is hosted and maintained by [Open Source Ecology Germany e.V. (non-profit)](https://ose-germany.de/) since 2022. You can reach these folks via eMail ([verein@ose-germany.de](mailto:verein@ose-germany.de?cc=martin.haeuer@ose-germany.de&subject=from the LOSH report)) or Telegram ([@OSEGWelcome](https://t.me/OSEGWelcome)) – don't be shy; looking forward to e-meet you :)

You can also sign up for our newsletter [here]() or follow us on Twitter via [@OSHdata](https://twitter.com/OSHdata).

## This report…

<!--- brief intro specific to this version of the report to be added -->

[[TOC]]

# OSH Platforms

## Introduction

Currently, LOSH collects data from the following platforms:

- [GitHub.com](http://github.com/)
- [GitLab.com](https://gitlab.com/)
- [GitLab.OpenSourceEcology.de](https://gitlab.opensourceecology.de/)
- [Wikifactory.com](https://wikifactory.com/)
- [OSHWA Certification List](https://certification.oshwa.org/list.html)
- [Thingiverse.com](https://www.thingiverse.com/)

Additionally we have scripts catching data from:

- [Appropedia.org](https://appropedia.org/)
- [Open Know-How](https://openknowhow.org/) (including e.g. [Fieldready.org](https://www.fieldready.org/))

and making it available via GitHub (in [this repository](https://github.com/OPEN-NEXT/LOSH-list/)).

The minimum threshold for LOSH to be recognised as an OSH project is to have:

- a free/open license,
- a README file and
- at least one source file (other than the README.md, CONTRIBUTING.md or an image).

## Data input

By the publishing date of this report, the LOSH knowledge base contains:

- {ghproj} from [GitHub.com](http://github.com/) (not counting Open Know-How or Appropedia.org) ({} % of all its projects)
- {glcomproj} from [GitLab.com](https://gitlab.com/) ({} % of all its projects)
- {glosegproj} from [GitLab.OpenSourceEcology.de](https://gitlab.opensourceecology.de/) ({} % of all its projects)
- {wifproj} from [Wikifactory.com](https://wikifactory.com/) ({} % of all its projects)
- {oshwaproj} from [OSHWA Certification List](https://certification.oshwa.org/list.html) ({} % of all its projects)
- {thingiproj} from [Thingiverse.com](https://www.thingiverse.com/) ({} % of all its projects)
- {approproj} from [Appropedia.org](https://appropedia.org/) ({} % of all its projects)
- {okhproj} from [Open Know-How](https://openknowhow.org/) ({} % of all its projects)

…as illustrated in @fig:data-input-count

<!--- a bar chart with the above mentioned values, each bar splitting into accepted and rejected projects (rejected projects on top) -->
{#fig:data-input-count}

## History

Since the first report, published back in January 2022, data input has developed as following:

<!--- combined historical line diagram of total count of projects per year & for for each platform -->

Looking into the recent past @fig:data-hist-grow2 shows the grow rates for the past two years.

<!--- horizontal bar chart with grow rates per platform per each of the past 2 years + a bar for the total grow rate -->
{#fig:data-hist-grow2}

# Licenses

What separates a piece of open source hardware from a proprietary one is primarily its license.

<!--- add more info, also linking the OSH legal issues guideline and the tl;dr -->

The following @fig:license-dist-ind shows the distribution of licenses under which the _hardware_ has been published per platform.

<!--- 1 pie chart per platform showing the distribution of `spdxLicense` --> 
{#fig:fig:license-dist-ind}

Totalled, @fig:license-dist-total is the overall distribution of licenses used for the _hardware_.

<!--- pie chart showing the overall distribution of `spdxLicense`, sorted by strongly, weakly an non-reciprocal licensing schemes --> 
{#fig:fig:license-dist-ind}

# Technology and documentation readiness

- OTRL/ODRL assessment? (or mayby under git-based platforms)

# git-based platforms, OKH and Appropedia

- some detailled statistics based on manifest files
	+ OKH(v1) count + historical grow rate (2 years)
		* fields used (vertical bar chart) <!--- would require parsing the original YAML files-->
	+ appropedia count + historical grow rate (2 years)
		* fields used (vertical bar chart) <!--- would require parsing the original TOML files-->
	+ on git-based platforms OKH-LOSH (manifest) count + historical grow rate (2 years)
		* fields used (vertical bar chart) <!--- would require parsing the original TOML files-->

## Community-based Assessment according to DIN SPEC 3105-2

- CAB data
	+ project count:
		- attested/in progress + historical grow rate (2 years)
		- OHO / OSEG
	* certification per organisation
	* average assessment time (first submission…final attestation) + variance
	* average number of comments per asssessment + variance for top & bottom 10% of assessment time

### Projects of the year

2…4 projects from OSEG-CAB & OHO-CAB to be briefly presented & promoted

<!--- 2021: MNT Reform, OpenFlexure; something from OHO -->

<!--- section to be written manually -->

# Wikifactory

- some detailled statistics based on their API

# OSHWA

- data mostly like old OSHdata report
	+ certification per organisation
	+ etc.

# Thingiverse

- some detailled statistics based on their API

# Outro

<!--- add brief & friendly outro -->

See also

- https://stateofoshw.oshwa.org/
