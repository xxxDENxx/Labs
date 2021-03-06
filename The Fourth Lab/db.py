import ast
import string
import os
import shutil
from inspect import getsourcefile
import typing
import security


class Data:

    def __init__(self) -> None:
        name = getsourcefile(lambda: 0)
        if name is not None:
            os.chdir(os.path.dirname(os.path.abspath(name)))
        self.sec = security.Secur()
        self.alphl = list(string.ascii_letters)
        st = "0123456789-_."
        stp = "0123456789.,:;?!*+%-<{>@[]/_}$#"
        self.alphf = self.alphl.copy()
        self.alphp = self.alphl.copy()
        for let in st:
            self.alphf.append(let)
        for let in stp:
            self.alphp.append(let)
        self.er = 0
        if os.path.exists("servdata.encode"):
            with open("servdata.encode", "r", encoding="UTF-8") as sd:
                self.lap = dict(ast.literal_eval(sd.read()))
        else:
            with open("servdata.encode", "w", encoding="UTF-8") as sd:
                lap = "Logins and Passwords"
                dtdict: typing.Dict[str, typing.Dict[bytes, bytes]] = {lap: {}}
                self.lap = dtdict
                sd.write(str(dtdict))
        self.nwckey = b""

    def Creation(self, log: str, pas: str, paschek: str) -> None:
        self.er = 0
        if log[0] in self.alphl:
            pass
        else:
            print("Недопустимое начало логина")
            self.er = 1
        for let in log:
            if let in self.alphf:
                pass
            else:
                print("Недопустимые символы в логине")
                self.er = 1
                break
        if len(log) >= 6 and len(log) <= 20:
            pass
        else:
            print("Недопустимая длина логина")
            self.er = 1
        if log in self.lap["Logins and Passwords"].keys():
            print("Данный логин уже существует")
        else:
            for let in pas:
                if let in self.alphp:
                    pass
                else:
                    print("Недопустимые символы в пароле")
                    self.er = 1
                    break
            if len(pas) >= 8 and len(pas) <= 14:
                pass
            else:
                print("Недопустимая длина пароля")
                self.er = 1
            if self.er == 0:
                if paschek == pas:
                    tpas = pas.encode(encoding="UTF-8")
                    pasw = self.sec.Hashing(tpas)
                    ciphkey = self.sec.GenUSKey(tpas, "en", b"")
                    fil = "servdata.encode"
                    with open(fil, "w", encoding="UTF-8") as sd:
                        logdata = self.lap["Logins and Passwords"]
                        logdata.update({log: [pasw, ciphkey]})
                        sd.write(str(self.lap))
                    os.mkdir(log)
                    print("Вы успешно создали аккаунт")
                else:
                    print("Пароли не совпадают")
            else:
                pass

    def Enter(self, log: str, pas: str) -> bool:
        self.log = log
        tpas = pas.encode(encoding="UTF-8")
        self.pas = tpas
        pasw = self.sec.Hashing(tpas)
        with open("servdata.encode", "r", encoding="UTF-8") as sd:
            lap = dict(ast.literal_eval(sd.read()))
        spis = lap["Logins and Passwords"]
        if self.log in spis.keys() and pasw in spis[self.log]:
            return True
        else:
            return False

    def Deletion(self, pas: str) -> bool:
        tpas = pas.encode(encoding="UTF-8")
        if self.sec.Hashing(tpas) == self.sec.Hashing(self.pas):
            with open("servdata.encode", "w", encoding="UTF-8") as sd:
                logdata = self.lap["Logins and Passwords"]
                logdata.pop(self.log)
                sd.write(str(self.lap))
            shutil.rmtree(self.log)
            return True
        else:
            return False

    def Exit(self) -> None:
        self.log = ""
        self.pas = b""

    def ChCiphKey(self) -> None:
        er = 0
        with open("servdata.encode", "r", encoding="UTF-8") as sd:
            servd = dict(ast.literal_eval(sd.read()))
        ky = self.sec.GenUSKey(self.pas, "en", b"")
        self.nwckey = self.sec.GenUSKey(self.pas, "", ky)
        os.chdir(self.log)
        for fl in os.listdir(os.getcwd()):
            try:
                with open(fl, "r", encoding="UTF-8") as nt:
                    tx = dict(ast.literal_eval(nt.read()))
                tx["Ciphertext"][0]
            except SyntaxError:
                print(f"{fl} не был создан в этой программе")
                er = 1
            except IndexError:
                er = 1
            if er == 0:
                with open(fl, "w", encoding="UTF-8") as nt:
                    a = tx["Ciphertext"]
                    b = servd["Logins and Passwords"][self.log][1]
                    bk = self.sec.GenUSKey(self.pas, "", b)
                    dtext = self.sec.Decrypt(a, bk)
                    d = self.sec.Encrypt(dtext, self.nwckey)
                    tx.update({"Ciphertext": d})
                    nt.write(str(tx))
            else:
                pass
        os.chdir("..")
        with open("servdata.encode", "w", encoding="UTF-8") as sd:
            logdata = self.lap["Logins and Passwords"]
            logdata[self.log][1] = ky
            sd.write(str(self.lap))
