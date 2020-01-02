mol_mass = {'H':1, 'C':12, 'O':16}
digits = '23456789'
formula = input()
stack = []
for i in range(len(formula)):
    if formula[i] == ')':
        bracket_mass = 0
        while stack[-1] != '(':
            bracket_mass += stack.pop()
        stack.pop()
        stack.append(bracket_mass)
    elif formula[i] in mol_mass:
        stack.append(mol_mass[formula[i]])
    elif formula[i] == '(':
        stack.append('(')
    elif formula[i] in digits:
        stack[-1] *= int(formula[i])
print(sum(stack))
