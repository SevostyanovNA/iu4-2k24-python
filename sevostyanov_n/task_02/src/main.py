import argparse
from tree import print_tree

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Отображение иерархии файлов и папок в указанной директории')
    parser.add_argument('directory', nargs='?', default='.', help='Путь к директории (по умолчанию - текущая директория)')
    parser.add_argument('-L', type=int, metavar='level', help='Максимальный уровень вложенности')
    parser.add_argument('--symlinks', action='store_true', help='Показать символические ссылки')
    parser.add_argument('--hidden', action='store_true', help='Показать скрытые файлы и папки')
    args = parser.parse_args()

    print("Иерархия директории:")
    print_tree(args.directory, max_level=args.L, show_symlinks=args.symlinks, show_hidden=args.hidden)
