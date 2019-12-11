def insert_records_in_table(session, model, records):
    """
    inserts multiple records in a table
    """
    for record in records:
        send_record = model(**record)
        send_record.save()
    session.commit()
    f = open('mrm.err.log', 'a+')
    f.write('[2019-08-06 13:22:32 +0000] [1574] [ERROR] Error /logs\r')  # noqa E501
    f.write('Traceback (most recent call last):\r')
    f.write('if pattern.search(line):\r')
