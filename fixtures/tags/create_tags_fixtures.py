null = None

create_tag_query = '''
    mutation {
        createTag (name: "BlockA", color: "blue", description: "Block") {
    tag {
      name,
      color,
      description
    }
  }
}
'''

create_tag_response = {
    "data": {
     "createTag": {
      "tag": {
        "name": "BlockA",
        "color": "blue",
        "description": "Block"
      }
     }
    }
}

create_tag_with_duplicate_name = '''
    mutation {
        createTag (name: "Block-B", color: "green",
        description: "The description") {
        tag {
        name,
        color,
        description
        }
    }
    }
'''

create_duplicate_tag_response = {
  "errors": [
    {
      "message": "Block-B Tag already exists",
      "locations": [
        {
          "line": 3,
          "column": 9
        }
      ],
      "path": [
        "createTag"
      ]
    }
  ],
  "data": {
    "createTag": null
  }
}


create_tag_with_missing_argument = '''
    mutation {
        createTag (name: "", color: "green", description: "The description") {
        tag {
        name,
        color,
        description
        }
    }
    }
'''

create_tag_missing_args_response = {
  "errors": [
    {
      "message": "name is required field",
      "locations": [
        {
          "line": 3,
          "column": 9
        }
      ],
      "path": [
        "createTag"
      ]
    }
  ],
  "data": {
    "createTag": null
  }
}


update_tag_mutation = '''
mutation {
        updateTag (tagId: 1,color: "black") {
    tag {
      name,
      color,
      description
    }
  }
}'''

update_tag_response = {
  "data": {
    "updateTag": {
      "tag": {
        "name": "Block-B",
        "color": "black",
        "description": "The description"
      }
    }
  }
}

update_non_existent_tag_mutation = '''
mutation {
        updateTag (tagId: 20,color: "black") {
    tag {
      name,
      color,
      description
    }
  }
}'''

update_non_existent_tag_response = {
  "errors": [
    {
      "message": "Tag not found",
      "locations": [
        {
          "line": 3,
          "column": 9
        }
      ],
      "path": [
        "updateTag"
      ]
    }
  ],
  "data": {
    "updateTag": null
  }
}
