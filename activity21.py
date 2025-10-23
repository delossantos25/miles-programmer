kyri_bantot = True

while kyri_bantot == True:
    answer = input("\n Si kyri ay mabantot? (y / n) " ).lower()
    if answer == "y":
        print("\n maasim, apaka asim, or super asim")
        duh = input("Ano sya? " ).lower()
        if duh == "maligo":
            print("\t go mo yan ma maligo ka")
        elif duh == "apaka asim":
            print("\t bala ka te sa buhay mo magpaka asim ka")
        elif duh == "super asim":
            print("\t ayan ha wag puro lalaki, maligo din")
        continue
    if answer == "n":
        print("\n  pfffrrtt, okay po!")
        break
