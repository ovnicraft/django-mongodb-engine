from django.db.backends import BaseDatabaseOperations
from pymongo.objectid import ObjectId

class DatabaseOperations(BaseDatabaseOperations):
    compiler_module = 'django_mongodb_engine.mongodb.compiler'

    def __init__(self, database_wrapper):
        super(DatabaseOperations, self).__init__()
        self.database = database_wrapper

    def quote_name(self, name):
        return name

    def value_to_db_date(self, value):
        # TODO - take a look at date queries
        # value is a date here, no need to check it
        return value

    def sql_flush(self, style, tables, sequence_list):
        for table in tables:
            self.database.db_connection.drop_collection(table)
        return tables

    def value_to_db_datetime(self, value):
        # value is a datetime here, no need to check it
        return value

    def value_to_db_time(self, value):
        # value is a time here, no need to check it
        return value

    def prep_for_like_query(self, value):
        return value

    def check_aggregate_support(self, aggregate):
        """
        This function is meant to raise exception if backend does
        not support aggregation.
        
        In fact, mongo probably even has more flexible aggregation
        support than relational DB
        """
        pass

    def value_to_db_auto(self, value):
        """
        Transform a value to an object compatible with the auto field required
        by the backend driver for auto columns.
        """
        if value is None:
            return None
        return ObjectId(value)
