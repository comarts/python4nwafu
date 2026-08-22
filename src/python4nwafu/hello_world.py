#!/usr/bin/env python3
"""Hello World."""
import sys


def main():
    """主函数."""
    # 定义变量
    message = 'Hello, World!'
    name = 'Python Developer'
    year = 2026

    # 使用变量输出
    print(message)
    print(f'作者：{name}')
    print(f'当前年份：{year}')
    print(f'Python解释器路径: {sys.executable}')


if __name__ == '__main__':
    main()
