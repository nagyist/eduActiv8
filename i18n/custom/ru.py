# -*- coding: utf-8 -*-

# Translated by Anton Kayukov (Антон Каюков), Alexey Loginov (Алексей Логинов)

# FAO Translators:
# First of all thank you for your interest in translating this game,
# I will be grateful if you could share it with the community -
# if possible please send it back to my email, and I'll add it to the next version.

# The translation does not have to be exact as long as it makes sense and fits in its location
# (if it doesn't I'll try to either make the font smaller or make the area wider - where possible).
# The colour names in other languages than English are already in smaller font.

d = dict()  # messages for display
dp = dict()  # messages with pronunciation exceptions - this dictionary will override entries in a copy of d

d["local_kbrd"] = "Русскими буквами"
d[
    "Clock0 - Russian official time"] = "Научитесь читать официальное русское время"  # Learn to read Russian official time
d["Russian official - subtitle"] = ""

d["Clock2 - Russian official time"] = "Официальное русское время"  # Russian official time
d["Russian official - txt_only"] = "Протестируйте сами себя"  # test yourself

numbers = ["один", "два", "три", "четыре", "пять", "шесть", "семь", "восемь", "девять", "десять", "одиннадцать",
           "двенадцать", "тринадцать", "четырнадцать", "пятнадцать", "шестнадцать", "семнадцать", "восемнадцать",
           "девятнадцать", "двадцать", "двадцать один", "двадцать два", "двадцать три", "двадцать четыре",
           "двадцать пять", "двадцать шесть", "двадцать семь", "двадцать восемь", "двадцать девять"]
numbers2090 = ['двадцать', 'тридцать', 'сорок', 'пятьдесят', 'шестьдесят', 'семьдесят', 'восемьдесят', 'девяносто']

# dp['abc_flashcards_word_sequence'] = ['Автобус', 'Банка', 'Виноград','Гитара','Дом','Ель', 'Ёж', 'Жеребец', 'Зебра',  'Иглу', 'Йога','Кошка','Лев', 'Муравей', 'Ночь', 'Обувь', 'Попугай', 'Рыба', 'Слон','Томат','Утка','Филин', 'Хлеб', 'Цветок', 'Чайник', 'Шлюпка', 'Щука','Съёмка', 'Мышь', 'Нить', 'Электричка', 'Юбка', 'Яхта']
d['abc_flashcards_word_sequence'] = ['<1>А<2>втобус', '<1>Б<2>анка', '<1>В<2>иноград', '<1>Г<2>итара', '<1>Д<2>ом',
                                     '<1>Е<2>ль', '<1>Ё<2>ж', '<1>Ж<2>еребец', '<1>З<2>ебра', '<1>И<2>глу',
                                     '<1>Й<2>ога', '<1>К<2>ош<1>к<2>а', '<1>Л<2>ев', '<1>М<2>уравей', '<1>Н<2>очь',
                                     '<1>О<2>бувь', '<1>П<2>о<1>п<2>угай', '<1>Р<2>ыба', '<1>С<2>лон', '<1>Т<2>ома<1>т',
                                     '<1>У<2>тка', '<1>Ф<2>илин', '<1>Х<2>леб', '<1>Ц<2>веток', '<1>Ч<2>айник',
                                     '<1>Ш<2>люпка', '<1>Щ<2>ука', '<2>С<1>ъ<2>ёмка', '<2>М<1>ы<2>шь', '<2>Нит<1>ь',
                                     '<1>Э<2>лектричка', '<1>Ю<2>бка', '<1>Я<2>хта']
d['abc_flashcards_frame_sequence'] = [77, 9, 6, 28, 7, 31, 29, 45, 25, 8, 32, 2, 11, 0, 54, 60, 15, 5, 4, 33, 3, 14, 35,
                                      69, 19, 1, 38, 39, 12, 24, 63, 41, 66]

# alphabet ru: - 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя' & 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
alphabet_lc = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у',
               'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']
alphabet_uc = ['А', 'Б', 'В', 'Г', 'Д', 'Е', 'Ё', 'Ж', 'З', 'И', 'Й', 'К', 'Л', 'М', 'Н', 'О', 'П', 'Р', 'С', 'Т', 'У',
               'Ф', 'Х', 'Ц', 'Ч', 'Ш', 'Щ', 'Ъ', 'Ы', 'Ь', 'Э', 'Ю', 'Я']
# correction of eSpeak pronounciation of single letters if needed
letter_names = []

accents_lc = ['-']
accents_uc = []


