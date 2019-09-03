
room_events_query = "SELECT * FROM events WHERE room_id=:room_id AND \
   state=:state AND end_time::timestamptz + interval :hour_offset \
   < :event_end_time AND start_time::timestamptz + interval :hour_offset >= \
   :event_start_time"
