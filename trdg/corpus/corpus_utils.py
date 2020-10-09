import string, os, random


def get_list_file_in_folder(dir, ext=['png']):
    included_extensions = ext
    file_names = [fn for fn in os.listdir(dir)
                  if any(fn.endswith(ext) for ext in included_extensions)]
    return file_names


def get_list_dir_in_folder(dir):
    sub_dir = [o for o in os.listdir(dir) if os.path.isdir(os.path.join(dir, o))]
    return sub_dir


def get_single_word_from_composed_word(corpus_path):
    # gen single word from tu ghep
    all_text = open(corpus_path, 'r')
    final_list = []
    count = 0
    for line in all_text.readlines():
        sub_str = (line.replace('\n', '')).split(' ')
        for str in sub_str:
            if str not in final_list:
                count += 1
                print(count, ':', str)
                final_list.append(str)
    final_text = ''
    for line in final_list:
        final_text += line + '\n'

    # list_text = [line.split(' ') for line in all_text.readlines()]
    with open("data/corpus/Viet22k_single.txt", "w") as save_file:
        save_file.write(final_text)
    print("Done")


def gen_random_serial_corpus(num_to_gen=1000, max_length=15):  # generate serial
    print("gen_random_serial_corpus", num_to_gen, max_length)
    final_text = ''
    for i in range(num_to_gen):
        length_of_word = random.randint(2, max_length)
        lower = random.choice([True, False])
        if lower:
            line = ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(length_of_word))
        else:
            line = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(length_of_word))
        final_text += line + '\n'

    with open("random_serial_" + str(num_to_gen) + ".txt", "w") as save_file:
        save_file.write(final_text)
    print("Done")


def gen_random_number_corpus(num_to_gen=1000, max_length=14):  # generate number with/without dot or comma
    print("gen_number_corpus", num_to_gen, max_length)
    final_text = ''
    for i in range(num_to_gen):
        length_of_word = random.randint(1, max_length)
        line = ''.join(random.choice(string.digits)) + ''.join(random.choice('.,0123456789.,')) + ''.join(
            random.choice(string.digits) for _ in range(length_of_word))
        final_text += line + '\n'

    with open("random_number_" + str(num_to_gen) + ".txt", "w") as save_file:
        save_file.write(final_text)


def gen_random_symbol_corpus(num_to_gen=300, max_length=4):  # generate symbol
    print("gen_number_corpus", num_to_gen, max_length)
    symbol_char = '*:,@$.-(#%\'\")/~!^&_+={}[]\;<>?”'
    symbol_char_list = [x for x in symbol_char]
    final_text = ''
    for i in range(num_to_gen):
        length_of_word = random.randint(1, max_length)
        line = ''.join(random.choice(symbol_char_list) for _ in range(length_of_word))
        final_text += line + '\n'

    with open("random_symbol_" + str(num_to_gen) + ".txt", "w") as save_file:
        save_file.write(final_text)


def gen_final_corpus(corpus_dir=''):
    print('corpus_utils.gen_final_corpus')
    file_list = [
        #'#English10k.txt'
        'English10k_triple.txt',
        'Viet_1474_no_accent_triple.txt',
        'Viet_5944_single_triple.txt',
        'random_number_5000.txt',
        'random_serial_5000.txt',
        'random_symbol_1000.txt'
    ]
    final_corpus = []
    for file in file_list:
        gen_triple = False
        if 'number' in file or 'symbol' in file:
            gen_triple = False
        all_text = open(os.path.join(corpus_dir, file), 'r', encoding='utf-8')
        for line in all_text.readlines():
            sub_str = line.replace('\n', '')
            final_corpus.append(sub_str.lower())
            if gen_triple:  # generate uppercase and word with 1st uppercase
                str_upper = sub_str.upper()
                final_corpus.append(str_upper)
                first_char = sub_str[0]
                first_char_upper = first_char.upper()
                str_first_char_upper = first_char_upper + sub_str[1:]
                final_corpus.append(str_first_char_upper)

    final_str = ''
    count = 0
    random.shuffle(final_corpus)
    for corpus in final_corpus:
        count += 1
        print(count, corpus)
        final_str += corpus + '\n'

    save_filename = os.path.join(corpus_dir, 'Viet_Eng_corpus_2408.txt')
    print('Save corpus:', save_filename)
    with open(save_filename, "w", encoding='utf-8') as save_file:
        save_file.write(final_str)
    return save_filename


