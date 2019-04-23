null = None

office_structure_mutation_query = '''
    mutation{
        createOfficeStructure(
            data: [
                {structureId: "a-web-story", name: "Office 1", level: 1,
                parentId: "1", parentTitle: "parent1", tag: "office",
                position: 1, locationId: 2},
                {structureId: "a-web-user", name: "1st Floor", level: 1,
                parentId: "1", parentTitle: "parent2", tag: "office",
                position: 2, locationId: 2},
                {structureId: "a-web-guy", name: "Block A", level: 1,
                parentId: "1", parentTitle: "parent3", tag: "office",
                position: 2, locationId: 2}
            ]){
            structure
            {
                structureId
                name
                level
                parentId
                parentTitle
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
                    "parentId": "1",
                    "parentTitle": "parent1",
                    "tag": "office",
                    "position": 1,
                    "locationId": 2
                },
                {
                    "structureId": "a-web-user",
                    "name": "1st Floor",
                    "level": 1,
                    "parentId": "1",
                    "parentTitle": "parent2",
                    "tag": "office",
                    "position": 2,
                    "locationId": 2
                },
                {
                    "structureId": "a-web-guy",
                    "name": "Block A",
                    "level": 1,
                    "parentId": "1",
                    "parentTitle": "parent3",
                    "tag": "office",
                    "position": 2,
                    "locationId": 2
                }
            ]
        }
    }
}
