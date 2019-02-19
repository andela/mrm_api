from helpers.database import database_uri
from sqlalchemy import create_engine, MetaData


class DataDeletion:
    def clean_deleted_data(self):
        """
        This method deletes data that has been marked for
        deletion from the database
        """
        print("cleaning data...")
        database_engine = create_engine(database_uri)
        metadata = MetaData()
        metadata.reflect(bind=database_engine)

        for table in reversed(metadata.sorted_tables):
            try:
                statement = table.delete().where(table.c.state == "deleted")
                database_engine.execute(statement)
            except AttributeError:
                continue
