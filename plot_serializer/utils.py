from rdflib import Graph


def unit_in_ontology(unit_name, ontology_url="default"):
    if ontology_url == "default":
        ontology_url = (
            "https://raw.githubusercontent.com/HajoRijgersberg/OM/master/om-2.0.rdf"
        )
    g = Graph()

    g.parse(ontology_url, format="xml")

    query = (
        """
        PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
        SELECT ?unit
        WHERE{
        ?unit a om:Unit ;
                rdfs:label "%s"@en .
        }
        """
        % unit_name
    )

    results = g.query(query)

    return len(results)
