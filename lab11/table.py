def table(tup1_1, tup2_1, tup3_1, tup1_2, tup2_2, tup3_2, tup1_3, tup2_3, tup3_3, n1, n2, n3):
    print("-" * 117)
    print("|" + " " * 22 + "|" + " " * 30 + "|"  + " " * 30 + "|"  + " " * 30 + "|")
    print("-" * 117)
    print(f"|                      | {n1:^28} | {n2:^28} | {n3:^28} |")
    print("-" * 117)
    print("|" + " " * 22 + "|" + "  время в нс " + "|" + "  перестановки  " + "|" + "  время в нс " + "|" + "  перестановки  " + "|" + "  время в нс " + "|" + "  перестановки  " + "|")
    print("-" * 117)
    print(f"| Упорядоченный список | {tup1_2[0]:^11} | {tup1_2[1]:^14} | {tup2_2[0]:^11} | {tup2_2[1]:^14} | {tup3_2[0]:^11} | {tup3_2[1]:^14} |")
    print("-" * 117)
    print(f"|   Случайный список   | {tup1_1[0]:^11} | {tup1_1[1]:^14} | {tup2_1[0]:^11} | {tup2_1[1]:^14} | {tup3_1[0]:^11} | {tup3_1[1]:^14} |")
    print("-" * 117)
    print(f"|  Упорядоченный в об- | {tup1_3[0]:^11} | {tup1_3[1]:^14} | {tup2_3[0]:^11} | {tup2_3[1]:^14} | {tup3_3[0]:^11} | {tup3_3[1]:^14} |")
    print(f"|    ратном порядке    |             |                |             |                |             |                |")
    print("-" * 117)