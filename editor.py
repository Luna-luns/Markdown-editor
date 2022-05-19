def ask_user_for_input() -> str:
    return input('Choose a formatter:').strip()


def ask_user_for_text() -> str:
    return input('Text:').strip()


def ask_text_level() -> str:
    return input('Level:')


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


correct_formatters = ['plain', 'bold', 'italic', 'header', 'link', 'inline-code', 'ordered-list', 'unordered-list', 'new-line']
special_commands = ['!help', '!done']
while True:
    formatter = ask_user_for_input()
    if not (formatter in correct_formatters or formatter in special_commands):
        print('Unknown formatting type or command.')
    if formatter == correct_formatters[3]:
        while True:
            text_level = int(ask_text_level())
            if 1 <= text_level <= 6:
                user_text = ask_user_for_text()
                print(format_text_by_level(text_level, user_text), '\n')
                break
            else:
                print('The level should be within the range of 1 to 6')
    while True:
        user_text = ask_user_for_text()
        print(format_text(user_text, correct_formatters, formatter))
        break
    if formatter == special_commands[0]:
        correct_formatters_string = ' '.join(correct_formatters)
        special_commands_string = ' '.join(special_commands)
        print(f'Available formatters: {correct_formatters_string}\nSpecial commands: {special_commands_string}')
    if formatter == special_commands[1]:
        exit()

