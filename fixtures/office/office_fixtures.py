office_mutation_sample_string = '''
    mutation {
        createOffice(name: "%d", locationId:%s ) {
            office {
                name
                locationId
                blocks {
                    id
                    name
                }
            }
        }
    }
'''
paginated_offices_sample_string = '''
query {
    allOffices(page:%d, perPage:%s){
        offices{
            name
            id
        }
        hasNext
        hasPrevious
        pages
    }
}
'''
get_office_by_name_sample_string = '''
query{
    getOfficeByName(name:"%s"){
        name
        id
        blocks{
            name
            floors{
                name
                id
                rooms{
                name
                  id
                    }
                    }
                    }
                }
        }
'''


office_mutation_query = office_mutation_sample_string % (
    "The Crest", 1
)

get_office_by_name = get_office_by_name_sample_string % (
    "St. catherines"
)

office_mutation_query_Different_Location = office_mutation_sample_string % (
    "The Crest", 2
)

office_mutation_query_non_existant_ID = office_mutation_sample_string % (
    "The Crest", 10
)

office_mutation_query_duplicate_name = '''
    mutation {
        createOffice (name: "St. catherines", locationId: 1) {
            office {
                name
            }
        }
    }
'''

paginated_offices_query = paginated_offices_sample_string % (
    1, 3
)

offices_query = '''
query {
    allOffices{
        offices{
            name
            id
        }
    }
}
'''

paginated_offices_non_existing_page_query = paginated_offices_sample_string % (
    5, 3
)

get_office_by_invalid_name = get_office_by_name_sample_string % (
    "No name"
)
