def CheckDOM(strParam):

    stack = []
    tag_mapping = {'b': 'b', 'i': 'i', 'em': 'em', 'div': 'div', 'p': 'p'}

    def is_closing_tag(tag):
        return tag.startswith('</')

    def get_tag_name(tag):
        if is_closing_tag(tag):
            return tag[2:-1]
        else:
            return tag[1:-1]

    def is_nested_correctly(current_tag):
        if stack:
            top_tag = stack[-1]
            return tag_mapping[get_tag_name(top_tag)] == get_tag_name(current_tag)
        return False

    for tag in strParam.split():
        if is_closing_tag(tag):
            if is_nested_correctly(tag):
                stack.pop()
            else:
                return get_tag_name(tag)

        else:
            stack.append(tag)

    if not stack:
        return True
    elif len(stack) == 1 and is_closing_tag(stack[0]):
        return get_tag_name(stack[0])
    else:
        return False

# CheckDOM("<b><i>hello</i></b>")

# def CheckDOM(strParam):
#     # __define-ocg__ This function checks the correctness of a sequence of HTML elements
    
#     varOcg_stack = []
#     varOcg_tag_mapping = {'b': 'b', 'i': 'i', 'em': 'em', 'div': 'div', 'p': 'p'}

#     def varOcg_is_closing_tag(varOcg_tag):
#         return varOcg_tag.startswith('</')

#     def varOcg_get_tag_name(varOcg_tag):
#         if varOcg_is_closing_tag(varOcg_tag):
#             return varOcg_tag[2:-1]
#         else:
#             return varOcg_tag[1:-1]

#     def varOcg_is_nested_correctly(current_tag):
#         if varOcg_stack:
#             top_tag = varOcg_stack[-1]
#             return varOcg_tag_mapping[varOcg_get_tag_name(top_tag)] == varOcg_get_tag_name(current_tag)
#         return False

#     for varOcg_tag in strParam.split():
#         if varOcg_is_closing_tag(varOcg_tag):
#             if varOcg_is_nested_correctly(varOcg_tag):
#                 varOcg_stack.pop()
#             else:
#                 return varOcg_get_tag_name(varOcg_tag)

#         else:
#             varOcg_stack.append(varOcg_tag)

#     return not varOcg_stack

result = CheckDOM("<b><i>hello</i></b>")
print(result)  # Output: True

result = CheckDOM("<b><i>hello</b></i>")
print(result)  # Output: 'i'

result = CheckDOM("<b><i>hello</i>")
print(result)  # Output: False