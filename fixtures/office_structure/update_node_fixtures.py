update_node_mutation = '''
mutation {
  updateNode(nodeId: "C56A4180-65AA-42EC-A945-5FD21DEC0518",
             name: "Epic Tower", tag: "Building Name") {
    node {
      name
      tag
    }
  }
}
'''

update_node_mutation_response = {
  "data": {
      "updateNode": {
        "node": {
          "name": "Epic Tower",
          "tag": "Building Name"
        }
      }
    }
  }

update_node_only_name_response = {
  "data": {
      "updateNode": {
        "node": {
          "name": "Epic Tower",
          "tag": "Lagos Building"
        }
      }
    }
  }

update_node_only_name_mutation = '''
mutation {
  updateNode(nodeId: "C56A4180-65AA-42EC-A945-5FD21DEC0518",
             name: "Epic Tower") {
    node {
      name
      tag
    }
  }
}
'''

update_node_only_tag_mutation = '''
mutation {
  updateNode(nodeId: "C56A4180-65AA-42EC-A945-5FD21DEC0518",
             tag: "Building Name") {
    node {
      name
      tag
    }
  }
}
'''

update_node_empty_name_mutation = """
mutation {
  updateNode(nodeId: "C56A4180-65AA-42EC-A945-5FD21DEC0518", name: "") {
    node {
      name
      tag
    }
  }
}
"""

update_node_empty_tag_mutation = """
mutation {
  updateNode(nodeId: "C56A4180-65AA-42EC-A945-5FD21DEC0518", tag: "") {
    node {
      name
      tag
    }
  }
}
"""

update_node_not_exist_mutation = """
mutation {
  updateNode(nodeId: "C56A4180-65AA-42EC-A945-5FD21DEC0432",
             name: "Epic Tower") {
    node {
      name
      tag
    }
  }
}
"""
