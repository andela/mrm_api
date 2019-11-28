from ..output.OutputBuilder import build
from ..output.Error import error_item

null = None

resource_query = '''
        {
            resourceByName(searchName: "Speakers") {
                name
                room {
                    room {
                        name
                    }
                    quantity
                }
            }
        }
    '''

blank_resource_query = '''
        {
            resourceByName(searchName: "") {
                name
                room {
                    room {
                        name
                    }
                    quantity
                }
            }
        }
    '''

resource_response = {
    "data": {
        "resourceByName": [
            {
                "name": "Speakers",
                "room": []
            }
        ]
    }
}

ner_error = error_item
ner_error.message = "No Matching Resource"
ner_error.locations = [{"line": 3, "column": 13}]
ner_error.path = ["resourceByName"]
ner_data = {"resourceByName": null}
none_existing_resource_response = build(
    error=ner_error.build_error(ner_error),
    data=ner_data
)

sbn_error = error_item
sbn_error.message = "Please input Resource Name"
sbn_error.locations = [{"line": 3, "column": 13}]
sbn_error.path = ["resourceByName"]
sbn_data = {"resourceByName": null}
search_blank_name_response = build(
    error=sbn_error.build_error(sbn_error),
    data=sbn_data
)
