node_creation_mutation = '''
mutation{
  createNode(name:"floors", parentId:1, tagId:1){
    node{
      name
      level
      left
      right
    }
  }
}
'''

duplicate_node_creation = '''
mutation{
  createNode(name:"location"){
    node{
      name
      level
      left
      right
    }
  }
}
'''

child_node_creation_mutation_with_non_existent_parent_id = '''
mutation{
  createNode(name:"floors", parentId:5){
    node{
      name
      level
      left
      right
    }
  }
}
'''

node_creation_mutation_with_non_existent_tag_id = '''
mutation{
  createNode(name:"floors", tagId:5){
    node{
      name
      level
      left
      right
    }
  }
}
'''