def get_corpus(corpus_file, percentage=1.0, shuffle=True):
    all_text = open(corpus_file, 'r', encoding='utf-8')
    file_lines = all_text.readlines()
    num_lines = len(file_lines)
    num_lines_to_use = int(num_lines * percentage)

    total_lines = []
    num_repeat = int(percentage) + 1
    for i in range(num_repeat):
        total_lines.extend(file_lines)
    if shuffle:
        random.shuffle(total_lines)

    final_lines = total_lines[0:num_lines_to_use - 1]
    final_txt = []
    for line in final_lines:
        sub_str = line.replace('\n', '')
        final_txt.append(sub_str)
    return final_txt


def gen_final_corpus2(corpus_dir=''):
    print('corpus_utils.gen_final_corpus')
    file_list = [
        ('Công nghệ_words.txt', 0.2),
        ('Đời sống_words.txt', 0.2),
        ('Giải trí_words.txt', 0.2),
        ('Giáo dục_words.txt', 0.2),
        ('Khoa học_words.txt', 0.2),
        ('Kinh tế_words.txt', 0.2),
        ('Nhà đất_words.txt', 0.2),
        ('None_words.txt', 0.2),
        ('Pháp luật_words.txt', 0.2),
        ('Thế giới_words.txt', 0.2),
        ('Thể thao_words.txt', 0.2),
        ('Văn hóa_words.txt', 0.2),
        ('Xã hội_words.txt', 0.2),
        ('Xe cộ_words.txt', 0.2)
    ]
    final_corpus = []
    for file in file_list:
        print(file)
        file_corpus = get_corpus(os.path.join(corpus_dir, file[0]), percentage=file[1])
        final_corpus.extend(file_corpus)

    final_str = ''
    count = 0
    random.shuffle(final_corpus)
    for corpus in final_corpus:
        count += 1
        print(count, corpus)
        final_str += corpus + '\n'

    save_filename = os.path.join(corpus_dir, 'final_corpus_general_words_vnmese_15Sep.txt')
    print('Save corpus:', save_filename)
    with open(save_filename, "w", encoding='utf-8') as save_file:
        save_file.write(final_str)
    return save_filename


def get_corpus_list_from_icdar_dataset(data_dir, corpus_dir=''):  # only word, no space
    list_file = get_list_file_in_folder(data_dir, '.txt')

    corpus_list = []
    count = 0
    for i in range(len(list_file)):
        anno_path = os.path.join(data_dir, list_file[i])
        print("anno file:", list_file[i])

        with open(anno_path, "r", encoding='utf-8') as f:
            anno_list = f.readlines()
        anno_list = [x.strip() for x in anno_list]

        for index, anno in enumerate(anno_list):
            pts = anno.split(',')
            left = int(pts[0])
            top = int(pts[1])
            right = int(pts[2])
            bottom = int(pts[5])
            loc = -1
            for i in range(0, 8):
                loc = anno.find(',', loc + 1)
            val = anno[loc + 1:]

            if val not in corpus_list:
                corpus_list.append(val)

    final_str = ''
    count = 0
    random.shuffle(corpus_list)
    for corpus in corpus_list:
        count += 1
        print(count, corpus)
        final_str += corpus + '\n'

    save_filename = os.path.join(corpus_dir, 'Korea_english_corpus.txt')
    print('Save corpus:', save_filename)
    with open(save_filename, "w", encoding='utf-8') as save_file:
        save_file.write(final_str)


def get_text_from_annotation(data_dir):
    list_dir = get_list_dir_in_folder(data_dir)
    corpus_list = []
    for dir in list_dir:
        list_file = get_list_file_in_folder(os.path.join(data_dir, dir), '.txt')
        for file in list_file:
            anno_path = os.path.join(data_dir, dir, file)
            with open(anno_path, "r", encoding='utf-8') as f:
                anno_list = f.readlines()
            anno_txt = anno_list[0].replace(' \n', '').replace('\n', '')
            corpus_list.append(anno_txt)

    final_str = ''
    count = 0
    random.shuffle(corpus_list)
    for corpus in corpus_list:
        count += 1
        print(count, corpus)
        final_str += corpus + '\n'

    save_filename = os.path.join(data_dir, 'handwriting_corpus.txt')
    print('Save corpus:', save_filename)
    with open(save_filename, "w", encoding='utf-8') as save_file:
        save_file.write(final_str)


