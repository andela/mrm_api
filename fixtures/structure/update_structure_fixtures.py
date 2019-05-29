update_office_structure_mutation = '''
mutation {
  updateOfficeStructure(
      structureId: "b05fc5f2-b4aa-4f48-a8fb-30bdcc3fc968",
      name:"St.Catherine's", level:3, parentTitle:"parent 5",
      tag:"offices", position:4, locationId:1, parentId:"2") {
    structure {
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

update_office_structure_mutation_response = {
  "data": {
    "updateOfficeStructure": {
      "structure": {
        "structureId": "b05fc5f2-b4aa-4f48-a8fb-30bdcc3fc968",
        "name": "St.Catherine's",
        "level": 3,
        "parentId": "2",
        "parentTitle": "parent 5",
        "tag": "offices",
        "position": 4,
        "locationId": 1
      }
    }
  }
}

update_structure_invalid_id = '''
mutation {
  updateOfficeStructure(
      structureId: "b05fc5f2-b4aa-4f48-a8fb-30bdcc3fc968-non-existent",
      name:"St.Catherine's", level:3, parentTitle:"parent 5",
      tag:"offices", position:4, locationId:1, parentId:"2") {
    structure {
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
