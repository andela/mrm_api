from ..output.OutputBuilder import build
from ..output.Error import error_item

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

een_error = error_item
een_error.message = "Structure not found"
een_error.locations = [{"line": 3, "column": 7}]
een_error.path = ["structureByStructureId"]
een_data = {"structureByStructureId": null}
expected_error_non_existant_structure_id = build(
    error=een_error.build_error(een_error),
    data=een_data
)

structure_query_invalid_structure_id = '''
   {
      structureByStructureId(structureId: "") {
          name
          level
          tag
      }
   }
        '''

eei_error = error_item
eei_error.message = "Please input a valid structureId"
eei_error.locations = [{"line": 3, "column": 7}]
eei_error.path = ["structureByStructureId"]
eei_data = {"structureByStructureId": null}
expected_error_invalid_structure_id = build(
    error=eei_error.build_error(eei_error),
    data=eei_data
)
