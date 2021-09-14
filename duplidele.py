import pdb
import sys
from janome.tokenizer import Tokenizer
import pdb
ori_str = ''
def exduplidelechar(arg_1 = 'test sentence test sentence duplicate delete', arg_2 = 5):
    save_ori_str = ori_str = arg_1
    delete_count_start = arg_2
    con_num = int(len(arg_1)) + 2
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
            # [0, 'リ']
            target_word = original[i]
            # 0
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

                                if str(original[i + next_i + 1][1]) == str(original[find_i][1]):
                                    after_ori_str = ori_str.replace(dupli, '', 1)
                                    return after_ori_str, flag_stop
                                else:
                                    after_ori_str = ori_str
                                    break
                            else:
                                after_ori_str = ori_str
                                break
                        
                        if str(original[find_i + next_i + 1][1]) == str(original[i + next_i + 1][1]):
                            same_count += 1
                        else:
                            dupli = ori_str[int(original[find_i][0]):int(original[find_i][0]) + next_i + 1]
                            if delete_count_start <= same_count:

                                # ～である　　～です。　を同一と考える特例処置
                                if (str(original[find_i + next_i + 1][1]) == 'あ' and str(original[i + next_i + 1][1]) == 'す'):
                                    if (str(original[find_i + next_i + 2][1]) == 'る' and str(original[i + next_i + 2][1]) == '。'):
                                        dupli = ori_str[int(original[find_i][0]):int(original[find_i][0]) + next_i + 1]
                                        if delete_count_start <= same_count:
                                            after_ori_str = ori_str.replace(dupli + 'ある', '', 1)
                                            print('delete:', str(dupli) + 'ある')
                                            return after_ori_str, flag_stop
                                        else:
                                            after_ori_str = ori_str
                                            break
                                # ～です。　　～である　を同一と考える特例処置
                                if (str(original[find_i + next_i + 1][1]) == 'す' and str(original[i + next_i + 1][1]) == 'あ'):
                                    if (str(original[find_i + next_i + 2][1]) == '。' and str(original[i + next_i + 2][1]) == 'る'):
                                        dupli = ori_str[int(original[find_i][0]):int(original[find_i][0]) + next_i + 1]
                                        if delete_count_start <= same_count:
                                            after_ori_str = ori_str.replace(dupli + 'ある', '', 1)
                                            print('delete:', str(dupli) + 'ある')
                                            return after_ori_str, flag_stop
                                        else:
                                            after_ori_str = ori_str
                                            break
                                
                                if str(original[i + next_i + 1][1]) == str(original[find_i][1]):
                                    after_ori_str = ori_str.replace(dupli, '', 1)
                                    return after_ori_str, flag_stop
                                else:
                                    after_ori_str = ori_str
                                    break
                            else:
                                after_ori_str = ori_str
                                break
        # duplicate confirmation until last character
        flag_stop = 1
        # Once you find the next character and find it to the end, you're done
        return after_ori_str, flag_stop

    while(flag_stop == 0):
        ori_str, flag_stop = main(ori_str, con_num, delete_count_start, flag_stop)

    print(ori_str)

def exduplidele(arg_1 = 'おはよう。元気ですか？おはよう。元気ですか？猫さん。私は元気です。', arg_2 = 6):
    save_ori_str = ori_str = arg_1
    delete_count_start = arg_2
    con_num = int(len(arg_1)) + 2
    flag_stop = 0
    last_sentence = 'last_sentence:'
    def main(ori_str, con_num, delete_count_start, flag_stop):
        after_ori_str = ''
        original = []
        # db make
        t = Tokenizer()
        ori_str_list = list(t.tokenize(ori_str, wakati=True))
        for num, i in enumerate(ori_str_list):
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
                            if delete_count_start <= same_count:
                                if str(original[i + next_i + 1][1]) == str(original[find_i][1]):
                                    if next_i == 0:
                                        del original[int(find_i)]
                                        ori_str = ''
                                        for str_i2 in range(len(original)):
                                            ori_str += original[str_i2][1]
                                        after_ori_str = ori_str
                                        if after_ori_str == save_ori_str:
                                            flag_stop = 1
                                        return after_ori_str, flag_stop
                                    else:
                                        del original[int(find_i + 1):int(find_i + next_i + 1)]
                                        ori_str = ''
                                        for str_i2 in range(len(original)):
                                            ori_str += original[str_i2][1]
                                        after_ori_str = ori_str
                                        if after_ori_str == save_ori_str:
                                            flag_stop = 1
                                        return after_ori_str, flag_stop
                                else:
                                    if after_ori_str == save_ori_str:
                                        flag_stop = 1
                                    after_ori_str = ori_str
                                    break                               
                            else:
                                if after_ori_str == save_ori_str:
                                    flag_stop = 1
                                after_ori_str = ori_str
                                break
                        if str(original[find_i + next_i + 1][1]) == str(original[i + next_i + 1][1]):
                            same_count += 1
                        else:
                            if delete_count_start <= same_count:
                                if str(original[i + next_i + 1][1]) == str(original[find_i][1]):
                                    del original[int(original[find_i][0]):int(original[find_i + next_i + 1][0])]

                                    ori_str = ''
                                    for str_i2 in range(len(original)):
                                        ori_str += original[str_i2][1]
                                    after_ori_str = ori_str
                                    return after_ori_str, flag_stop
                                else:
                                    after_ori_str = ori_str
                                    break
                            else:
                                after_ori_str = ori_str
                                break
        # duplicate confirmation until last character
        flag_stop = 1
        # Once you find the next character and find it to the end, you're done
        after_ori_str = ori_str
        return after_ori_str, flag_stop

    while(flag_stop == 0):
        ori_str, flag_stop = main(ori_str, con_num, delete_count_start, flag_stop)
    print(ori_str)

if __name__ == "__main__":
    exduplidele()
    exduplidelechar()