class InvoiceCorpus():  # nt.anh
    def gen_random_date(self, num_to_gen=1000):
        print("gen_random_date", num_to_gen)
        numb_date = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        final_text = ''
        for i in range(num_to_gen):
            year = random.randrange(1980, 2100)
            month = random.randrange(1, 12)
            date = random.randrange(1, numb_date[month - 1])
            date_str_list = ['Ngày:',
                             'Ngày',
                             'Ngày (day):',
                             'Ngày (date):',
                             'Ngày/date:']
            month_str_list = ['tháng:',
                              'tháng',
                              'tháng (month):']
            year_str_list = ['năm:',
                             'năm',
                             'năm (year):']
            date_str = random.choice(date_str_list)
            month_str = random.choice(month_str_list)
            year_str = random.choice(year_str_list)
            space = ''
            for i in range(random.randint(0, 2)):
                space += ' '

            date_value = random.choice([str(date).zfill(2), str(date)])
            month_value = random.choice([str(month).zfill(2), str(month)])
            year_value = str(year)

            str_date = ' '.join(
                [date_str, space, date_value, month_str, space, month_value, year_str, space, year_value])
            final_text += str_date + '\n'
        # print(final_text)
        path_file = os.path.join("random_invoice_date_" + str(num_to_gen) + ".txt")
        with open(path_file, "w") as save_file:
            save_file.write(final_text)
        print("Done")

    def gen_random_form(self, num_to_gen=1000):  # generate form
        print("gen_random_form", num_to_gen)
        prefix = ['Mẫu số:',
                  'Mẫu số (Form):',
                  'Mẫu số (Form No.):',
                  'Mẫu số (Template No):',
                  '',
                  '',
                  '',
                  '',
                  '']
        nameForm = ['02GTTT', '01GTKT', '07KPTQ', '03XKNB', '04HGDL']

        final_text = ''
        for i in range(num_to_gen):
            Cap = random.randrange(1, 100)
            key_only = random.randrange(1, 5)
            pre = random.choice(prefix)
            form = random.choice(nameForm)
            form += str(random.randint(1, 5))
            form += '/'
            form += '%03d' % (random.choice([random.randint(1, 10), random.randint(10, 1000)]))
            space = ''
            if pre != '':  # cuongnd
                for i in range(random.randint(1, 4)):
                    space += ' '
            if Cap == 1:  # 1%
                pre = pre.upper()
            if key_only == 1 and pre != '':  # 20%
                line = pre
            else:
                line = pre + space + form

            final_text += line + '\n'
        # print(final_text)
        path_file = os.path.join("random_invoice_form_" + str(num_to_gen) + ".txt")
        with open(path_file, "w") as save_file:
            save_file.write(final_text)
        print("Done")

    def gen_random_serial(self, num_to_gen=1000):  # generate serial
        print("gen_random_serial", num_to_gen)
        prefix = ['Ký hiệu:',
                  'Ký hiệu (Serial):',
                  'Ký hiệu (Sign):',
                  'Ký hiệu (Serial No.):',
                  'Ký hiệu/ Series No:',
                  'Ký hiệu / Serial',
                  'Ký hiệu (Series):',
                  '',
                  '',
                  '',
                  '',
                  '']
        final_text = ''
        for i in range(num_to_gen):
            Cap = random.randrange(1, 100)
            key_only = random.randrange(1, 5)
            pre = random.choice(prefix)
            serial = list(random.choice(string.ascii_uppercase) for _ in range(2))
            serial.append('/')
            serial += '%02d' % (random.randint(0, 30))
            serial += random.choice('EPT')
            space = ''
            if pre != '':  # cuongnd
                for i in range(random.randint(1, 4)):
                    space += ' '

            if Cap == 1:  # 1%
                pre = pre.upper()
            if key_only == 1 and pre != '':  # 20%
                line = pre
            else:
                line = pre + space + ''.join(serial)

            final_text += line + '\n'
        # print(final_text)
        with open("random_invoice_serial_" + str(num_to_gen) + ".txt", "w") as save_file:
            save_file.write(final_text)
        print("Done")

    def gen_random_taxcode(self, num_to_gen=1000):  # generate taxcode
        print("gen_random_taxcode", num_to_gen)
        prefix = ['Mã số thuế:',
                  'Mã số thuế (Tax code):',
                  'Mã số thuế (VAT code):',
                  'MST:',
                  'MST (Tax Code):',
                  '',
                  '',
                  '',
                  '',
                  '',
                  '',
                  '',
                  '',
                  '']
        final_text = ''
        for i in range(num_to_gen):
            Cap = random.randrange(1, 100)
            key_only = random.randrange(1, 5)
            pre = random.choice(prefix)
            taxcode_length1 = random.randint(6, 10)
            taxcode_length2 = random.randint(3, 4)
            taxcode1 = list(random.choice(string.digits) for _ in range(taxcode_length1))
            taxcode2 = list(random.choice(string.digits) for _ in range(taxcode_length2))
            space = ''
            if pre != '':  # cuongnd
                for i in range(random.randint(1, 4)):
                    space += ' '

            if Cap == 1:  # 1%
                pre = pre.upper()
            if key_only == 1 and pre != '':  # 20%
                line = pre
            else:
                line = pre + space + ''.join(taxcode1) + random.choice(['', '-']) + ''.join(taxcode2)
            final_text += line + '\n'
        # print(final_text)
        with open("random_invoice_taxcode_" + str(num_to_gen) + ".txt", "w") as save_file:
            save_file.write(final_text)
        print("Done")


