from application.salary import *
from application.db.people import *
from application.current_date import *



if __name__ == '__main__':
    print(f'{calculate_salary()}\t{day}.{month}.{year}')
    print(f'{get_employees()}\t{day}.{month}.{year}')