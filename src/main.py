import util
dict={
    "description":"Bonjour\nJe suis un robot",
    "actions":[
        {
            "str":"Bonjour",
            "encounter":{
    "description":"Bonjour\nJe suis un robot",
    "actions":[
        {
            "str":"Bonjour",
            "encounter":None,
            "items":["Bonjour"],
            "ritems":[]
        }
    ]

},
            "items":["Bonjour"],
            "ritems":["Auevoir"]
        }
    ]

}
story=util.Story(dict)
story.start()