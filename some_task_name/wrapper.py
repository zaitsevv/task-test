from typing import (
    Callable,
    Optional,
    TypeVar,
    ParamSpec
)

Param = ParamSpec("Param")
RetType = TypeVar("RetType")

def with_exception_handling(func: Callable[Param, RetType]) -> Callable[Param, RetType]:
    def wrapper(*args: Param.args, **kwargs: Param.kwargs) -> Optional[RetType]:
        try:
            result = func(*args, **kwargs)
            return result
        except Exception as e:
            print(f"Error: {e=}")
    return wrapper
