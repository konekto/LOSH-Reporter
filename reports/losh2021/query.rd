PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
prefix okh: <https://github.com/OPEN-NEXT/OKH-LOSH/raw/master/OKH-LOSH.ttl#>


SELECT ?label ?function ?dataSource ?readme
WHERE {
  ?x rdfs:label ?label .
  ?x okh:function ?function .
  ?x okh:dataSource ?dataSource .
  ?x okh:hasReadme ?readme .
}
LIMIT 255