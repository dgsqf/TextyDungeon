import util
dict={
    "description":"Bonjour\nJe suis un robot",
    "actions": [
        {
            "str":"Bonjour",
            "encounter":{
    "description":"Bonjour\nJe suis un robot",
    "actions": [
        {
            "str":"Bonjour",
            "encounter":None,
            "items":["Bonjour"]

        },
        {
            "str":"Aurevoir",
            "encounter":None,
            "items":["Aurevoir"]

        }
    ]

},
            "items":["Bonjour"]

        },
        {
            "str":"Aurevoir",
            "encounter":{
    "description":"Bonjour\nJe suis un robot",
    "actions": [
        {
            "str":"Bonjour",
            "encounter":None,
            "items":["Bonjour"]

        },
        {
            "str":"Aurevoir",
            "encounter":None,
            "items":["Aurevoir"]

        }
    ]

},
            "items":["Aurevoir"]

        }
    ]

}
story=util.Story(dict)
story.start()