class SEVT_corpus:
    #form 1
    def gen_rand_serial(self, length=2, number_pecent=0.9, include_lowercase=False):
        result = ''
        for i in range(length):
            rand = random.randrange(1, 100)
            if rand < int(100 * number_pecent):
                result += random.choice(string.digits)
            else:
                if include_lowercase:
                    result += random.choice(string.ascii_uppercase+string.ascii_lowercase)
                else:
                    result += random.choice(string.ascii_uppercase)
        return result

    def gen_code(self, num_to_gen=1000):
        final_text = ''
        for i in range(num_to_gen):
            first_part = self.gen_rand_serial(2, 0.9)
            second_part = list(random.choice(string.digits) for _ in range(2))
            third_part = self.gen_rand_serial(7, 0.95)
            code = first_part + ''.join(second_part) + '-' + third_part
            final_text += code + '\n'
            print(code)
            with open("random_sevt_code_" + str(num_to_gen) + ".txt", "w") as save_file:
                save_file.write(final_text)

    def gen_footer(self, num_to_gen=1000):
        final_text = ''
        for i in range(num_to_gen):
            first_part = str(random.randrange(1, 100)).zfill(3)
            second_part = self.gen_rand_serial(5, 0.8)
            third_part = self.gen_rand_serial(4, 0.7)
            code = 'SMD_' + first_part + ' <' + second_part + '/' + third_part + '>'
            final_text += code + '\n'
            print(code)
            with open("random_sevt_footer_" + str(num_to_gen) + ".txt", "w") as save_file:
                save_file.write(final_text)

    def gen_no(self, num_to_gen=999):
        final_text = ''
        for i in range(num_to_gen):
            final_text += str(i) + '\n'
            with open("random_sevt_no_" + str(num_to_gen) + ".txt", "w") as save_file:
                save_file.write(final_text)

    #unplan
    def gen_random_date(self, num_to_gen=1000):
        print("gen_random_date", num_to_gen)
        numb_date = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        final_text = ''
        for i in range(num_to_gen):
            year = random.randrange(2000, 2100)
            month = random.randrange(1, 12)
            date = random.randrange(1, numb_date[month - 1])
            connect_list = ['/','-','\\','.']
            connect = random.choice(connect_list)

            len_date=random.choices([1,1,1,2,2,3])[0]
            begin_date=max(1,date+1-len_date)
            end_date=begin_date+len_date-1
            date_value=''
            for i in range(begin_date,end_date+1):
                date_value += random.choice([str(i).zfill(2), str(i)])+'+'
            date_value=date_value.rstrip('+')


            month_value = random.choice([str(month).zfill(2), str(month)])
            year_value = str(year)
            include_year=random.choices([True,False])[0]
            if include_year:
                str_date = connect.join([date_value, month_value, year_value])
            else:
                str_date = connect.join([date_value, month_value])

            final_text += str_date + '\n'
        # print(final_text)
        path_file = os.path.join("random_sevt_date_" + str(num_to_gen) + ".txt")
        with open(path_file, "w") as save_file:
            save_file.write(final_text)
        print("Done")

    def gen_model(self, num_to_gen=1000):
        final_text = ''
        for i in range(num_to_gen):
            len_first_part=random.randrange(3,8)
            first_part = self.gen_rand_serial(len_first_part, 0.6, include_lowercase=True)

            connect= random.choices(['/','_'])[0]

            len_second_part = random.randrange(2, 6)
            second_candidates = self.gen_rand_serial(len_second_part, 0.6, include_lowercase=True)
            second_part=random.choices([second_candidates,
                                        second_candidates,
                                              'master',
                                              'MASTER',
                                              'slave',
                                              'SLAVE',
                                        ])[0]
            include_second_part=random.choices([True,False])[0]
            if include_second_part:
                model = first_part + connect + second_part
            else:
                model = first_part
            final_text += model + '\n'
            print(model)
            with open("random_sevt_model_" + str(num_to_gen) + ".txt", "w") as save_file:
                save_file.write(final_text)

    def gen_LKDT_LKDB(self, num_to_gen=1000):
        final_text = ''
        for i in range(num_to_gen):
            first_part = self.gen_rand_serial(2, 0.9)
            second_part = list(random.choice(string.digits) for _ in range(2))
            third_part = self.gen_rand_serial(7, 0.95)
            code = first_part + ''.join(second_part) + '-' + third_part
            final_code=random.choices([code,
                                        code,
                                        code,
                                        code,
                                        code,
                                        code,
                                        code,
                                        code,
                                        code,
                                        code,
                                        code,
                                        code,
                                        code,
                                              'PCB trắng',
                                              'Board 1 mặt',
                                              'Board 2 mặt'
                                        ])[0]
            final_text += final_code + '\n'
            print(code)
            with open("random_sevt_LKDT_LKDB_" + str(num_to_gen) + ".txt", "w") as save_file:
                save_file.write(final_text)

    def gen_id(self, num_to_gen=999):
        final_text = ''
        for i in range(num_to_gen):

            len=random.randrange(6,8)
            id=''
            for j in range(len):
                id+=random.choice(string.digits)
            final_text += id + '\n'
            with open("random_sevt_id_" + str(num_to_gen) + ".txt", "w") as save_file:
                save_file.write(final_text)

