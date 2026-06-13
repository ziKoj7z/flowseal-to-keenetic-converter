import re
import os

def format_nfqws_config(input_text):
    start_idx = input_text.find('--filter')
    if start_idx != -1:
        input_text = input_text[start_idx:]
    else:
        start_idx = input_text.find('--')
        if start_idx != -1:
            input_text = input_text[start_idx:]

    #Словарь с точными заменами
    replacements = {
        "%GameFilterUDP%": "1024-65535",
        "%GameFilterTCP%": "1024-65535",
        '--hostlist="%LISTS%list-general.txt"': "--hostlist=/opt/etc/nfqws/list-general.list",
        '--hostlist="%LISTS%list-general-user.txt"': "--hostlist=/opt/etc/nfqws/list-general-user.list",  
        '--hostlist-exclude="%LISTS%list-exclude.txt"': "--hostlist-exclude=/opt/etc/nfqws/list-exclude.list",
        '--hostlist-exclude="%LISTS%list-exclude-user.txt"': "--hostlist-exclude=/opt/etc/nfqws/list-exclude-user.list",  
        '--ipset-exclude="%LISTS%ipset-exclude.txt"': "--ipset-exclude=/opt/etc/nfqws/ipset-exclude.list",
        '--ipset-exclude="%LISTS%ipset-exclude-user.txt"': "--ipset-exclude=/opt/etc/nfqws/ipset-exclude-user.list",  
        '--ipset="%LISTS%ipset-all.txt"': "--ipset=/opt/etc/nfqws/ipset-all.list",
        '--hostlist="%LISTS%list-google.txt"': "--hostlist=/opt/etc/nfqws/list-google.list",

        '"%BIN%tls_clienthello_max_ru.bin"': "/opt/etc/nfqws/fake/tls_clienthello_max_ru.bin",
        '"%BIN%tls_clienthello_www_google_com.bin"': "/opt/etc/nfqws/fake/tls_clienthello_www_google_com.bin",
        '"%BIN%stun.bin"': "/opt/etc/nfqws/fake/stun.bin",
        '"%BIN%quic_initial_dbankcloud_ru.bin"': "/opt/etc/nfqws/fake/quic_initial_dbankcloud_ru.bin",
        '^': ""
    }
    for old, new in replacements.items():
        input_text = input_text.replace(old, new)
    input_text = re.sub(r'"%BIN%([^"]+)"', r'/opt/etc/nfqws/fake/\1', input_text)
    input_text = re.sub(r'\s+', ' ', input_text).strip()
    args = input_text.split(' --')
    
    formatted_lines = []
    for arg in args:
        arg = arg.strip()
        if not arg:
            continue
        if arg.startswith('wf-tcp') or arg.startswith('wf-udp') or 'winws.exe' in arg:
            continue
        if not arg.startswith('--'):
            arg = '--' + arg
        formatted_lines.append(arg)
        if arg == '--new':
            formatted_lines.append('')

    return '\n'.join(formatted_lines).strip()

if __name__ == "__main__":
    print("Перетащите .bat файл в это окно и нажмите Enter, результат будет сохранён в папке с исходным файлом:")
    file_path = input().strip('''&'" ''')
    if os.path.exists(file_path):
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                raw_text = f.read()
            result = format_nfqws_config(raw_text)
            base_name, _ = os.path.splitext(file_path)
            output_path = f"{base_name}_edited.txt"
            with open(output_path, "w", encoding="utf-8") as f:
                f.write(result)
        except Exception as e:
            print(f"\nПроизошла ошибка при обработке файла: {e}")
    else:
        print("\nОшибка: Файл не найден. Проверьте правильность пути.")
