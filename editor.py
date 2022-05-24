def ask_user_for_input() -> str:
    return input('Choose a formatter:').strip()


def ask_user_for_text() -> str:
    return input('Text:').strip()


def ask_text_level() -> str:
    return input('Level:').strip()


def format_text_by_level(_text_level: int, _user_text: str) -> str:
    if _text_level == 1:
        return f'# {_user_text}'
    if _text_level == 2:
        return f'## {_user_text}'
    if _text_level == 3:
        return f'### {_user_text}'
    if _text_level == 4:
        return f'#### {_user_text}'
    if _text_level == 5:
        return f'##### {_user_text}'
    if _text_level == 6:
        return f'###### {_user_text}'


def format_text(_user_text: str, _correct_formatters: list, _formatter: str) -> str:
    if _formatter == _correct_formatters[0]:
        return _user_text
    if _formatter == _correct_formatters[1]:
        return f'**{_user_text}**'
    if _formatter == _correct_formatters[2]:
        return f'*{_user_text}*'
    if _formatter == _correct_formatters[5]:
        return f'`{_user_text}`'


def print_saved_formatted_text(_formatted_text: str) -> None:
    if not _formatted_text == '':
        print(_formatted_text)


def print_text(_raw_text: str, _formatted_text: str) -> None:
    if not _raw_text == '':
        print(f'{_raw_text}{_formatted_text}')


def print_newline_texts(_raw_text: str, _formatted_text: str) -> None:
    if not _raw_text == '':
        print(f'{_raw_text}{_formatted_text}\n')


def ask_user_for_label() -> str:
    return input('Label:').strip()


def ask_user_for_url() -> str:
    return input('URL:').strip()


def link_text(_user_label: str, _user_url: str, _saved_formatted_texts: str) -> str:
    return f'{_saved_formatted_texts}[{_user_label}]({_user_url})'


correct_formatters = ['plain', 'bold', 'italic', 'header', 'link', 'inline-code', 'ordered-list', 'unordered-list', 'new-line']
special_commands = ['!help', '!done']
format_with_text = {'plain', 'bold', 'italic', 'inline-code'}
format_without_text = {'new-line', 'link'}
formatted_text = ''
raw_text = ''
hello = ''
while True:
    formatter = ask_user_for_input()
    if not (formatter in correct_formatters or formatter in special_commands):
        print('Unknown formatting type or command')
    if formatter in format_with_text:
        while True:
            user_text = ask_user_for_text()
            formatted_text = format_text(user_text, correct_formatters, formatter)
            if raw_text == '':
                print(formatted_text)
                raw_text = formatted_text

                break

            if not hello == '':
                formatted_text = f'{hello}\n{formatted_text}'
            else:
                print_text(raw_text, formatted_text)

            break

    if formatter in format_without_text:
        if formatter == correct_formatters[8]:
            if hello == '':
                print_newline_texts(raw_text, formatted_text)
            print(formatted_text + '\n')
        if formatter == correct_formatters[4]:
            user_label = ask_user_for_label()
            user_url = ask_user_for_url()
            link_text = link_text(user_label, user_url, formatted_text)
            print(link_text)
            formatted_text = link_text
    if formatter == correct_formatters[3]:
        while True:
            text_level = int(ask_text_level())
            if 1 <= text_level <= 6:
                user_text = ask_user_for_text()
                print_saved_formatted_text(formatted_text)
                result = format_text_by_level(text_level, user_text)
                print(result, '\n')
                hello = result
                break
            else:
                print('The level should be within the range of 1 to 6')
    if formatter == special_commands[0]:
        correct_formatters_string = ' '.join(correct_formatters)
        special_commands_string = ' '.join(special_commands)
        print(f'Available formatters: {correct_formatters_string}\nSpecial commands: {special_commands_string}')
    if formatter == special_commands[1]:
        exit()
