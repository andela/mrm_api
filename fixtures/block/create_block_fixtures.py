create_block_sample_string = '''
  mutation{
  createBlock(officeId:%d, name:"%s" ) {
    block{
      officeId
        name
      }
  }
}
'''
delete_block_sample_string = '''
mutation{
  DeleteBlock(blockId:%s){
    block{
      name
      id
    }
  }
}
'''
update_block_sample_string = '''
mutation{
  updateBlock(name: "%d", blockId: %s){
    block{
      name
      id
    }
  }
}
'''

create_block_query = create_block_sample_string % (2, "blask")

block_mutation_query_without_name = create_block_sample_string % (2, "")

block_creation_with_duplicate_name = create_block_sample_string % (2, "Ec")

create_block_with_non_existing_office = create_block_sample_string % (
    56, "Block F")


update_block = update_block_sample_string % ("Block A", 1)

delete_block = delete_block_sample_string % (1)

delete_non_existent_block = delete_block_sample_string % (431)

update_non_existent_block = update_block_sample_string % ("Block A", 423)

create_block_outside_nairobi = create_block_sample_string % (1, "Block D")
