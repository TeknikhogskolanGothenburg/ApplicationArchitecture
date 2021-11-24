from application.dll.repository import records_repository as rr


def get_all_records():
    return rr.get_all_records()
