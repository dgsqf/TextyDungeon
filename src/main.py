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
            "ritems":[],
            "vchanges":[
                {
                    "name":"=",
                    "operation":"=",
                    "value":"10"

                },
                {
                    "name":"+",
                    "operation":"+",
                    "value":"10"

                },
                {
                    "name":"-",
                    "operation":"-",
                    "value":"10"

                },
                {
                    "name":"*",
                    "operation":"*",
                    "value":"10"

                },
                {
                    "name":"/",
                    "operation":"/",
                    "value":"10"

                }
            ]
        }
    ]

},
            "items":["Bonjour"],
            "ritems":["Auevoir"],
            "vchanges":[
                {
                    "name":"=",
                    "operation":"=",
                    "value":"10"

                },
                {
                    "name":"+",
                    "operation":"+",
                    "value":"10"

                },
                {
                    "name":"-",
                    "operation":"-",
                    "value":"10"

                },
                {
                    "name":"*",
                    "operation":"*",
                    "value":"10"

                },
                {
                    "name":"/",
                    "operation":"/",
                    "value":"10"

                }
            ]
        }
    ]

}
story=util.Story(dict,True)
story.start()