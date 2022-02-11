import sys

non_working = [5,6]
def main():
    cases = int(sys.stdin.readline()[:-1])
    for case in range(cases):
        days = int(sys.stdin.readline()[:-1])
        n_parties = int(sys.stdin.readline()[:-1])
        parties = []
        for i in range(n_parties):
            parties.append(int(sys.stdin.readline()[:-1]))

        hartals = []
        for party in parties:
            aux = 0
            while (aux < days):
                aux += party

                if aux > days:
                    break

                if ((aux - 1) % 7) not in non_working and aux not in hartals:
                    hartals.append(aux)



        print(len(hartals))
    return


if __name__ == "__main__":
    main()