def n2txt(n, twoliner=False):
    "takes a number from 1 - 99 and returns it back in a word form, ie: 63 returns 'sixty three'."
    if 0 < n < 30:
        return numbers[n - 1]
    elif 30 <= n < 100:
        m = n % 10
        tens = numbers2090[(n // 10) - 2]
        if m == 0:
            return tens
        elif m > 0:
            ones = numbers[m - 1]
            if twoliner:
                return [tens, ones]
            else:
                return tens + " " + ones
    elif n == 0:
        return "ноль"
    elif n == 100:
        return "сто"
    return ""


# TIME FOR DISPLAY
mt1 = ["одна", "две", "три", "четыре", "пять", "шесть", "семь", "восемь", "девять", "десять", "одиннадцать",
       "двенадцать", "тринадцать", "четырнадцать", "пятнадцать", "шестнадцать", "семнадцать", "восемнадцать",
       "девятнадцать", "двадцать", "двадцать одна", "двадцать две", "двадцать три", "двадцать четыре", "двадцать пять",
       "двадцать шесть", "двадцать семь", "двадцать восемь", "двадцать девять", "тридцать", "тридцать одна",
       "тридцать две", "тридцать три", "тридцать четыре", "тридцать пять", "тридцать шесть", "тридцать семь",
       "тридцать восемь", "тридцать девять"]
mt2 = ["одной", "двух", "трёх", "четырёх", "пяти", "шести", "семи", "восьми", "девяти", "десяти", "одиннадцати",
       "двенадцати", "тринадцати", "четырнадцати", "пятнадцати", "шестнадцати", "семнадцати", "восемнадцати",
       "девятнадцати", "двадцати", "двадцати одной", "двадцати двух", "двадцати трёх", "двадцати четырёх",
       "двадцати пяти", "двадцати шести", "двадцати семи", "двадцати восьми", "двадцати девяти"]

ht1 = ["час", "два", "три", "четыре", "пять", "шесть", "семь", "восемь", "девять", "десять", "одиннадцать",
       "двенадцать"]
ht2 = ["первого", "второго", "третьего", "четвёртого", "пятого", "шестого", "седьмого", "восьмого", "девятого",
       "десятого", "одиннадцатого", "двенадцатого"]


def time2str_short(h, m):
    'takes 2 variables: h - hour, m - minute, returns time as a string, ie. six fifty five - for 6:55'
    if m > 0:
        if h == 12:
            h = 1
        else:
            h += 1

    if m == 0:
        if h == 1:
            return "один час"
        elif h < 5:
            return "%s часа" % ht1[h - 1]
        else:
            return "%s часов" % ht1[h - 1]
    elif m == 15:
        return "четверть %s" % ht2[h - 1]
    elif m == 20:
        return "%s минут %s" % (mt1[m - 1], ht2[h - 1])
    elif m in [1, 21]:
        return "%s минута %s" % (mt1[m - 1], ht2[h - 1])
    elif m in [2, 3, 4, 22, 23, 24]:
        return "%s минуты %s" % (mt1[m - 1], ht2[h - 1])
    elif m < 30:
        return "%s минут %s" % (mt1[m - 1], ht2[h - 1])
    elif m == 30:
        return "половина %s" % ht2[h - 1]
    elif m == 39:
        return "без двадцати одной минуты %s" % ht1[h - 1]
    elif m == 40:
        return "без %s минут %s" % (mt2[60 - m - 1], ht1[h - 1])
    elif m == 45:
        return "без четверти %s" % ht1[h - 1]
    elif m == 59:
        return "без одной минуты %s" % ht1[h - 1]
    elif m > 30:
        return "без %s минут %s" % (mt2[60 - m - 1], ht1[h - 1])
    return ""


def time2str(h, m):
    'takes 2 variables: h - hour, m - minute, returns time as a string, ie. five to seven - for 6:55'

    # get the right "suffix" for hour
    if h == 1:
        sf = "час"
    elif h < 5:
        sf = "часа"
    else:
        sf = "часов"

    if m == 0:
        return "%s %s" % (numbers[h - 1], sf)
    elif m == 1:
        return "%s %s одна минута" % (numbers[h - 1], sf)
    elif m in [21, 31, 41, 51]:
        return "%s %s %s одна минута" % (numbers[h - 1], sf, n2txt(m - 1))
    elif m == 2:
        return "%s %s две минуты" % (numbers[h - 1], sf)
    elif m in [22, 32, 42, 52]:
        return "%s %s %s две минуты" % (numbers[h - 1], sf, n2txt(m - 2))
    elif m in [3, 4, 23, 24, 33, 34, 43, 44, 53, 54]:
        return "%s %s %s минуты" % (numbers[h - 1], sf, n2txt(m))
    else:
        return "%s %s %s минут" % (numbers[h - 1], sf, n2txt(m))

#write a fraction in words
numerators = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve']
d_singular = ['', 'half', 'third', 'quarter', 'fifth', 'sixth', 'seventh', 'eighth', 'ninth', 'tenth', 'eleventh', 'twelfth']
d_plural = ['', 'halves', 'thirds', 'quarters', 'fifths', 'sixths', 'sevenths', 'eighths', 'ninths', 'tenths', 'elevenths', 'twelfths']

def fract2str(n, d):
    if n == 1:
        return numerators[0] + " " + d_singular[d-1]
    else:
        return numerators[n-1] + " " + d_plural[d-1]


# TIME FOR SPEAKER
spkmt1 = ["одна", "две", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19",
          "20", "20 одна", "20 две", "23", "24", "25", "26", "27", "28", "29", "30", "30 одна", "30 две", "33", "34",
          "35", "36", "37", "38", "39"]
spkmt2 = ["одной", "двух", "трёх", "четырёх", "пяти", "шести", "семи", "вось-ми", "девя-ти", "десяти", "1-надца-ти",
          "две-надца-ти", "три-надца-ти", "четыр-надца-ти", "пят-надца-ти", "шест-надца-ти", "сем-надца-ти",
          "восем-надца-ти", "девят-надца-ти", "двадца-ти", "двадца-ти одной", "двадца-ти двух", "двадца-ти трёх",
          "двадца-ти четырёх", "двадца-ти пяти", "двадца-ти шести", "двадца-ти семи", "двадца-ти вось-ми",
          "двадца-ти девя-ти"]

spkht1 = ["час", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12"]
spkht2 = ["пер-во-во", "второго", "треть-его", "четвёртого", "пя-то-во", "шестого", "седьмого", "восьмого", "девятого",
          "десятого", "1-надца-того", "две-надца-того"]

spknumbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19",
              "20", "21", "22", "23", "24", "25", "26", "27", "28", "29"]


def time2spk_short(h, m):
    'takes 2 variables: h - hour, m - minute, returns time as a string but in exception format for espeak Russian language'
    if m > 0:
        if h == 12:
            h = 1
        else:
            h += 1

    if m == 0:
        if h == 1:
            return "1 час"
        elif h < 5:
            return "%s ча-са" % spkht1[h - 1]
        else:
            return "%s ча-сов" % spkht1[h - 1]
    elif m == 15:
        return "чет-верть %s" % spkht2[h - 1]
    elif m == 20:
        return "%s минут %s" % (spkmt1[m - 1], spkht2[h - 1])
    elif m in [1, 21]:
        return "%s минута %s" % (spkmt1[m - 1], spkht2[h - 1])
    elif m in [2, 3, 4, 22, 23, 24]:
        return "%s минуты %s" % (spkmt1[m - 1], spkht2[h - 1])
    elif m < 30:
        return "%s минут %s" % (spkmt1[m - 1], spkht2[h - 1])
    elif m == 30:
        return "половина %s" % spkht2[h - 1]
    elif m == 39:
        return "без двад-ца-ти одной минуты %s" % spkht1[h - 1]
    elif m == 40:
        return "без %s минут %s" % (spkmt2[60 - m - 1], spkht1[h - 1])
    elif m == 45:
        return "без четвер-ти %s" % spkht1[h - 1]
    elif m == 59:
        return "без од-ной минуты %s" % spkht1[h - 1]
    elif m > 30:
        return "без %s минут %s" % (spkmt2[60 - m - 1], spkht1[h - 1])
    return ""


def time2spk(h, m):
    'takes 2 variables: h - hour, m - minute, returns time as a string, ie. five to seven - for 6:55'

    # get the right "suffix" for hour
    if h == 1:
        sf = "час"
    elif h < 5:
        sf = "ча-са"
    else:
        sf = "ча-сов"

    if m == 0:
        return "%s %s" % (spknumbers[h - 1], sf)
    elif m == 1:
        return "%s %s одна минута" % (spknumbers[h - 1], sf)
    elif m in [21, 31, 41, 51]:
        return "%s %s %d-одна минута" % (spknumbers[h - 1], sf, m - 1)
    elif m == 2:
        return "%s %s две минуты" % (spknumbers[h - 1], sf)
    elif m in [22, 32, 42, 52]:
        return "%s %s %d-две минуты" % (spknumbers[h - 1], sf, m - 2)
    elif m in [3, 4, 23, 24, 33, 34, 43, 44, 53, 54]:
        return "%s %s %d минуты" % (spknumbers[h - 1], sf, m)
    else:
        return "%s %s %d минут" % (spknumbers[h - 1], sf, m)
    return ""


d["a4a_animals"] = ["корова", "индейка", "креветка", "волк", "пантера", "панда", "сорока", "моллюск", "пони", "мышь",
                    "мопс", "коала", "лягушка", "божья коровка", "горилла", "лама", "стервятник", "хомяк", "птица",
                    "морская звезда", "ворона", "длиннохвостый попугай", "гусеница", "тигр", "колибри", "пиранья",
                    "свинья", "скорпион", "лиса", "леопард", "игуана", "дельфин", "летучая мышь", "цыплёнок", "краб",
                    "курица", "оса", "хамелион", "кит", "ёжик", "олень", "лось", "пчела", "змея", "сорокопут", "осёл",
                    "морская свинка", "ленивец", "конь", "пингвин", "выдра", "медведь", "зебра", "страус", "верблюд",
                    "антилопа", "лемур", "голубь", "лама", "крот", "скат", "баран", "скунс", "медуза", "овца", "акула",
                    "котёнок", "олень", "улитка", "фламинго", "кролик", "устрица", "бобр", "воробей", "голубь", "орёл",
                    "жук", "бегемот", "сова", "кобра", "саламандра", "гусь", "кенгуру", "стрекоза", "лягушка",
                    "пеликан", "кальмар", "львёнок", "ягуар", "утка", "ящерица", "носорог", "гиена", "бык", "павлин",
                    "попугай", "лось", "крокодил", "муравей", "козёл", "крольчонок", "лев", "белка", "опоссум",
                    "шимпанзе", "оленёнок", "суслик", "слон", "жираф", "паук", "щенок", "сойка", "тюлень", "петух",
                    "черепаха", "бык", "кошка", "крыса", "улитка", "бизон", "чёрный дрозд", "лебедь", "омар",
                    "собака", "комар", "змея", "цыплёнок", "муравьед"]
d["a4a_sport"] = ["дзюдо", "плавание", "велогонка", "растяжка", "шлем", "коньки", "ходьба", "бег", "бег", "ныряние",
                  "батут", "пеший туризм", "бокс", "хоккей", "забег", "бросок", "скейт", "победа", "приседания", "лыжи",
                  "гольф", "свисток", "факел", "яхта", "стойка", "теннис", "скачок", "гребля", "бег трусцой",
                  "скакалка"]
d["a4a_body"] = ["зуб", "щека", "косточка", "колено", "пята", "мускул", "рот", "ступня", "рука", "локоть", "волосы",
                 "ресничка", "борода", "пупок", "большой палец", "грудь", "ноздря", "нос", "поясница", "рука", "бровь",
                 "кулак", "шея", "запястье", "горло", "глаз", "нога", "спина", "ухо", "палец", "ступня", "борода",
                 "лицо", "спина", "подбородок", "ягодицы", "бедро", "живот"]
d["a4a_people"] = ["девушка", "парень", "сын", "одноклассники", "друзья", "малыш", "ребёнок", "папа", "мама",
                   "близнецы", "братья", "мужчина", "мать", "дедушка", "семья", "женщина", "жена", "муж", "невеста",
                   "тётя", "бабушка", "влюблённые", "мальчик", "двойняшки", "дикари", "мальчик", "сёстры", "женщина",
                   "леди"]
d["a4a_food"] = ["конфета", "сосиска", "гамбургер", "бифштекс", "помадка", "пончик", "кокос", "рис", "мороженое",
                 "желе", "йогурт", "десерт", "десерт", "крендель", "арахис", "варенье", "курица", "бекон", "специи",
                 "кофе", "пирог", "лимонад", "шоколад", "бутылка с водой", "обед", "лёд", "сахар", "соус", "суп", "сок",
                 "чипсы", "торт", "пюре", "чай", "булка", "сыр", "отбивная", "бутерброд", "ломтик", "посыпка", "пицца",
                 "мука", "жевательная резинка", "спагетти", "жаркое", "напиток", "тушёное мясо", "намазанное", "мясо",
                 "молоко", "пища", "кукуруза", "хлеб", "орех", "яйцо", "хот-дог", "ветчина"]
d["a4a_clothes_n_accessories"] = ["украшение", "носок", "пиджак", "шпилька", "пятно", "шорты", "карман", "ожерелье",
                                  "свитер", "униформа", "плащ", "штаны", "солнечные очки", "куртка", "пулловер",
                                  ",блузка", "сандалии", "костюм", "пижама", "юбка", "молния", "туфли", "камень",
                                  "галстук", "шлёпанцы", "перчатки", "шляпа", "рукав", "кепка", "купальник",
                                  "кроссовки", "жилет", "перчатки", "шнурок", "заплатка", "шарф", "ботинок", "пуговица",
                                  "платье", "пояс", "подошва", "мантия", "трусы", "кимоно", "комбинезон"]
d["a4a_actions"] = ["лизать", "забрасывать", "молиться", "падать", "царапать", "трогать", "нюхать", "смотреть",
                    "карабкаться", "копать", "выть", "спать", "исследовать", "рисовать", "обнимать", "учить", "дремать",
                    "лепить", "ловить", "хлопать", "плакать", "петь", "встречаться", "продавать", "клевать", "ударить",
                    "становиться на колени", "искать", "танцевать", "кашлять", "резать", "думать", "лаять", "говорить",
                    "веселить", "стряпать", "писать", "бить", "бренчать", "учиться", "пахать", "мечтать", "отправлять",
                    "нырять", "шептать", "рыдать", "трясти", "кормить", "ползти", "обосноваться", "разливать", "мыть",
                    "кричать", "рвать", "плавать", "тянуть", "поесть", "целовать", "сидеть", "вылупляться", "мигать",
                    "слушать", "целоваться", "играть", "мыть", "говорить", "вести", "пить", "летать", "жонглировать",
                    "кусать", "мести", "смотреть", "вязать", "поднимать", "держать", "читать", "квакать", "оставаться",
                    "есть"]
d["a4a_construction"] = ["маяк", "дверь", "цирк", "церковь", "конура", "храм", "дым", "дымоход", "кирпич", "колодец",
                         "улица", "замок", "магазин", "лестница", "школа", "ферма", "мост", "плотина", "пирамида",
                         "кладовая", "мельница", "окно", "домик", "ступенька", "магазин", "сарай", "крыша",
                         "колокольня", "гараж", "мечеть", "госпиталь", "палатка", "дом", "стена", "банк", "ставень",
                         "хижина"]
d["a4a_nature"] = ["земля", "утёс", "холм", "каньон", "камень", "море", "озеро", "пляж", "побережье", "гора", "пруд",
                   "вершина", "лава", "пещера", "дюна", "остров", "лес", "пустыня", "айсберг"]
d["a4a_jobs"] = ["клоун", "инженер", "священник", "ветеринар", "судья", "повар", "атлет", "библиотекарь", "жонглёр",
                 "полицейский", "водопроводчик", "жетонщик", "королева", "фермер", "фокусник", "рыцарь", "доктор",
                 "каменщик", "уборщица", "учитель", "охотник", "солдат", "музыкант", "юрист", "рыбак", "принцесса",
                 "пожарник", "монахиня", "пират", "ковбой", "электрик", "няня", "король", "президент", "клерк",
                 "плотник", "жокей", "рабочий", "механик", "пилот", "актёр", "повар", "студент", "мясник", "бухгалтер",
                 "принц", "поп", "моряк", "боксёр", "балерина", "тренер", "астронавт", "художник", "анестезиолог",
                 "учёный"]
d["a4a_fruit_n_veg"] = ["морковь", "смородина", "сельдерей", "редька", "какао", "персик", "дыня", "грейпфрут",
                        "брокколи", "виноград", "шпинат", "инжир", "косточка", "редис", "помидор", "киви", "спаржа",
                        "оливки", "огурцы", "бобы", "клубника", "перцы", "малина", "абрикос", "картофель", "горох",
                        "капуста", "вишни", "тыква", "ежевика", "груша", "апельсин", "тыква", "авокадо", "чеснок",
                        "лук", "яблоко", "лайм", "цветная капуста", "манго", "салат", "лимон", "баклажан", "артишоки",
                        "сливы", "лук", "бананы", "папайа"]
d["a4a_transport"] = ["яхта", "такси", "автомобиль", "велосипед", "плот", "педаль", "автобус", "руль", "лодка", "пикап",
                      "сани", "ковёр", "мотоцикл", "поезд", "корабль", "фургон", "каноэ", "ракета", "мачта", "санки",
                      "велосипед"]

dp["a4a_animals"] = ["корова", "индейка", "креветка", "волк", "пантера", "панда", "сорока", "моллюск", "пони", "мышь",
                     "мопс", "коала", "лягушка", "божья коровка", "горилла", "лама", "стервятник", "хомяк", "птица",
                     "морская звезда", "ворона", "длиннохвостый попугай", "гусеница", "тигр", "колибри", "пиранья",
                     "свинья", "скорпион", "лиса", "леопард", "игуана", "дельфин", "летучая мышь", "цыплёнок", "краб",
                     "курица", "оса", "хамелион", "кит", "ёжик", "олень", "лось", "пчела", "змея", "сорокопут", "осёл",
                     "морская свинка", "ленивец", "конь", "пингвин", "выдра", "медведь", "зебра", "страус", "верблюд",
                     "антилопа", "лемур", "голубь", "лама", "крот", "скат", "баран", "скунс", "медуза", "овца", "акула",
                     "котёнок", "олень", "улитка", "фламинго", "кролик", "устрица", "бобр", "воробей", "голубь", "орёл",
                     "жук", "бегемот", "сова", "кобра", "саламандра", "гусь", "кенгуру", "стрекоза", "лягушка",
                     "пеликан", "кальмар", "львёнок", "ягуар", "утка", "ящерица", "носорог", "гиена", "бык", "павлин",
                     "попугай", "лось", "крокодил", "муравей", "козёл", "крольчонок", "лев", "белка", "опоссум",
                     "шимпанзе", "оленёнок", "суслик", "слон", "жираф", "паук", "щенок", "сойка", "тюлень", "петух",
                     "черепаха", "бык", "кошка", "овца", "крыса", "улитка", "бизон", "чёрный дрозд", "лебедь", "омар",
                     "собака", "комар", "змея", "цыплёнок", "муравьед"]
dp["a4a_sport"] = ["дзюдо", "плавание", "велогонка", "растяжка", "шлем", "коньки", "ходьба", "бег", "бег", "ныряние",
                   "батут", "пеший туризм", "бокс", "хоккей", "забег", "бросок", "скейт", "победа", "приседания",
                   "лыжи", "гольф", "свисток", "факел", "яхта", "стойка", "теннис", "скачок", "гребля", "бег трусцой",
                   "скакалка"]
dp["a4a_body"] = ["зуб", "щека", "косточка", "колено", "пята", "мускул", "рот", "ступня", "рука", "локоть", "волосы",
                  "ресничка", "борода", "пупок", "большой палец", "грудь", "ноздря", "нос", "поясница", "рука", "бровь",
                  "кулак", "шея", "запястье", "горло", "глаз", "нога", "спина", "ухо", "палец", "ступня", "борода",
                  "лицо", "спина", "подбородок", "ягодицы", "бедро", "живот"]
dp["a4a_people"] = ["девушка", "парень", "сын", "одноклассники", "друзья", "малыш", "ребёнок", "папа", "мама",
                    "близнецы", "братья", "мужчина", "мать", "дедушка", "семья", "женщина", "жена", "муж", "невеста",
                    "тётя", "бабушка", "влюблённые", "мальчик", "двойняшки", "дикари", "мальчик", "сёстры", "женщина",
                    "леди"]
dp["a4a_food"] = ["конфета", "сосиска", "гамбургер", "бифштекс", "помадка", "пончик", "кокос", "рис", "мороженое",
                  "желе", "йогурт", "десерт", "десерт", "крендель", "арахис", "варенье", "курица", "бекон", "специи",
                  "кофе", "пирог", "лимонад", "шоколад", "бутылка с водой", "обед", "лёд", "сахар", "соус", "суп",
                  "сок", "чипсы", "торт", "пюре", "чай", "булка", "сыр", "отбивная", "бутерброд", "ломтик", "посыпка",
                  "пицца", "мука", "жевательная резинка", "спагетти", "жаркое", "напиток", "тушёное мясо", "намазанное",
                  "мясо", "молоко", "пища", "кукуруза", "хлеб", "орех", "яйцо", "хот-дог", "ветчина"]
dp["a4a_clothes_n_accessories"] = ["украшение", "носок", "пиджак", "шпилька", "пятно", "шорты", "карман", "ожерелье",
                                   "свитер", "униформа", "плащ", "штаны", "солнечные очки", "куртка", "пулловер",
                                   ",блузка", "сандалии", "костюм", "пижама", "юбка", "молния", "туфли", "камень",
                                   "галстук", "шлёпанцы", "перчатки", "шляпа", "рукав", "кепка", "купальник",
                                   "кроссовки", "жилет", "перчатки", "шнурок", "заплатка", "шарф", "ботинок",
                                   "пуговица", "платье", "пояс", "подошва", "мантия", "трусы", "кимоно", "комбинезон"]
dp["a4a_actions"] = ["лизать", "забрасывать", "молиться", "падать", "царапать", "трогать", "нюхать", "смотреть",
                     "карабкаться", "копать", "выть", "спать", "исследовать", "рисовать", "обнимать", "учить",
                     "дремать", "лепить", "ловить", "хлопать", "плакать", "петь", "встречаться", "продавать", "клевать",
                     "ударить", "становиться на колени", "искать", "танцевать", "кашлять", "резать", "думать", "лаять",
                     "говорить", "веселить", "стряпать", "писать", "бить", "бренчать", "учиться", "пахать", "мечтать",
                     "отправлять", "нырять", "шептать", "рыдать", "трясти", "кормить", "ползти", "обосноваться",
                     "разливать", "мыть", "кричать", "рвать", "плавать", "тянуть", "поесть", "целовать", "сидеть",
                     "вылупляться", "мигать", "слушать", "целоваться", "играть", "мыть", "говорить", "вести", "пить",
                     "летать", "жонглировать", "кусать", "мести", "смотреть", "вязать", "поднимать", "держать",
                     "читать", "квакать", "оставаться", "есть"]
dp["a4a_construction"] = ["маяк", "дверь", "цирк", "церковь", "конура", "храм", "дым", "дымоход", "кирпич", "колодец",
                          "улица", "замок", "магазин", "лестница", "школа", "ферма", "мост", "плотина", "пирамида",
                          "кладовая", "мельница", "окно", "домик", "ступенька", "магазин", "сарай", "крыша",
                          "колокольня", "гараж", "мечеть", "госпиталь", "палатка", "дом", "стена", "банк", "ставень",
                          "хижина"]
dp["a4a_nature"] = ["земля", "утёс", "холм", "каньон", "камень", "море", "озеро", "пляж", "побережье", "гора", "пруд",
                    "вершина", "лава", "пещера", "дюна", "остров", "лес", "пустыня", "айсберг"]
dp["a4a_jobs"] = ["клоун", "инженер", "священник", "ветеринар", "судья", "повар", "атлет", "библиотекарь", "жонглёр",
                  "полицейский", "водопроводчик", "жетонщик", "королева", "фермер", "фокусник", "рыцарь", "доктор",
                  "каменщик", "уборщица", "учитель", "охотник", "солдат", "музыкант", "юрист", "рыбак", "принцесса",
                  "пожарник", "монахиня", "вождь", "пират", "ковбой", "электрик", "няня", "король", "президент",
                  "клерк", "плотник", "жокей", "рабочий", "механик", "пилот", "актёр", "повар", "студент", "мясник",
                  "бухгалтер", "принц", "поп", "моряк", "боксёр", "балерина", "тренер", "астронавт", "художник",
                  "анестезиолог", "учёный"]
dp["a4a_fruit_n_veg"] = ["морковь", "смородина", "сельдерей", "редька", "какао", "персик", "дыня", "грейпфрут",
                         "брокколи", "виноград", "шпинат", "инжир", "косточка", "редис", "помидор", "киви", "спаржа",
                         "оливки", "огурцы", "бобы", "клубника", "перцы", "малина", "абрикос", "картофель", "горох",
                         "капуста", "вишни", "тыква", "ежевика", "груша", "апельсин", "тыква", "авокадо", "чеснок",
                         "лук", "яблоко", "лайм", "цветная капуста", "манго", "салат", "лимон", "баклажан", "артишоки",
                         "сливы", "лук", "бананы", "папайа"]
dp["a4a_transport"] = ["яхта", "такси", "автомобиль", "велосипед", "плот", "педаль", "автобус", "руль", "лодка",
                       "пикап", "сани", "ковёр", "мотоцикл", "поезд", "корабль", "фургон", "каноэ", "ракета", "мачта",
                       "санки", "велосипед"]

dp["Welcome back."] = "Доб-ро по-жа-ловать в иг-ру."

dp['abc_flashcards_word_sequence'] = ['Автобус', 'Банка', 'Виноград', 'Гитара', 'Дом', 'Ель', 'Ёж', 'Жеребец', 'Зебра',
                                      'Иглу', 'Йога', 'Кошка', 'Лев', 'Муравей', 'Ночь', 'Обувь', 'Попугай', 'Рыба',
                                      'Слон', 'Томат', 'Утка', 'Филин', 'Хлеб', 'Цветок', 'Чайник', 'Шлюпка', 'Щука',
                                      'Съёмка', 'Мышь', 'Нить', 'Электричка', 'Юбка', 'Яхта']
dp["shape_names"] = ["Равносторонний треугольник", "Равнобедренный треугольник", "Тупоугольный треугольник",
                     "Прямоугольный треугольник", "Остроугольный треугольник", "Квадрат", "Прямоугольник",
                     "Правильная трапеция", "Равнобедренная трапеция", "Ромб", "Пара-лле-ло-грамм", "Пятиугольник",
                     "Шестиугольник", "Круг", "Эллипс"]
dp["solid_names"] = ["Куб", "Квадратная призма", "Треугольная призма", "Квадратная пирамида", "Треугольная пирамида",
                     "Сфера", "Цилиндр", "Конус", "Тор"]

dp["fruit"] = ["зе-лё-ное яб-ло-ко", "крас-ное яб-ло-ко", "клубника", "груша", "апель-син", "луковица", "томат",
               "ли-мон", "вишня", "пе--рец", "мор-ковь", "ба-нан", "ар-буз"]

# game instructions
dp[
    "Drag the slider"] = "Перетащите ползунок вверх или вниз так, чтобы правильный знак оказался в красном квадрате."  # Drag the slider up or down so that the right sign is in the red square.
# dp["Take your sheep"] = "Приве-ди-те овцу к ос-таль-но-му стаду." #Take your sheep to the rest of the herd.

dp[
    "Check the shopping list"] = "Проверьте список покупок и перетащите все необходи-мые предметы в корзину."  # Check the shopping list and drag all needed items into the basket.
dp[
    "Drag lt2"] = "Перетащите 1 из меньше, больше или ра-вно в красный квадрат."  # Drag one of the greater, lesser or equal to the red square.
dp[
    "Re-arrange right"] = "Переставьте цифры, чтобы они были в правильном порядке"  # Re-arrange the above numbers so they are in the right order
dp["Complete abc"] = "Заполните алфавит с помощью букв."  # Complete the abc using the letters above.
dp["Write a word:"] = "Напишите слово:"  # Write a word:
dp[
    "Find and separate"] = "Найдите и отделите чётные числа от нечётных чисел в указанной последовательна-сти."  # Find and separate the Even Numbers from the Odd Numbers in the above series.
dp[
    "Re-arrange alphabetical"] = "Переставьте буквы, чтобы они были в алфавитном порядке."  # Re-arrange the above letters so they are in the alphabetical order.
dp[
    "Re-arrange ascending"] = "Переставьте цифры, чтобы они были в порядке возрастания."  # Re-arrange the above numbers so they are in the ascending order.
dp[
    "Build the following word using the letters below."] = "Пост-рой-те следующее слово, используя приведён-ные ни-же буквы."
# dp["Please try again."] = "Пожалуйста, попробуйте ещё раз."#no longer used
# dp["Sorry! It is wrong."] = "Извините! Это неправильно." #no longer uses
dp["Perfect! Task solved!"] = "Великолепно! Задача решена!"
dp["work harder"] = "В следующий раз постарайтесь ра-бо-тать лучше."

# level_controller
dp["Game Over!"] = "Игра проиграна!"
dp["Congratulations! Game Completed."] = "Поздравляем! Вы выполнили все задачи в этой игре."
dp["Great job!"] = ["Отличная работа", "Велико-лепно", "Потрясающе", "Фантастическая работа",
                    "Мо-ло-дец"]  # ["Great job!","Perfect!","Awesome!","Fantastic job!","Well done!"]
dp["Perfect! Level completed!"] = "Великолепно! Уровень завершён!"

dp["Perfect!"] = "Велико-лепно"  # Perfect!

# game specific labels:
dp["area:"] = "пло-щадь:"  # area:
dp["circumference:"] = "окру--жность::"  # circumference:
dp["perimeter:"] = "периметр:"
dp["surface area:"] = "пло-щадь поверхности:"  # surface area:
dp["volume:"] = "объём"  # volume:
dp["divided by"] = "делённое на"  # divided by
dp["multiplied by"] = "умножен-ное на"
dp["equals"] = "ра-вно"  # equals
# dp["Shopping List"] = "Список поку-пок" #Shopping List
dp["Even"] = "Чётные"  # Even
dp["Odd"] = "Нечётные"  # Odd

dp["white"] = "Белый"  # "white"
dp["black"] = "Чёрный"  # "black"
dp["grey"] = "Серый"  # "grey"
dp["red"] = "Красный"  # "red"
dp["orange"] = "Оран-же-вый"  # "orange"
dp["yellow"] = "Жёлтый"  # "yellow"
dp["olive"] = "Оли-вковый"  # "olive"
dp["green"] = "Зелёный"  # "green"
dp["sea green"] = "Мор-ской вол-ны"  # "sea green"
dp["teal"] = "Сине-зелёный"  # "teal"
dp["blue"] = "Синий"  # "blue"
dp["navy"] = "Тёмно-синий"  # "navy"
dp["purple"] = "Фиолетовый"  # "purple"
# dp["violet"] = "Лиловый" #"violet"
dp["magenta"] = "Пурпурный"  # "magenta"
dp["indigo"] = "Индиго"  # "indigo"
dp["pink"] = "Ро-зо-вый"  # "pink"
dp["maroon"] = "Бордовый"  # maroon
dp["brown"] = "Коричневый"  # brown
dp["aqua"] = "Го-лу-бой"  # aqua
dp["lime"] = "Лайм"  # lime

dp["more red"] = "ещё красного"
dp["more green"] = "ещё зелёного"
dp["more blue"] = "ещё синего"
dp["more cyan"] = "ещё го-лу-бого"
dp["more magenta"] = "ещё пурпурного"
dp["more yellow"] = "ещё жёлтого"

dp["less red"] = "поменьше красного"
dp["less green"] = "поменьше зелёного"
dp["less blue"] = "поменьше синего"
dp["less cyan"] = "поменьше го-лу-бого"
dp["less magenta"] = "поменьше пурпурного"
dp["less yellow"] = "поменьше жёлтого"

dp["red is ok"] = "красного нормально"
dp["green is ok"] = "зелёного нормально"
dp["blue is ok"] = "синего нормально"
dp["cyan is ok"] = "го-лу-бого нормально"
dp["magenta is ok"] = "пурпурного нормально"
dp["yellow is ok"] = "жёлтого нормально"

dp[
    "Fract instr0"] = "Устано-вите соответствие дро-бей справа и дро-бей слева"  # Match fraction charts on the right to the ones on the left
dp[
    "Fract instr1"] = "Устано-вите соответствие дро-бей справа дро-бям слева"  # [Match fraction charts and fractions on the right","to the fraction charts on the left"]
dp[
    "Fract instr2"] = "Устано-вите соответствие дро-бей справа дро-бям слева"  # Match fraction charts to the fractions on the left
dp[
    "Fract instr3"] = "Устано-вите соответствие дро-бей и десятичных дро-бей справа их процентному представлению слева"  # ["Match fraction charts, fractions and decimal fractions on the right","to their percentage representations"]
dp[
    "Fract instr4"] = "Устано-вите соответствие отношений слева отношениям справа. Отношения показаны как отношения цвет-ных час-тей к белым час-тям"  # ["Match charts to the ratios on the left","Ratios are expressed as ratio of coloured pieces to white pieces"]
