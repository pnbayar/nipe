import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print(f"Execution time: {time.time() - start:.4f}s")
        return result
    return wrapper

@timer
def example():
    time.sleep(1)
    return "Done"

print(example())
