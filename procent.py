

class Percent:

    def start(self):
        while True:
            try:
                chisl = int (input("ваше число\n"))
                break
            except ValueError:
                print("ошибка!!!введите число")
                
                
        while True:
            try:
                procent = float(input("процент\n"))
                break
            except ValueError:
                print("ошибка!!!введите число")
                continue

        print("procents ", (chisl/100)*procent,)
