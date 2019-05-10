null = None

office_structure_mutation_query = '''
    mutation {
  createOfficeStructure(data: [
      {structureId: "851ae8b3-48dd-46b5-89bc-ca3f8111ad87", name: "Office 1",
      level: 1, parentId: "1", tag: "office", position: 1, locationId: 2},
      {structureId: "fd236595-71aa-407f-b417-f97ebadb94a0", name: "Office 2",
      level: 1, parentId: "1", tag: "office", position: 2, locationId: 2},
      {structureId: "27fbc541-6c2f-437a-bb38-be9af64442c3", name: "Office 3",
      level: 1, parentId: "1", tag: "office", position: 2, locationId: 2}]) {
    structure {
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

office_structure_mutation_with_duplicates = '''
    mutation {
  createOfficeStructure(data: [
      {structureId: "851ae8b3-48dd-46b5-89bc-ca3f8111ad87", name: "Office 1",
      level: 1, parentId: "1", tag: "office", position: 1, locationId: 2},
      {structureId: "851ae8b3-48dd-46b5-89bc-ca3f8111ad87", name: "Office 2",
      level: 1, parentId: "1", tag: "office", position: 2, locationId: 2},
      {structureId: "27fbc541-6c2f-437a-bb38-be9af64442c3", name: "Office 3",
      level: 1, parentId: "1", tag: "office", position: 2, locationId: 2}]) {
    structure {
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
                    "structureId": "851ae8b3-48dd-46b5-89bc-ca3f8111ad87",
                    "name": "Office 1",
                    "level": 1,
                    "parentId": "1",
                    "tag": "office",
                    "position": 1,
                    "locationId": 2
                },
                {
                    "structureId": "fd236595-71aa-407f-b417-f97ebadb94a0",
                    "name": "Office 2",
                    "level": 1,
                    "parentId": "1",
                    "tag": "office",
                    "position": 2,
                    "locationId": 2
                },
                {
                    "structureId": "27fbc541-6c2f-437a-bb38-be9af64442c3",
                    "name": "Office 3",
                    "level": 1,
                    "parentId": "1",
                    "tag": "office",
                    "position": 2,
                    "locationId": 2
                }
            ]
        }
    }
}
