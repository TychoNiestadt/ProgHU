newpassword = str(input('voer je nieuwe wachtwoord in:'))
oldpassword = 'HoiHoi'
def new_password(oldPassword, newpassword):
    if newpassword != oldPassword and len(newpassword) >= 6 and any(i.isdigit() for i in newpassword):
        res = True
    else:
        res = False
    print(res)
    return res

new_password(newpassword)
