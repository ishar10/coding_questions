class LRUCache:

    def __init__(self, capacity: int):
        self.l = [{}, capacity, []]
        return None
        

    def get(self, key: int) -> int:
        print("hashmap",self.l[0])
        if key in self.l[0]:
            one = []
            while(self.l[2]!= []):
                ele = self.l[2].pop(-1)
                one.append(ele)
                if ele== key:
                    break
            print("get initial",self.l[2])
            print(one)
            self.l[2] = self.l[2] + one
            print("get final",self.l[2])
            return self.l[0][key]

        else:
            return -1
        

    def put(self, key: int, value: int) -> None:
        c = self.l[1]
        if c > len(self.l[0]):
            if key in self.l[0]:
                one = []
                while(self.l[2]!= []):
                    ele = self.l[2].pop(-1)
                    one.append(ele)
                    if ele== key:
                        break
                self.l[2] = self.l[2] + one[::-1]
            else:
                self.l[2].append(key)
            
            self.l[0][key] = value
        elif c == len(self.l[0]):
            if key in self.l[0]:
                one = []
                while(self.l[2]!= []):
                    ele = self.l[2].pop(-1)
                    one.append(ele)
                    if ele== key:
                        break
                self.l[2] = self.l[2] + one[::-1]
                self.l[0][key] = value
            else:
                # print("list",self.l[2])
                delete_key = self.l[2].pop(0)
                del self.l[0][delete_key]
                self.l[2].append(key)
                self.l[0][key] = value

func = ["LRUCache","put","put","put","put","get","get","get","get","put","get","get","get","get","get"]
value = [[3],[1,1],[2,2],[3,3],[4,4],[4],[3],[2],[1],[5,5],[1],[2],[3],[4],[5]]

for i in range(len(func)):
    if func[i] == "LRUCache":
        obj = LRUCache(value[i][0])
        print("none")
    elif func[i] == "put":
        obj.put(value[i][0],value[i][1])
        print("none")
    else:
        param_1 = obj.get(value[i][0])
        print(value[i][0],param_1)