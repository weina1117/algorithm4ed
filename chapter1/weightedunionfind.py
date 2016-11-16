class WeightedQuickUnionUF:
    def __init__(self,n):
        self.count_ = n # number of components
        self.id_ = range(n) #parent link(site indexed)
        self.sz_ = [1] * n #size of component for roots(site indexed)

    def count(self):
        return self.count_

    def connected(self, p, q):
        return self.find(p) == self.find(q)


    def find(self, p):
        while p != self.id_[p]:
            p = self.id_[p]
        return p

    def union(self, p, q):
        i = self.find(p)
        j = self.find(q)
        if i == j:
            return
        if self.sz_[i] < self.sz_[j]:
            self.id_[i] = j
            self.sz_[j] += self.sz_[i]
        else:
            self.id_[j] = i
            self.sz_[i] += self.sz_[j]
        self.count_ -= 1


class WeightedQuickFindUF:
    def __init__(self, n):
        self.count_ = n
        self.id_ = range(n)
        self.sz_ = [1] * n

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
                if self.sz_[pid] < self.sz_[qid]:
                    self.id_[i] = qid
                    self.sz_[qid] += self.sz_[pid]
                else:
                    self.id_[i] = pid
                    self.sz_[pid] += self.sz_[qid]
        self.count_ -= 1


def main():
    with open('./mediumUF.txt') as f:
        uf = WeightedQuickUnionUF(int(f.readline()))
        [uf.union(*(map(int, line.split(' ')))) for line in f.readlines() if uf.connected(*(map(int, line.split(' '))))]
        print '%d components' % uf.count()
    with open('./mediumUF.txt') as f:
        uf = WeightedQuickFindUF(int(f.readline()))
        [uf.union(*(map(int, line.split(' ')))) for line in f.readlines() if uf.connected(*(map(int, line.split(' '))))]
        print '%d components' % uf.count()

if __name__ == '__main__':
    main()
