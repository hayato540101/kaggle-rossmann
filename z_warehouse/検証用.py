### dict
l = ['Alice', 'Bob', 'Charlie']
d = {s: len(s) for s in l}
# print(d)
# del d['Bob']

### Class
class MyClass:
    """A simple example class"""
    i = 12345

    def f(self):
        return 'hello world'
x = MyClass()

### ndarray
a = np.arange(0,12).reshape(3,4)

### dataframe
a = pd.DataFrame(np.arange(0,12).reshape(3,4))

### Onehotvector
a = [3, 0, 8, 1, 9]
a_one_hot = np.identity(10)[a]
print(a)
print(a_one_hot)


