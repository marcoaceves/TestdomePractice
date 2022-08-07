import cmath
from math import sqrt

# def group_by_owners(files):
#     output={}
#     for file  in files:
#         new_key=files.get(file)
#         print('file', new_key)
#         if new_key in output:
#             output[new_key].append(file)
#             print('hello')
#         else:
#             output[new_key] = [file]

#     return output

# def group_by_owners(files):
#     new_dict={}
#     books = files
#     for book in books:
#         author=books.get(book)
#         if author in new_dict:
#             new_dict[author].append(book)
#         else:
#             new_dict[author]=[book]
#     return new_dict





# files = {
#     'Input.txt': 'Randy',
#     'Code.py': 'Stan',
#     'Output.txt': 'Randy'
# }




# print(group_by_owners(files))







# Implement the IceCreamMachine's scoops method so that it returns all combinations of one ingredient and one topping. If there are no ingredients or toppings, the method should return an empty list.

# For example, IceCreamMachine(["vanilla", "chocolate"], ["chocolate sauce"]).scoops() should return [['vanilla', 'chocolate sauce'], ['chocolate', 'chocolate sauce']].





# class IceCreamMachine:

#     def __init__(self, ingredients, toppings):
#         self.ingredients = ingredients
#         self.toppings = toppings

#     def scoops(self):
        
#         scoops=[]
        
#         for i in self.ingredients:
#             for top in self.toppings:
#                 scoops.append([i, top])

#         return scoops

# machine = IceCreamMachine(["vanilla", "chocolate"], ["chocolate sauce"])
# print(machine.scoops()) #should print[['vanilla', 'chocolate sauce'], ['chocolate', 'chocolate sauce']]





# Implement the unique_names method. When passed two lists of names, it will return a list containing the names that appear in either or both lists. The returned list should have no duplicates.

# For example, calling unique_names(['Ava', 'Emma', 'Olivia'], ['Olivia', 'Sophia', 'Emma']) should return a list containing Ava, Emma, Olivia, and Sophia in any order.


# def unique_names(names1, names2):

#     new_list=[]

#     for i in names2:
#         if i not in new_list:
#             new_list.append(i)
#     for i in names1:
#         if i not in new_list:
#             new_list.append(i)
#     return new_list

# if __name__ == "__main__":
#     names1 = ["Ava", "Emma", "Olivia"]
#     names2 = ["Olivia", "Sophia", "Emma"]
#     print(unique_names(names1, names2)) # should print Ava, Emma, Olivia, Sophia




# ?Implement the function find_roots to find the roots of the quadratic equation: ax2 + bx + c = 0. The function should return a tuple containing roots in any order. If the equation has only one solution, the function should return that solution as both elements of the tuple. The equation will always have at least one solution.

# *The roots of the quadratic equation can be found with the following formula: A quadratic equation.

# ~For example, find_roots(2, 10, 8) should return (-1, -4) or (-4, -1) as the roots of the equation 2x2 + 10x + 8 = 0 are -1 and -4.


# def find_roots(a, b, c):

#     # calculate the discriminant
#     d = (b**2) - (4*a*c)

#     # find two solutions
#     sol1 = (-b-sqrt(d))/(2*a)
#     sol2 = (-b+sqrt(d))/(2*a)
#     return sol1, sol2
# print(find_roots(2, 10, 8));


def pipeline(*funcs):
    def helper(arg):
        print(arg)
        for elem in funcs:
            arg = elem(arg)
        return arg
        
    return helper
            
fun = pipeline(lambda x: x * 3, lambda x: x + 1, lambda x: x / 2)
print(fun(3)) #should print 5.0