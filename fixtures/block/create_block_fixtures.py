null = None

create_block_query = '''
  mutation{
  createBlock(officeId:2, name:"blask" ) {
    block{
      officeId
        name
      }
  }
}
'''

create_block_response = {
  "data": {
    "createBlock": {
      "block": {
        "officeId": 2,
        "name": "blask"
      }
    }
  }
}

block_mutation_query_without_name = '''
     mutation{
    createBlock(officeId:2, name:"" ) {
        block{
            officeId
            name
        }
    }
}
'''

block_creation_with_duplicate_name = '''
mutation{
  createBlock(officeId:1 name:"EC" ) {
    block{
      officeId
        name
      }
  }
}
'''

block_creation_with_duplicate_name_response = {
  "errors": [
    {
      "message": "Block aleady exists",
      "locations": [
        {
          "line": 3,
          "column": 3
        }
      ],
      "path": [
        "createBlock"
      ]
    }
  ],
  "data": {
    "createBlock": null
  }
}

create_block_with_non_existing_office = '''
mutation{
  createBlock(officeId:56 name:"Block F" ) {
    block{
      officeId
        name
      }
  }
}
'''

create_block_with_non_existing_office_response = {
  "errors": [
    {
      "message": "Office not found",
      "locations": [
        {
          "line": 3,
          "column": 3
        }
      ],
      "path": [
        "createBlock"
      ]
    }
  ],
  "data": {
    "createBlock": null
  }
}
