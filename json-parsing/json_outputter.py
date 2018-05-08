#!/usr/bin/env python

import json

print json.dumps(
    dict(
        hi="world",
        mylist=[1,1,2,3,5,8 ],
        truthybool=True,
        none=None,
        people={
            "maddie": { 
                "age": 16,
                "middlename": "ivy"
            }
        },
    ), 
    indent=2
)
