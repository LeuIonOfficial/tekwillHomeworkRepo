import time


def benchmark_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"It took {end_time - start_time:.2f} seconds to execute {func.__name__}")
        return result

    return wrapper


@benchmark_time
def my_function():
    time.sleep(5)


my_function()
