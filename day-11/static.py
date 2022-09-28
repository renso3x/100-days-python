class Method:
    # static method doesn't modify anything from it's attribute
    @staticmethod
    def add_five(x):
        return x + 5


print(Method.add_five(5))