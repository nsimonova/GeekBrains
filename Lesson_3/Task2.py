# Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон. Функция должна принимать параметры как именованные
# аргументы. Реализовать вывод данных о пользователе одной строкой.
def user_information(name, surname, year_of_birth, city_of_residence, email, phone_number):
    print(name, surname, year_of_birth, city_of_residence, email, phone_number)


user_information(name='Vadim', surname='Kotov', year_of_birth='1991', city_of_residence='Moscow',
                 email='kotov.vadim@mail.ru', phone_number='+79153393933')
