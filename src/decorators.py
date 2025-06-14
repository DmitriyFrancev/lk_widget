from typing import Any, Callable


def log(filename: str | None = None) -> Callable:
    """
    Принимает необязательный параметр filename. Если параметр не указан - выводит логи в консоль.
    Если указан - вывод логов осуществляется в текстовый файл.
    """
    def decorator_log(function: Any) -> Callable:
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            find_error = None
            result = None
            try:
                result = function(*args, **kwargs)
            except Exception as e:
                find_error = f'{function.__name__} error: {type(e).__name__}. Inputs: {args},{kwargs})\n'
                # print(find_error)

            if filename:
                if find_error:
                    with open(filename, 'a') as log_file:
                        log_file.write(find_error)
                else:
                    with open(filename, 'a') as log_file:
                        log_file.write(f'{function.__name__} ok\n')

            else:
                if find_error:
                    print(find_error)
                else:
                    print(f'{function.__name__} ok\n')

            return result
        return wrapper
    return decorator_log
