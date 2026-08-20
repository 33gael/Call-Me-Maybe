from llm_sdk import Small_LLM_Model


#  init model
print("Model loading")
llm = Small_LLM_Model()
print("Model ready")


def ft_encode(prompt):
    """try using encode()"""
    encode_res = llm.encode(prompt)
    return (encode_res)


def ft_decode(prompt):
    """try using decode()"""
    encode_res = ft_encode(prompt)
    integers = encode_res[0].tolist()
    for integer in integers:
        print('"' + llm.decode(integer) + '"')
    return (integer)


if __name__ == "__main__":
    prompt = "What is the sum of 2 and 3?"
    ft_decode(prompt)
