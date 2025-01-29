class Polynomial:

    def __init__(self, name, coefficients):
        self.name = name
        self.coefficients = coefficients #list instance variable
        self.order_number = self.calculate_order_no()

    
    """
    function to calculate the order of the polynomial
    ie number of values or entries in list minus constant term
    """
    def calculate_order_no(self):
        order_no = len(self.coefficients) - 1
        return f"Order number of {self.name} = {order_no} "

    """
    function to print polynomial as string (excluding 0 terms)
    for each term in coefficients, convert to string and append with 
    each term suffixed with its corresponding variable
    if list value or coefficient value equals 0, do not add
    """
    def display_formatted_polynomial(self):

        formatted_polynomial = f"{self.name} = "

        for index, value in enumerate(self.coefficients):
            value = round(value, 1)
            if value == 0:
                continue
            elif index == 0:
                formatted_polynomial += str(value) + " + "
            #if index number equals length, add value and index but not "+"
            elif index != len(self.coefficients) - 1:
                formatted_polynomial += str(value) + f"x^{index} + "
            else:
                formatted_polynomial += str(value) + f"x^{index}"

        return formatted_polynomial
    
    # compare two numbers and return highest
    #def max_value(self, a, b):
    #    if a == b :
    #        return a
    #    elif a > b :
    #        return a
    #    else :
    #        return b
        
    """
    add polynomials together
        if first list length equals other list length then no adjustments are 
        needed if they are unequal then add zeros until they are the same 
        length
    """
    def add_polynomials(self, other):
        #length_self = len(self.coefficients)
        #length_other = len(other.coefficients) 
        #max_list_length = self.max_value(length_self, length_other)
        
        max_list_length = max(len(self.coefficients), len(other.coefficients))

        self.coefficients.extend(
            [0] * (max_list_length - len(self.coefficients))
            )
        other.coefficients.extend(
            [0] * (max_list_length - len(other.coefficients))
            )

        new_coefficients = [
            self.coefficients[i] + other.coefficients[i]
            for i in range(max_list_length)
            ]
        new_polynomial_object = Polynomial(
            f"{self.name} + {other.name}", new_coefficients
            )

        return new_polynomial_object.display_formatted_polynomial()
    
    """
    derivative function
        # for each term in coefficients, if index equals zero then continue,
        # multiply index with value and append to first derivative list
    """
    def first_derivative(self):
        first_derivative = []
        for index, value in enumerate(self.coefficients):
            if index == 0:
                continue
            else:
                first_derivative.append(index * value)

        first_derivative_object = Polynomial(
            f"First derivative of {self.name}", first_derivative
            )

        return first_derivative_object.display_formatted_polynomial()
    
    """
    integrate function
        for each term in coefficients, if value is zero then append zero
        else divide coefficient by index plus 1
    """
    def first_integral(self):
        first_integral = [2]
        for index, value in enumerate(self.coefficients):
            if value == 0:
                first_integral.append(0)
            else:
                first_integral.append(value / (index + 1))

        first_integral_object = Polynomial(
            f"First integral of {self.name}", first_integral
            )

        return first_integral_object.display_formatted_polynomial()

a = [1, 2, 0, 3, 4]
b = [1, 1, 1, 1, 1, 1, 1]
c = [1.0, 2.0, 3.0]
P_ax = [2, 0, 4, -1, 0, 6]
P_bx = [-1, -3, 0, 4.5]

test_a = Polynomial("Poly Test a", a)
test_b = Polynomial("Poly Test b", b)
test_c = Polynomial("Poly Test c", c)

poly_a = Polynomial("P_a(x)", P_ax)
poly_b = Polynomial("P_b(x)", P_bx)

#print(test_a.display_formatted_polynomial())
#print(test_b.display_formatted_polynomial())
#print(test_c.display_formatted_polynomial())

print(poly_a.display_formatted_polynomial())
print(poly_a.calculate_order_no())
print(poly_b.display_formatted_polynomial())

#print(testP.add_polynomials(poly_a))
#print(test_a.add_polynomials(test_b))
print(poly_a.add_polynomials(poly_b))

#print(test_a.first_derivative())
#print(test_b.first_derivative())
#print(test_c.first_derivative())
#print(test_c.first_integral())

print(poly_a.first_derivative())
print(poly_a.first_integral())