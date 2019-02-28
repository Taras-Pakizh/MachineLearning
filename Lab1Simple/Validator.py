class Validator:
    def ValidVector(self, n, x, y):
        try:
            result = ()
            if not n or not x or not y:
                return "Потрібно заповнити всі дані перед генерацією масиву"
            if ValidInt(n) and ValidInt(x) and ValidInt(y):
                result = int(n), int(x), int(y)
            else:
                return "Розмір масиву та змінні X та Y - повинні бути цілочисельними значеннями\n та обовязкові для заповнення"
            if int(y) > int(x) and int(n) > 0:
                return result
            else:
                return "Змінна Y повинен бути більша за X, а розмір масиву бути більшим нуля"
        except Exception as ex:
            return ex.__str__()

    def ValidMatrix(self, rows, cols):
        try:
            result = ()
            if ValidInt(rows) and ValidInt(cols):
                result = int(rows), int(cols)
            else:
                return "Розміри матриці повинні бути цілочисельними значеннями"
            if int(rows) > 0 and int(cols) > 0:
                return result
            else:
                return "Розміри матриці повинні бути більшими нуля"
        except Exception as ex:
            return ex.__str__()

def ValidInt(s):
    if s[0] in ('-', '+'):
        return s[1:].isdigit()
    return s.isdigit()
