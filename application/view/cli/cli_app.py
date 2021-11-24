from application.view.cli.main_menu import menu
from application.view.cli.records import show_all, add_record, delete_record


def main():
    while True:
        menu_pick = menu()
        match menu_pick:
            case "1":
                add_record()
            case "2":
                show_all()
            case "3":
                delete_record()
            case "9":
                break


if __name__ == '__main__':
    main()
