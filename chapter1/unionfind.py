class QuickFind:
    def __init__(self, n):
        self.count_ = n
        self.id_ = range(n)

    def count(self):
        return self.count_

    def connected(self, p, q):
        return self.find(p) == self.find(q)


    def find(self, p):
        return self.id_[p]

    def union(self, p, q):
        pid = self.find(p)
        qid = self.find(q)
        if pid == qid:
            return
        i = 0
        for i in range(len(self.id_)):
            if self.id_[i] == pid:
               self.id_[i] = qid
        self.count_ -= 1

class QuickUnion:
    def __init__(self,n):
        self.count_ = n
        self.id_ = range(n)

    def count(self):
        return self.count_

    def connected(self, p, q):
        return self.find(p) == self.find(q)


    def find(self, p):
        while p != self.id_[p]:
            p = self.id_[p]
        return p
    def union(self, p, q):
        proot = self.find(p)
        qroot = self.find(q)
        if proot == qroot:
            return
        self.id_[proot] = qroot
        self.count_ -= 1


def main():
    with open('./mediumUF.txt') as f:
        uf = QuickFind(int(f.readline()))
        [uf.union(*(map(int, line.split(' ')))) for line in f.readlines() if uf.connected(*(map(int, line.split(' '))))]
        print '%d components' % uf.count()


    with open('./mediumUF.txt') as f:
        uf = QuickUnion(int(f.readline()))
        [uf.union(*(map(int, line.split(' ')))) for line in f.readlines() if uf.connected(*(map(int, line.split(' '))))]
        print '%d components' % uf.count()

if __name__ == '__main__':
    main()



    """ [1, 2, 3, 4, 5, 6, 7, 8]"""
