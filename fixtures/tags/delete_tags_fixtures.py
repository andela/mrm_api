delete_tag_query = '''
mutation{
  deleteTag(tagId:1){
    tag{
      id
    }
  }
}
'''

delete_tag_response = {
  "data": {
    "deleteTag": {
      "tag": {
        "id": "1"
      }
    }
  }
}

delete_non_existent_tag = '''
mutation{
  deleteTag(tagId:20){
    tag{
      id
    }
  }
}
'''
