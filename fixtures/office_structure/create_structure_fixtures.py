null = None

valid_structure_mutation = '''
    mutation {
      createStructure (nodeList: [
    {id: "C56A4180-65AA-42EC-A945-5FD21DEC0538",
    name: "Epic Tower" tag: "Building Name"},

    {id: "C56A4180-65AA-42EC-A945-5FD21DEC0536",
    name: "Gold Coast" tag: "First Floor",
    parentId: "C56A4180-65AA-42EC-A945-5FD21DEC0538"},

    {id: "C56A4180-65AA-42EC-A945-5FD21DEC0537",
    name: "Ubuntu" tag: "Fourth Floor",
    parentId: "C56A4180-65AA-42EC-A945-5FD21DEC0538"}]) {
        structure {
          name
          tag
          level
          left
          right
          treeId
        }
      }
    }
'''

valid_structure_mutation_response = {
  "data": {
    "createStructure": {
      "structure": [
        {
          "name": "Epic Tower",
          "tag": "Building Name",
          "level": 1,
          "left": 1,
          "right": 6,
          "treeId": 2
        },
        {
          "name": "Gold Coast",
          "tag": "First Floor",
          "level": 2,
          "left": 2,
          "right": 3,
          "treeId": 2
        },
        {
          "name": "Ubuntu",
          "tag": "Fourth Floor",
          "level": 2,
          "left": 4,
          "right": 5,
          "treeId": 2
        }
      ]
    }
  }
}

structure_mutation_empty_node_list = """
    mutation {
          createStructure (nodeList: []) {
            structure {
              name
              tag
              level
            }
          }
        }
"""

structure_mutation_empty_node_list_response = {
  "errors": [
    {
      "message": "node_list cannot be empty",
      "locations": [
        {
          "line": 3,
          "column": 11
        }
      ],
      "path": [
        "createStructure"
      ]
    }
  ],
  "data": {
    "createStructure": null
  }
}

structure_mutation_duplicate_node_id = """
    mutation {
          createStructure (nodeList: [
        {id: "C56A4180-65AA-42EC-A945-5FD21DEC0538",
        name: "Epic Tower" tag: "Building Name"},

        {id: "C56A4180-65AA-42EC-A945-5FD21DEC0538",
        name: "Gold Coast" tag: "First Floor",
        parentId: "C56A4180-65AA-42EC-A945-5FD21DEC0538"}]) {
            structure {
              name
              tag
              level
            }
          }
        }
"""

structure_mutation_duplicate_node_id_reponse = {
  "errors": [
    {
      "message": "nodes must have unique id",
      "locations": [
        {
          "line": 3,
          "column": 11
        }
      ],
      "path": [
        "createStructure"
      ]
    }
  ],
  "data": {
    "createStructure": null
  }
}

structure_mutation_node_id_in_use = """
  mutation {
        createStructure (nodeList:[
      {id: "C56A4180-65AA-42EC-A945-5FD21DEC0518",
      name: "Epic Tower" tag: "Building Name"}]) {
          structure {
            name
            tag
            level
          }
        }
    }
"""
structure_mutation_node_id_in_use_response = {
  "errors": [
    {
      "message": "node id \"c56a4180-65aa-42ec-a945-5fd21dec0518\" in use",
      "locations": [
        {
          "line": 3,
          "column": 9
        }
      ],
      "path": [
        "createStructure"
      ]
    }
  ],
  "data": {
    "createStructure": null
  }
}

structure_mutation_multiple_root_nodes = """
   mutation {
      createStructure (nodeList: [
    {id: "C56A4180-65AA-42EC-A945-5FD21DEC0521",
    name: "Epic Tower" tag: "Building Name"},

    {id: "C56A4180-65AA-42EC-A945-5FD21DEC0522",
     name: "Epic Tower" tag: "Building Name"}
   ]) {
        structure {
          name
          tag
          level
        }
      }
    }
"""

structure_mutation_multiple_root_nodes_response = {
  "errors": [
    {
      "message": "there must be exactly 1 root node. 2 were supplied",
      "locations": [
        {
          "line": 3,
          "column": 7
        }
      ],
      "path": [
        "createStructure"
      ]
    }
  ],
  "data": {
    "createStructure": null
  }
}

structure_mutation_node_before_parent = """
mutation {
      createStructure (nodeList: [
    {id: "C56A4180-65AA-42EC-A945-5FD21DEC0521",
    name: "Epic Tower" tag: "Building Name"},

    {id: "C56A4180-65AA-42EC-A945-5FD21DEC0522",
    name: "Ubuntu" tag: "Fourth Floor",
    parentId: "C56A4180-65AA-42EC-A945-5FD21DEC0523"}
   ]) {
        structure {
          name
          tag
          level
        }
      }
    }
"""

structure_mutation_node_before_parent_response = {
  "errors": [
    {
      "message": "node \"Ubuntu\" appears before its parent",
      "locations": [
        {
          "line": 3,
          "column": 7
        }
      ],
      "path": [
        "createStructure"
      ]
    }
  ],
  "data": {
    "createStructure": null
  }
}
