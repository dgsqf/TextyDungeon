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
story=util.Story(dict)
story.start()