

def get_url_list(source):
    pass


class AdsHandler:
    def __init__(self) -> None:
        pass

    def add_record(self, record_data):
        """
        Adds a record to both new_ads and ads tables.
        """
        if not self._record_exists(record_data):
            print(f"Adding data {record_data} to database")
            self._add_new_ads_record(record_data)
            self._add_ads_record(record_data)

    def empty_new_ads_table(self):
        pass

    def delete_record(self, record):
        """
        Removes a record from the table.
        """
        pass

    def clean_outdated_records(self):
        """
        Checks if the session of the records has expired and if so, removes it.
        """
        pass

    def _record_exists(self, record_data):
        return False

    def _add_new_ads_record(self, record_data):
        pass

    def _add_ads_record(self, record_data):
        pass


ads_handler = AdsHandler()