def split_word(line):
    line = line.rstrip('\n')
    words = line.split(' ')
    curr = 0
    separate = []
    while (curr < len(words)):
        prob = random.randrange(1, 11)
        if prob <= 6:  # len 1
            val = 1
        elif prob <= 9:  # len 2
            val = 2
        else:  # len 3
            val = 3
        if (curr + val > len(words)):
            val = len(words) - curr
        separate.append(val)
        curr += val
    #print(sum(separate), len(words))
    final_list = []
    start_idx = 0
    for l in separate:
        end_idx = start_idx + l
        sub_str_list = words[start_idx:end_idx]
        start_idx = end_idx
        word = ' '.join(sub_str_list)
        final_list.append(word)

    return final_list

def shorten_corpus(corpus_dir, corpus_shorten_dir, short_size=100000):
    print('shorten_corpus.',corpus_dir)
    list_file = get_list_file_in_folder(corpus_dir, '.txt')
    for file in list_file:
        print(file)
        anno_path = os.path.join(corpus_dir, file)
        with open(anno_path, "r", encoding='utf-8') as f:
            anno_list = f.readlines()
        random.shuffle(anno_list)
        anno_list_short = anno_list[0: min(short_size,len(anno_list))]
        saved_txt = ''.join(anno_list_short)
        saved_txt = saved_txt.rstrip('\n')
        with open(os.path.join(corpus_shorten_dir, file), "w", encoding='utf-8') as save_file:
            save_file.write(saved_txt)

def filter_words_from_corpus(corpus_dir, probs=[6,3,1]):
    list_file = get_list_file_in_folder(corpus_dir, '.txt')
    for file in list_file:
        print(file)
        final_words=[]
        anno_path = os.path.join(corpus_dir, file)
        with open(anno_path, "r", encoding='utf-8') as f:
            anno_list = f.readlines()
        for txt in anno_list:
            res= split_word(txt)
            final_words.extend(res)
        final_text = '\n'.join(final_words)
        print('filter_words_from_corpus. len of final words list',len(final_words))

        with open(anno_path.replace('.txt', '_words.txt'), "w", encoding='utf-8') as save_file:
            save_file.write(final_text)


if __name__ == "__main__":
    corpus_dir = '/home/duycuong/PycharmProjects/dataset/news-corpus-categorys-20181217/corpus'
    corpus_shorten_dir = '/home/duycuong/PycharmProjects/dataset/news-corpus-categorys-20181217/corpus_short'
    #shorten_corpus(corpus_dir,corpus_shorten_dir)
    #filter_words_from_corpus(corpus_shorten_dir)
    gen_final_corpus2(corpus_dir='/home/duycuong/PycharmProjects/dataset/news-corpus-categorys-20181217/corpus_short_words')
    #gen = SEVT_corpus()
    #gen.gen_no(num_to_gen=999)
    #gen.gen_random_date(num_to_gen=3000)
    #gen.gen_model(num_to_gen=1000)
    #gen.gen_LKDT_LKDB(num_to_gen=10000)
    #gen.gen_id(num_to_gen=1000)
    #get_corpus_list_from_icdar_dataset('/data20.04/data/aicr/korea_test_set/korea_English_test/GT_word_icdar')
