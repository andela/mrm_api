delete_floor_mutation = '''
    mutation {
        deleteFloor(floorId:1) {
            floor {
            name,
            blockId
            }
        }
    }
'''

delete_with_nonexistent_floor_id = '''
    mutation {
        deleteFloor(floorId:5) {
            floor {
            name,
            blockId
            }
        }
    }
'''
