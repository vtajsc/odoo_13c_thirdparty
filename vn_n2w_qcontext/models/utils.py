NUMBERS = ('không', 'một', 'hai', 'ba', 'bốn', 'năm', 'sáu', 'bảy', 'tám', 'chín', 'mười')


def _int(c):
    return ord(c) - ord('0') if c else 0


def _LT1e2(s):
    if len(s) <= 1:
        return NUMBERS[_int(s)]
    if s[0] == '1':
        ret = NUMBERS[10]
    else:
        ret = NUMBERS[_int(s[0])] + ' mươi'
    if s[1] != '0':
        ret += ' '
        if s[1] == '1' and s[0] != '1':
            ret += 'mốt'
        elif s[1] == '5':
            ret += 'lăm'
        else:
            ret += NUMBERS[_int(s[1])]
    return ret


def _LT1e3(s):
    if len(s) <= 2:
        return _LT1e2(s)
    if s == '000':
        return ''
    ret = NUMBERS[_int(s[0])] + ' trăm'
    if s[1] != '0':
        ret += ' ' + _LT1e2(s[1:])
    elif s[2] != '0':
        ret += ' lẻ ' + NUMBERS[_int(s[2])]
    return ret


def _LT1e9(s):
    if len(s) <= 3:
        return _LT1e3(s)
    if s == '000000' or s == '000000000':
        return ''
    mid = len(s) % 3 if len(s) % 3 else 3
    left, right = _LT1e3(s[:mid]), _LT1e9(s[mid:])
    hang = 'nghìn' if len(s) <= 6 else 'triệu'
    if not left:
        return right
    if not right:
        return left + ' ' + hang
    return left + ' ' + hang + ' ' + right


def n2w(num):
    num = str(num).lstrip('0').rsplit('.', 1)[0]
    if len(num) <= 9:
        return _LT1e9(num)
    mid = len(num) % 9 if len(num) % 9 else 9
    left, right = _LT1e9(num[:mid]), n2w(num[mid:])
    hang = ' '.join(['tỷ'] * ((len(num) - mid) // 9))
    if not left:
        return right
    if not right:
        return left + ' ' + hang
    return left + ' ' + hang + ', ' + right
