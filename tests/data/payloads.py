authorize_payload = {
    "name": "eduard"
}

new_meme_empty_payload = {
    "id": "",
    "info": {
        "colors": [
            "",
            "",
        ],
        "objects": [
            "",
            ""
        ]
    },
    "tags": [
        "",
        ""
    ],
    "text": "",
    "updated_by": "",
    "url": ""
}

payload_with_info = {
    "id": "",
    "info": {
        "colors": [
            "red",
            "black",
            "white"
        ],
        "objects": [
            "picture",
            "text"
        ]
    },
    "tags": [
        "meme",
        "fun"
    ],
    "text": "what are memes",
    "updated_by": "",
    "url": "www.example.com"
}

payload_invalid = {
    "id": "",
    "info": {
        "colors": [
            111,
            "black"
        ],
        "objects": [
        ]
    },
    "tags": [
        "",
        ""
    ],
    "text": "",
    "updated_by": "",
    "url": 111
}

payload_update = {
    "info": {
        "colors": [
            "red",
            "red"
        ],
        "objects": [
            "3",
            "4"
        ]
    },
    "tags": [
        "1",
        "2"
    ],
    "text": "h",
    "url": "www.www.com"
}
payload_with_invalid_id = {
    "id": "AAAAAAAA",
    "info": {
        "colors": [
            "red",
            "black",
            "white"
        ],
        "objects": [
            "picture",
            "text"
        ]
    },
    "tags": [
        "meme",
        "fun"
    ],
    "text": "what are memes",
    "updated_by": "",
    "url": "www.example.com"
}
