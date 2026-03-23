from preprocessing import apply_stemming

def and_query(list1, list2):
    return list(set(list1) & set(list2))


def or_query(list1, list2):
    return list(set(list1) | set(list2))


def not_query(list1, all_docs):
    return list(set(all_docs) - set(list1))

def proximity_query(pos_index, term1, term2, k):
    result = []

    if term1 not in pos_index or term2 not in pos_index:
        return result

    docs1 = pos_index[term1]
    docs2 = pos_index[term2]

    common_docs = set(docs1.keys()) & set(docs2.keys())

    for doc in common_docs:
        positions1 = docs1[doc]
        positions2 = docs2[doc]

        for p1 in positions1:
            for p2 in positions2:
                if p2-p1 <= k+1 and p2-p1 > 0:
                    result.append(doc)
                    break

    return list(set(result))

def precedence(op):
    if op == "not": return 3
    if op == "and": return 2
    if op == "or": return 1
    return 0

def infix_to_postfix(tokens):
    output = []
    stack = []
    for token in tokens:
        if token == "(":
            stack.append(token)
        elif token == ")":
            while stack and stack[-1] != "(":
                output.append(stack.pop())
            if stack:
                stack.pop()
        elif token in {"and", "or", "not"}:
            while stack and stack[-1] != "(" and precedence(stack[-1]) >= precedence(token):
                output.append(stack.pop())
            stack.append(token)
        else:
            output.append(token)
    while stack:
        output.append(stack.pop())
    return output

def evaluate_postfix(postfix, inverted_index, all_docs):
    stack = []
    for token in postfix:
        if token == "not":
            if not stack: continue
            operand = stack.pop()
            stack.append(not_query(operand, all_docs))
        elif token == "and":
            if len(stack) < 2: continue
            op2 = stack.pop()
            op1 = stack.pop()
            stack.append(and_query(op1, op2))
        elif token == "or":
            if len(stack) < 2: continue
            op2 = stack.pop()
            op1 = stack.pop()
            stack.append(or_query(op1, op2))
        else:
            stack.append(inverted_index.get(token, []))
    return stack[0] if stack else []

def process_query(query, inverted_index, positional_index, total_docs):
    all_docs = list(range(total_docs))

    if "/" in query:
        parts = query.split()
        term1 = apply_stemming(parts[0].lower())
        term2 = apply_stemming(parts[1].lower())
        k = int(parts[2].replace("/", ""))
        return proximity_query(positional_index, term1, term2, k)

    query = query.replace("(", " ( ").replace(")", " ) ")
    tokens = query.lower().split()
    
    operators = {"and", "or", "not", "(", ")"}
    tokens = [t if t in operators else apply_stemming(t) for t in tokens]

    postfix = infix_to_postfix(tokens)
    return evaluate_postfix(postfix, inverted_index, all_docs)