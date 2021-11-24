from application.bll.records_controllers import get_all_records


def show_all():
    records = get_all_records()
    print("***********")
    print("All Records")
    print("***********")
    print()
    for record in records:
        print(record)


def add_record():
    pass


def delete_record():
    pass

