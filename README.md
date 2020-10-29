# DiaboticalAPI
Get information from https://www.diabotical.com/api

Требования
1. Вывести информацию (все поля, кроме user_id) в STDOUT о N игроках в json формате.
Аргумент count необязательный - по умолчанию вывести столько же записей, сколько
возвращает API. Аргумент mode (режим игры) как в API.
$ python ./leaderboard.py --mode <MODE> --count 3
2. Найти и вывести информацию об игроке с определенным user_id с учётом count :
$ python ./leaderboard.py --mode <MODE> --count N --user_id < user_id >
3. Посчитать количество игроков определенной страны и вывести в STDOUT число (с учетом
count ):
$ python ./leaderboard.py --mode <MODE> --count N --country ru

- Приветствуется реализация на Python. Но допускается решение на любом другом языке с
динамической типизацией: Ruby, Perl, etc.
- Следует обратить внимание на обработку ошибок: недоступен API, неверный игровой режим
( mode ) и т.д.
- Можно использовать любые сторонние библиотеки. Например, requests.
- Unit tests приветствуются.
