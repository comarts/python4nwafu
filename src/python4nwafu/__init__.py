""""脚本演示."""
_HIDDEN_ONE = 1
PUBLIC_ONE = 1

def _hidden_sub() -> None:
    """被隐藏的函数."""
    print('Hello from _hidden_sub()!')

def public_sub() -> None:
    """普通函数."""
    print('Hello from public_sub()!')
