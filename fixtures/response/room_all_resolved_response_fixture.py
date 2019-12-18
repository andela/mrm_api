from ..output.OutputBuilder import build
from .room_search_response_fixture import room_response_data

all_resolved_room_response_query = '''{
    allRoomResponses(resolved:true) {
        responses {
        roomName,
        totalResponses,
        response {
          id,
          response {
            ... on Rate{
              rate
            }
            ... on SelectedOptions{
              options
            }
            ... on TextArea{
              suggestion
            }
            ... on MissingItems{
              missingItems{
                name
                id
              }
            }
          }
        }
      }
    }
}
'''

all_resolved_room_response_data = build(
    data=room_response_data
)
