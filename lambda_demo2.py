# f(m,n): 取最大值
# 請用lambda實現
# 例如: f(10,20) -> 20

def max_1(m, n):
    return m if m > n else n

if __name__ == '__main__':
    print(max_1(20,10))
    max_2 = lambda m, n: m if m > n else n
    print(max_2(10,20))