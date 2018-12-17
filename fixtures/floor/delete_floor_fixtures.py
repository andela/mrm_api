delete_floor_mutation = '''
    mutation {
        deleteFloor(floorId:4) {
            floor {
            name,
            blockId
            }
        }
    }
'''

delete_with_nonexistent_floor_id = '''
    mutation {
        deleteFloor(floorId:6) {
            floor {
            name,
            blockId
            }
        }
    }
'''
