assign_resource_mutation = '''
mutation{
 assignResource(roomId:1,resourceId:1, quantity:1){
  roomResource{
   quantity
 }
 }
}
'''

assign_resource_mutation_response = {
  "data": {
    "assignResource": {
      "roomResource": {
        "quantity": 1
      }
    }
  }
}

assign_resource_non_existent_room = '''
mutation{
 assignResource(roomId:5,resourceId:1, quantity:2){
  roomResource{
   quantity
 }
 }
}
'''

assign_non_existent_resource_id = '''
mutation{
 assignResource(roomId:1,resourceId:9, quantity:2){
  roomResource{
   quantity
 }
 }
}
'''

assign_quantity_less_than_one = '''
mutation{
 assignResource(roomId:1,resourceId:1, quantity:-3){
  roomResource{
   quantity
 }
 }
}
'''

assign_resource_multiple_times = '''
mutation{
 assignResource(roomId:1,resourceId:1, quantity:1){
  roomResource{
   quantity
 }
 }
}

'''

query_string = '/mrm?query='+assign_resource_mutation
