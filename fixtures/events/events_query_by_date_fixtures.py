query_events = '''
    query{
        allEvents(startDate: "Jul 9 2018", endDate: "Jul 9 2018"){
            events {
                eventTitle
            }
        }
    }
'''

query_events_with_start_date_before_end_date = '''
    query{
        allEvents(startDate: "Jul 20 2018",
                  endDate: "Jul 09 2018",
                  page:1,
                  perPage: 2){
            events {
                eventTitle

            },
            hasNext,
            hasPrevious,
            pages,
            queryTotal
        }
    }
'''

query_events_with_pagination = '''
    query{
        allEvents(startDate: "Jul 11 2018",
                  endDate: "Jul 11 2018",
                  page:1,
                  perPage: 1){
            events {
                    id
                    roomId
                    room{
                        name
                    }
            },
            hasNext,
            hasPrevious,
            pages,
            queryTotal
        }
    }
'''

query_events_page_without_per_page = '''
query{
  allEvents(
      startDate: "Mar 28 2019",
      endDate: "Mar 29 2019",
      page: 1
    ){
    events {
      eventTitle
    }
    hasNext
    hasPrevious
    pages
    queryTotal
  }
}
'''

query_events_per_page_without_page = '''
query{
  allEvents(
      startDate: "Mar 28 2019",
      endDate: "Mar 29 2019",
      perPage: 1
    ){
    events {
      eventTitle
    }
    hasNext
    hasPrevious
    pages
    queryTotal

  }
}
'''

query_events_invalid_page = '''
query{
  allEvents(
      startDate: "Mar 28 2019",
      endDate: "Mar 29 2019",
      page: 0,
      perPage:1
      ){
    events {
      eventTitle
    }
    hasNext
    hasPrevious
    pages
    queryTotal

  }
}
'''

query_events_invalid_per_page = '''
query{
  allEvents(
      startDate: "Mar 28 2019",
      endDate: "Mar 29 2019",
      page: 1,
      perPage:0
      ){
    events {
      eventTitle
    }
    hasNext
    hasPrevious
    pages
    queryTotal

  }
}
'''

query_events_without_start_date = '''
  query{
    allEvents(
        endDate: "Mar 29 2019",
        perPage: 1,
        page: 3
      ){
      events {
        eventTitle
      }
      hasNext
      hasPrevious
      pages
      queryTotal

    }
  }
'''

query_events_without_end_date = '''
  query{
    allEvents(
        startDate: "Mar 29 2019",
        perPage: 1,
        page: 3
      ){
      events {
        eventTitle
      }
      hasNext
      hasPrevious
      pages
      queryTotal

    }
  }
'''

query_events_without_page_and_per_page = '''
query{
  allEvents(startDate: "Jul 11 2018",
            endDate: "Jul 11 2018"){
        events {
                id
                roomId
                room{
                    name
                }
        },
        hasNext,
        hasPrevious,
        pages,
        queryTotal
    }
  }
'''

query_events_without_start_and_end_date = '''
  query{
      allEvents(perPage: 1, page: 3){
          events {
              eventTitle
          }
      }
  }
'''
