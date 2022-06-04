def ask_user_for_formatter() -> str:
    return input('Choose a formatter:').strip()


def ask_user_for_text() -> str:
    return input('Text:').strip()


def ask_text_level() -> str:
    return input('Level:').strip()


def format_text_by_level() -> str:
    text_level = int(ask_text_level())
    _user_text = ask_user_for_text()
    if 1 <= text_level <= 6:
        return ' '.join(['#' * text_level, _user_text]) + '\n'

    return 'The level should be within the range of 1 to 6'


def ask_user_for_label() -> str:
    return input('Label:').strip()


def ask_user_for_url() -> str:
    return input('URL:').strip()


def link_text() -> str:
    user_label = ask_user_for_label()
    user_url = ask_user_for_url()
    return f'[{user_label}]({user_url})'


def ask_user_for_rows() -> str:
    return input('Number of rows:').strip()


def ask_text_for_rows(_rows: int, _count: int) -> str:
    return input(f'Row #{_count}:')


def create_list(_user_formatter: str) -> str:
    while True:
        rows = int(ask_user_for_rows())
        if rows > 0:
            count = 1
            mark = '*'
            result_list = []
            for elem in range(1, int(rows) + 1):
                row_text = ask_text_for_rows(int(rows), count).strip()
                if _user_formatter == 'ordered-list':
                    result_list.append(f'{count}. {row_text}')
                else:
                    result_list.append(f'{mark} {row_text}')
                count += 1
            return '\n'.join(result_list)
        else:
            print('The number of rows should be greater than zero')


def append_formatter(_user_formatter: str) -> str:
    if _user_formatter == 'plain':
        _user_text = ask_user_for_text()
        return _user_text
    if _user_formatter == 'bold':
        _user_text = ask_user_for_text()
        return f'**{_user_text}**'
    if _user_formatter == 'italic':
        _user_text = ask_user_for_text()
        return f'*{_user_text}*'
    if _user_formatter == 'header':
        return format_text_by_level()
    if _user_formatter == 'link':
        return link_text()
    if _user_formatter == 'inline-code':
        _user_text = ask_user_for_text()
        return f'`{_user_text}`'
    if _user_formatter == 'new-line':
        return '\n'
    if _user_formatter == 'ordered-list' or 'unordered-list':
        return create_list(_user_formatter) + '\n'


def check_formatter_correctness(_user_formatter: str, _formatters_list: list, _special_commands: list) -> str:
    if (_user_formatter not in _formatters_list) and (_user_formatter not in _special_commands):
        return 'Unknown formatting type or command'


def add_formatted_text(_saved_text: str, _formatted_text: str, _user_formatter: str) -> str:
    if not _saved_text == '':
        if _user_formatter == 'header':
            return _saved_text + '\n' + _formatted_text
        else:
            return _saved_text + _formatted_text

    return _formatted_text


def append_special_commands(_user_formatter: str, _formatters_list: list, _special_commands: list) -> str:
    if _user_formatter == '!done':
        with open('output.md', 'w') as output:
            output.write(saved_text)
        exit()
    if _user_formatter == '!help':
        formatters_list_string = ' '.join(_formatters_list)
        special_commands_string = ' '.join(_special_commands)
        return f'Available formatters: {formatters_list_string}\nSpecial commands: {special_commands_string}'


formatters_list = ['plain', 'bold', 'italic', 'header', 'link', 'inline-code', 'ordered-list', 'unordered-list', 'new-line']
special_commands = ['!help', '!done']
saved_text = ''
while True:
    user_formatter = ask_user_for_formatter()
    formatter_correctness = check_formatter_correctness(user_formatter, formatters_list, special_commands)
    if not formatter_correctness:
        if user_formatter in special_commands:
            print(append_special_commands(user_formatter, formatters_list, special_commands))
        else:
            formatted_text = append_formatter(user_formatter)
            result = add_formatted_text(saved_text, formatted_text, user_formatter)
            print(result)
            saved_text = result
    else:
        print(formatter_correctness)
