
import math


def summa (first, second):

    return first + second


def sub (first, second):

    return first - second


def mult (first, second):

    return first * second


def div (first, second):

    return first / second


def calc(first, second, oper):

    result = None

    if oper == '+':

        result = summa(first, second)

    elif oper == '-':

        result = sub(first, second)

    elif oper == '*':

        result = mult(first, second)

    elif oper == '/':

        if (second == 0):

            print('������� �� ���� ���������!')

            return

        result = div(first, second)

    elif oper == '%':

        result = first / second * 100

    elif oper == '**':

        result = first ** second

    elif oper == 'log':

        result = math.log(first, second)

    else:

        print('������������ ��������!')

    return result


def operation():

    mes = input('�������� �������� (������� +, -, *, /, %, **, log):\n '

                '+ - �������� ���� �����\n'

                '- - ��������� ���� �����\n'

                '* - ��������� ���� �����\n'

                '/ - ������� ���� �����\n'

                '% - ������� ������� ����� �� �������\n'

                '** - ���������� ������� ����� � ������� �������\n'

                'log - �������� ������� ����� �� ��������� �������\n')

    if mes == '+':

        print('�� ������� �����')

    elif mes == '-':

        print('�� ������� ��������')

    elif mes == '*':

        print('�� ������� ���������')

    elif mes == '/':

        print('�� ������� �������')

    elif mes == '%':

        print('�� ������� ���������� �������� ������� ����� �� �������')

    elif mes == '**':

        print('�� ������� ���������� � �������')

    elif mes == 'log':

        print('�� ������� ��������')


    correct_operations = ['+', '-', '*', '/', '%', '**', 'log']

    while mes not in correct_operations:

        print('����� �������� ��� � ������. ���������� ���!')

        mes = input()


    return mes

def run():

    try:

        first = int(input('������� ������ �����: '))

    except ValueError:

        first = int(input('�� ����� ������������ ������. ����������, ������� ����� �����.'))

    try:

        second = int(input('������� ������ �����: '))

    except ValueError:

        second = int(input('�� ����� ������������ ������. ����������, ������� ����� �����.'))

    op = operation()

    result = calc(first, second, op)

    print(f'���������: {result}')

    progam_is_running = True

    while(progam_is_running):

    run()

    answer = input('������� ����������?\n'

      ' ������� + ���� �� � ������ ������, ���� ���: ')

    if answer != '+':

        progam_is_running = False