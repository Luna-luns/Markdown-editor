def ask_user_for_input() -> str:
    return input('Choose a formatter:')


correct_formatters = ['plain', 'bold', 'italic', 'header', 'link', 'inline-code', 'ordered-list', 'unordered-list', 'new-line']
special_commands = ['!help', '!done']
while True:
    formatter = ask_user_for_input()
    if formatter == '!help':
        correct_formatters_string = ' '.join(correct_formatters)
        special_commands_string = ' '.join(special_commands)
        print(f'Available formatters: {correct_formatters_string}\nSpecial commands: {special_commands_string}')
    if not (formatter in correct_formatters or formatter in special_commands):
        print('Unknown formatting type or command.')
    if formatter == '!done':
        exit()
