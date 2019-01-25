null = None
get_all_floors_query = '''{
    allFloors {
        floors {
            id
            name
            blockId
        }
    }
}
'''

get_floors_query_response = {
    "data": {
        "allFloors": {
            "floors": [
                {
                    "id": "5",
                    "name": "2nd",
                    "blockId": 2
                },
                {
                    "id": "4",
                    "name": "3rd",
                    "blockId": 1
                }
            ]
        }
    }
}

paginated_floors_query = '''
 query {
  allFloors(page:1, perPage:4){
   floors{
      id
      name
      blockId
   }
   hasNext
   hasPrevious
   pages
   currentPage
}
}
'''

paginated_floors_response = {
    "data": {
        "allFloors": {
            "floors": [
                {
                    "id": "5",
                    "name": "2nd",
                    "blockId": 2
                },
                {
                    "id": "4",
                    "name": "3rd",
                    "blockId": 1
                }
            ],
            "hasNext": False,
            "hasPrevious": False,
            "pages": 1,
            "currentPage": 1
        }
    }
}

non_existent_page_query = '''
 query {
  allFloors(page:100, perPage:4){
   floors{
      id
      name
      blockId
   }
   pages
   currentPage
}
}
'''
