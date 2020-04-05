from _datetime import datetime

def logger(path):
    def write_log(func):
        with open(path, 'a', encoding='utf-8') as file:
            file.write(f'Function "some_function" was called at: {str(datetime.now())}\n')
        return func
    return write_log


@logger(path='log.txt')
def some_function():
    print('Function is doing something...')

some_function()