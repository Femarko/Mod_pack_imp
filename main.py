from application.salary import calculate_salary as cs
from application.db.people import get_employees as ge
from application.current_date import day, month, year

if __name__ == '__main__':
    print(f'{cs()}\t{day}.{month}.{year}')
    print(f'{ge()}\t{day}.{month}.{year}')