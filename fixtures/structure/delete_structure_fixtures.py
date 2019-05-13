delete_office_structures = """
    mutation{
        deleteOfficeStructure(
            structureIds: [
                 "851ae8b3-48dd-46b5-89bc-ca3f8111ad87",
                 "27fbc541-6c2f-437a-bb38-be9af64442c3"]){
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
"""

delete_office_structures_with_invalid_id = """
    mutation{
        deleteOfficeStructure(
            structureIds: [
                 "invalid-id", "a-web-user","a-web-guy-y"]){
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
"""

delete_structures_expected_response = {
  'data': {
    'deleteOfficeStructure': {
      'structure': [{
        'structureId': '851ae8b3-48dd-46b5-89bc-ca3f8111ad87',
        'name': 'Office 1',
        'level': 1,
        'parentId': '1',
        'parentTitle': None,
        'tag': 'office',
        'position': 1, 'locationId': 2
        },
        {
          'structureId': '27fbc541-6c2f-437a-bb38-be9af64442c3',
          'name': 'Office 3',
          'level': 1,
          'parentId': '1',
          'parentTitle': None,
          'tag': 'office',
          'position': 2,
          'locationId': 2
        }
      ]
    }
  }
}
