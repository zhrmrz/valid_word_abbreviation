class Sol:
    def valid_word_abbreviation(self,s,st):
        num = ''
        index = -1
        list = []
        for i in range(len(s)):
            if s[i] in '123456789':
                num += str(s[i])
                if i == len(s) - 1:
                    list.append(str(num))
                    index += int(num)
                    break
                elif s[i + 1] not in '123456789':
                    list.append(str(num))
                    index += int(num)
                    num = ''
            else:
                index += 1
                if s[i] == st[index]:
                    list.append(s[i])
                else:
                    return False
        if index+1!=len(st):
            return False
        return True

if __name__ == '__main__':
    p1=Sol()
    print(p1.valid_word_abbreviation('a2e','apple'))
