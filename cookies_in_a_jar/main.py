class Jar:
    number_of_cookies_in_jar = 0

    def __init__(self, capacity=12):
        if capacity <= 0:
            raise ValueError('Jar can not have a 0 or less than 1 capacity')
        self.capacity = capacity 

    def __str__(self):
        return '🍪' * Jar.number_of_cookies_in_jar 
    
    def deposit(self, n):
        if n > self.capacity:
            raise ValueError(f'The jar can not take more than {self.capacity} cookies')
        Jar.number_of_cookies_in_jar += n
