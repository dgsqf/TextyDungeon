import util
dict={
    "description":"Bonjour\nJe suis un robot",
    "actions": [
        {
            "str":"Bonjour",
            "encounter":None

        },
        {
            "str":"Aurevoir",
            "encounter":None

        }
    ]

}
Encounter=util.encounter_from_dict(dict)
Encounter.Render()