"""用户名."""
import os


def get_current_username():
    """跨平台获取当前用户名."""
    if os.name == 'nt':           # Windows
        return os.environ.get('USERNAME', '')
    else:                        # Linux / macOS
        return os.environ.get('LOGNAME') or os.environ.get('USER', '')

print(get_current_username())
