class HashTable:
    def __init__(self,num_buckets):
        self.num_buckets = num_buckets
        self.buckets = [[] for i in range(num_buckets)]
    def hash(self,string):
        alphabet = 'abcdefghijklmnopqrstuvwxyz'
        string_lower = string.lower()
        tot = 0
        for lttr in string_lower:
            tot += alphabet.find(lttr)
        tot %= self.num_buckets
        return tot
    
    def insert(self,key,value):
        hash = self.hash(key)
        self.buckets[hash].append((key,value))

    def find(self,key):
        hash = self.hash(key)
        for i in self.buckets[hash]:
            if i[0] == key:
                return i[1]
    
ht = HashTable(3)
if ht.buckets != [[] for i in range(3)]:
    print('buckets failed at 3')
    print('should be ', [[] for i in range(3)])
    print('is ',ht.buckets)
if ht.hash('cabbage') != 2:
    print('failed at hash')
    print('should be 2')
    print('is ',ht.hash('cabbage'))
ht.insert('cabbage',5)
ht.insert('cab',20)
ht.insert('c',17)
ht.insert('ac',21)
if ht.buckets != [[('cab', 20)], [], [('cabbage',5),('c',17),('ac',21)]]:
    print('failed')
    print("wanted [[('cab', 20)], [], [('cabbage',5),('c',17),('ac',21)]]")
    print('got ',ht.buckets)

if ht.find('cabbage') != 5:
    print('failed')
    print('wanted 5')
    print('got ',ht.find('cabbage'))


if ht.find('cab') != 20:
    print('failed')
    print('wanted 20')
    print('got ',ht.find('cab'))


if ht.find('c') != 17:
    print('failed')
    print('wanted 17')
    print('got ',ht.find('c'))


if ht.find('ac') != 21:
    print('failed')
    print('wanted 21')
    print('got ',ht.find('ac'))

print('done')
