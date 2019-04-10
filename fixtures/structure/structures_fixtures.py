null = None

structures_query = '''
   {
      allStructures {
        structureId
        level
        name
        parentId
        tag
        locationId
        position
      }
    }
        '''

expected_structures_query_response = {
    "data": {
        "allStructures": [
            {
                "structureId": "b05fc5f2-b4aa-4f48-a8fb-30bdcc3fc968",
                "level": 1,
                "name": "Epic tower",
                "parentId": "1",
                "tag": "Building",
                "locationId": 1,
                "position": 1
            }
        ]
    }
}

structure_query = '''
   {
     structureByStructureId(structureId: "b05fc5f2-b4aa-4f48-a8fb-30bdcc3fc968")
     {
          name
          level
          tag
          locationId
      }
   }
        '''

expected_structure_query_response = {
    "data": {
        "structureByStructureId":
            {
                "name": "Epic tower",
                "level": 1,
                "tag": "Building",
                "locationId": 1
            }
    }
}

structure_query_non_existant_structure_id = '''
   {
      structureByStructureId(structureId: "b05fc5f2-b4aa-4f48") {
          name
          level
          tag
      }
   }
        '''

expected_error_non_existant_structure_id = {
  "errors": [
    {
      "message": "Structure not found",
      "locations": [
        {
          "line": 3,
          "column": 7
        }
      ],
      "path": [
        "structureByStructureId"
      ]
    }
  ],
  "data": {
    "structureByStructureId": null
  }
}

structure_query_invalid_structure_id = '''
   {
      structureByStructureId(structureId: "") {
          name
          level
          tag
      }
   }
        '''

expected_error_invalid_structure_id = {
  "errors": [
    {
      "message": "Please input a valid structureId",
      "locations": [
        {
          "line": 3,
          "column": 7
        }
      ],
      "path": [
        "structureByStructureId"
      ]
    }
  ],
  "data": {
    "structureByStructureId": null
  }
}
