# LOSH-Reporter

A locally executable script + Apache Jena + Queries to generate (mostly statistical) reports on LOSH data in MD + PDF &amp; HTML exports

## How to read the template

- `TEMPLATE.md` is the template for the report to be generated
- `{DATA-FIELD}` is to be replaced by the value of the referenced `DATA-FIELD`
- diagrams are referenced using the `pandoc-fignos` syntax: inline in the text with `@fig:SOME-REF` and directly under the diagram with `{#fig:SOME-REF}`

Comment:

- While the report speaks of OSH _projects_, the `OKH-LOSH` specification defines OSH `modules`. In data specifications in this repo we'll use the `OKH-LOSH` notion.
- If not otherwise noted, numbers refer to modules, _ignoring their different versions_.
- …hence calculations are (if not otherwise noted) run on the total LOSH data

## References

- OKH-LOSH specification: <https://github.com/OPEN-NEXT/OKH-LOSH/>
- LOSH-Krawler: <https://github.com/OPEN-NEXT/LOSH-Krawler/>
- the raw data of LOSH (RDF): <https://gitlab.opensourceecology.de/verein/projekte/losh-rdf>
- Jena-based test implementation: <https://github.com/OPEN-NEXT/LOSH-RDF-DB-tester>
