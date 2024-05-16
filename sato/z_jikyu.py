user = input("時給はいくらですか？")
jikyu = int(user)

user = input("何日働きましたか？")
nissu = int(user)

user = input("1日何時間働きましたか？")
jikan = int(user)

kyuryou = nissu * jikyu * jikan

fmt = """
時給{0}円で、{1}日間、1日{2}時間働いたので...
給料は、{3}円です。
"""
desc = fmt.format(jikyu,nissu,jikan,kyuryou)
print(desc)