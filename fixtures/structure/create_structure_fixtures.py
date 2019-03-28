null = None

office_structure_mutation_query = '''
    mutation{
        createOfficeStructure(
            data: [
                {structureId: "a-web-story", name: "Office 1", level: 1,
                parentId: 1, tag: "office", position: "1", locationId: 2},
                {structureId: "a-web-user", name: "Office 1", level: 1,
                parentId: 1, tag: "office", position: "2", locationId: 2},
                {structureId: "a-web-guy", name: "Office 1", level: 1,
                parentId: 1, tag: "office", position: "2", locationId: 2}
            ]){
            structure
            {
                structureId
                name
                level
                parentId
                tag
                position
                locationId
            }
        }
    }
'''

office_structure_mutation_response = {
    "data": {
        "createOfficeStructure": {
            "structure": [
                {
                    "structureId": "a-web-story",
                    "name": "Office 1",
                    "level": 1,
                    "parentId": 1,
                    "tag": "office",
                    "position": 1,
                    "locationId": 2
                },
                {
                    "structureId": "a-web-user",
                    "name": "Office 1",
                    "level": 1,
                    "parentId": 1,
                    "tag": "office",
                    "position": 2,
                    "locationId": 2
                },
                {
                    "structureId": "a-web-guy",
                    "name": "Office 1",
                    "level": 1,
                    "parentId": 1,
                    "tag": "office",
                    "position": 2,
                    "locationId": 2
                }
            ]
        }
    }
}
