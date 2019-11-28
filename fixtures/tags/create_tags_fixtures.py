from ..output.OutputBuilder import build
from ..output.Error import error_item

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

cdt_error = error_item
cdt_error.message = "Block-B Tag already exists"
cdt_error.locations = [{"line": 3, "column": 9}]
cdt_error.path = ["createTag"]
cdt_data = {"createTag": null}
create_duplicate_tag_response = build(
    error=cdt_error.build_error(cdt_error),
    data=cdt_data
)

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

ctm_error = error_item
ctm_error.message = "name is required field"
ctm_error.locations = [{"line": 3, "column": 9}]
ctm_error.path = ["createTag"]
ctm_data = {"createTag": null}
create_tag_missing_args_response = build(
    error=ctm_error.build_error(ctm_error),
    data=ctm_data
)

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

une_error = error_item
une_error.message = "Tag not found"
une_error.locations = [{"line": 3, "column": 9}]
une_error.path = ["updateTag"]
une_data = {"updateTag": null}
update_non_existent_tag_response = build(
    error=une_error.build_error(une_error),
    data=une_data
)
