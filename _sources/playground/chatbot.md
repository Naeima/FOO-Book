# FOO chatbot
## https://huggingface.co/spaces/Naeima/FOO 

'''python 

    from rdflib import Graph
    import gradio as gr
    foo_KG = Graph()
    foo_KG.parse("https://naeima.github.io/fooKG/index.ttl", format="ttl")
    def handle_question(question):
        try:
            q = question.lower()
            if "gps" in q or "location" in q:
                query = """
                PREFIX foo: <https://w3id.org/def/foo#>
                SELECT ?id ?latitude ?longitude ?localDate
                WHERE {
                ?s a foo:gPSObservation ;
                    foo:id ?id ;
                    foo:latitude ?latitude ;
                    foo:longitude ?longitude ;
                    foo:localDate ?localDate .
                }
                ORDER BY ?localDate
                LIMIT 5
                """
                rows = [row.asdict() for row in foo_KG.query(query)]
                return "\n\n".join([
                    f"🛰️ ID: {r['id']}, 🌍 Lat: {r['latitude']}, Long: {r['longitude']}, 📅 Date: {r['localDate']}"
                    for r in rows
                ]) if rows else "No GPS data found."

            elif "tree" in q or "liana" in q or "plot" in q:
                query = """
                PREFIX foo: <https://w3id.org/def/foo#>
                SELECT ?id ?treeID ?treeHeightM ?treeDbhCm ?treeNLianas ?sitePlotCode ?siteName
                WHERE {
                ?s a foo:treeObservation ;
                    foo:id ?id ;
                    foo:treeID ?treeID ;
                    foo:treeHeightM ?treeHeightM ;
                    foo:treeDbhCm ?treeDbhCm ;
                    foo:treeNLianas ?treeNLianas ;
                    foo:sitePlotCode ?sitePlotCode ;
                    foo:siteName ?siteName .
                }
                LIMIT 5
                """
                rows = [row.asdict() for row in foo_KG.query(query)]
                return "\n\n".join([
                    f"🌳 Tree ID: {r['treeID']} ({r['id']}), Height: {r['treeHeightM']} m, DBH: {r['treeDbhCm']} cm, Lianas: {r['treeNLianas']}, Plot: {r['sitePlotCode']} @ {r['siteName']}"
                    for r in rows
                ]) if rows else "No tree/liana observations found."

            elif "soil" in q or "ph" in q or "clay" in q or "carbon" in q or "nitrogen" in q:
                query = """
                PREFIX foo: <https://w3id.org/def/foo#>
                SELECT ?identifier ?soilPH ?totalC ?totalN ?cNRatio ?plotName ?landUse ?site
                WHERE {
                ?s a foo:Observation ;
                    foo:identifier ?identifier ;
                    foo:soilPH ?soilPH ;
                    foo:totalC ?totalC ;
                    foo:totalN ?totalN ;
                    foo:cNRatio ?cNRatio ;
                    foo:plotName ?plotName ;
                    foo:landUse ?landUse ;
                    foo:site ?site .
                }
                LIMIT 5
                """
                rows = [row.asdict() for row in foo_KG.query(query)]
                return "\n\n".join([
                    f"🧪 Site: {r['site']} ({r['plotName']}, {r['identifier']}), pH: {r['soilPH']}, C: {r['totalC']}, N: {r['totalN']}, C/N: {r['cNRatio']}, Land use: {r['landUse']}"
                    for r in rows
                ]) if rows else "No soil data found."

            else:
                return "I support questions about GPS observations, tree/liana features, and soil chemistry. Try asking about tree height, GPS data, or soil pH."

        except Exception as e:
            return f"❌ Error: {e}"
    gr.Interface(
        fn=handle_question,
        inputs=gr.Textbox(lines=2, placeholder="Ask about GPS, trees, or soil observations..."),
        outputs="text",
        title="FOO Chatbot",
        description="Ask questions about GPS, tree/liana, and soil observations from FOO.",
        examples=[
            "Show me GPS observation data.",
            "How many GPS observations are there?",
            "List liana observations with tree heights.",
            "What is the soil pH at Maliau Basin?",
            "Show me soil nitrogen and carbon values.",
            "Where are trees with more than 5 lianas?",
            "Give me site and plot info for tree observations."
        ]
    ).launch()
'''