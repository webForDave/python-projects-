class Jar:
    number_of_cookies_in_jar = 0

    def __init__(self, capacity=12):
        if capacity <= 0:
            raise ValueError('Jar can not have a 0 or less than 1 capacity')
        self.__capacity = capacity 

    def __str__(self):
        if Jar.number_of_cookies_in_jar == 0:
            return 'The jar is empty'
        return '🍪' * Jar.number_of_cookies_in_jar 
    
    def deposit(self, n):
        if n > self.__capacity:
            raise ValueError(f"The jar can not take more than {self.capacity} cookies")
        Jar.number_of_cookies_in_jar += n

    def withdraw(self, n):
        if n > Jar.number_of_cookies_in_jar:
            raise ValueError(f"You cannot take more than {Jar.number_of_cookies_in_jar} cookies from the jar")
        Jar.number_of_cookies_in_jar -= n

    def capacity(self):
        return self.__capacity

    def size(self):
        return Jar.number_of_cookies_in_jar