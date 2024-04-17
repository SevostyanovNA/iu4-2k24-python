import argparse
from tree import print_tree

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='����������� �������� ������ � ����� � ��������� ����������')
    parser.add_argument('directory', nargs='?', default='.', help='���� � ���������� (�� ��������� - ������� ����������)')
    parser.add_argument('-L', type=int, metavar='level', help='������������ ������� �����������')
    parser.add_argument('--symlinks', action='store_true', help='�������� ������������� ������')
    parser.add_argument('--hidden', action='store_true', help='�������� ������� ����� � �����')
    args = parser.parse_args()

    print("�������� ����������:")
    print_tree(args.directory, max_level=args.L, show_symlinks=args.symlinks, show_hidden=args.hidden)
