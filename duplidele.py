import sys

def exduplidele(arg_1 = 'test sentence test sentence duplicate delete', arg_2 = 5, arg_3 = 10000):
    print('sys.argv[1] str:', arg_1) # target sentence
    print('sys.argv[2] int:', arg_2) # minimum delete characters
    print('sys.argv[3] int:', arg_3) # max target sentence

    save_ori_str = ori_str = arg_1
    delete_count_start = arg_2
    con_num = arg_3
    flag_stop = 0
    last_sentence = 'last_sentence:'
    def main(ori_str, con_num, delete_count_start, flag_stop):
        after_ori_str = ''
        original = []
        # db make
        for num, i in enumerate(ori_str):
            db = []
            db.append(num)
            db.append(i)
            original.append(db)
        for i in range(len(original)):
            target_word = original[i]
            target_place = original[i][0]
            for find_i in range(len(original)):
                if original[find_i][0] == target_place:
                    continue
                if str(original[find_i][1]) == str(original[i][1]):
                    # finding same words
                    # How about each other next word?
                    same_count = 1
                    for next_i in range(con_num):
                        try:
                            tm_str = str(original[find_i + next_i + 1][1])
                            tm_str2 = str(original[i + next_i + 1][1])
                        except:
                            dupli = ori_str[int(original[find_i][0]):int(original[find_i][0]) + next_i + 1]
                            if delete_count_start <= same_count:
                                after_ori_str = ori_str.replace(dupli, '', 1)
                                return after_ori_str, flag_stop
                            else:
                                after_ori_str = ori_str
                                break
                        if str(original[find_i + next_i + 1][1]) == str(original[i + next_i + 1][1]):
                            same_count += 1
                        else:
                            dupli = ori_str[int(original[find_i][0]):int(original[find_i][0]) + next_i + 1]
                            if delete_count_start <= same_count:
                                after_ori_str = ori_str.replace(dupli, '', 1)
                                return after_ori_str, flag_stop
                            else:
                                after_ori_str = ori_str
                                break
        # duplicate confirmation until last character
        flag_stop = 1
        # Once you find the next character and find it to the end, you're done
        return after_ori_str, flag_stop

    while(flag_stop == 0):
        ori_str, flag_stop = main(ori_str, con_num, delete_count_start, flag_stop)

    print('last_sentence:', ori_str)

if __name__ == "__main__":
    exduplidele()