from helpers.database import database_uri
from sqlalchemy import create_engine, MetaData, and_
from datetime import timedelta, datetime
import celery


@celery.task(name='clean_archived_data.delete_archived_data')
def delete_archived_data():
    """
        This method deletes data that has been deleted for
        more than 30 days
        """
    database_engine = create_engine(database_uri)
    metadata = MetaData()
    metadata.reflect(bind=database_engine)

    for table in reversed(metadata.sorted_tables):
        try:
            now = datetime.now()
            delta = now - timedelta(days=30)
            statement = table.delete().where(
                and_(table.c.date_updated < delta, table.c.state == 'archived'))
            database_engine.execute(statement)
        except AttributeError:
            continue
