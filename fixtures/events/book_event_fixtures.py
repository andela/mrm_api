book_event_mutation = '''mutation {
    bookEvent(
        eventTitle:"Hello Converge",
        startDate:"2029-11-06",
        startTime:"10:00",
        duration:60
        attendees: "adafia.samuel@gmail.com, qanda8@gmail.com",
        timeZone: "Africa/Kigali",
        room:"Yankara"
    ){
            response
        }
    }
'''

book_event_mutation_no_title = '''mutation {
    bookEvent(
        eventTitle:"",
        startDate:"2019-11-06",
        startTime:"10:00",
        duration:60
        attendees: "adafia.samuel@gmail.com, qanda8@gmail.com",
        timeZone: "Africa/Kigali",
        room:"Yankara"
    ){
            response
        }
    }
'''

book_event_mutation_no_room = '''mutation {
    bookEvent(
        eventTitle:"Hello Converge",
        startDate:"2019-11-06",
        startTime:"10:00",
        duration:60
        attendees: "adafia.samuel@gmail.com, qanda8@gmail.com",
        timeZone: "Africa/Kigali",
        room:""
    ){
            response
        }
    }
'''

book_event_mutation_no_start_date = '''mutation {
    bookEvent(
        eventTitle:"Hello Converge",
        startDate:"",
        startTime:"10:00",
        duration:60
        attendees: "adafia.samuel@gmail.com, qanda8@gmail.com",
        timeZone: "Africa/Kigali",
        room:"Yankara"
    ){
            response
        }
    }
'''

book_event_mutation_no_start_time = '''mutation {
    bookEvent(
        eventTitle:"Hello Converge",
        startDate:"2019-11-06",
        startTime:"",
        duration:60
        attendees: "adafia.samuel@gmail.com, qanda8@gmail.com",
        timeZone: "Africa/Kigali",
        room:"Yankara"
    ){
            response
        }
    }
'''

book_event_mutation_no_time_Zone = '''mutation {
    bookEvent(
        eventTitle:"Hello Converge",
        startDate:"2019-11-06",
        startTime:"10:00",
        duration:60
        attendees: "adafia.samuel@gmail.com, qanda8@gmail.com",
        timeZone: "",
        room:"Yankara"
    ){
            response
        }
    }
'''
