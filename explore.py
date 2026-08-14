from llm_sdk import Small_LLM_Model

print("Model loading")
llm = Small_LLM_Model()  #  init model
print("Model ready")

def ft_encode(str):
    """try using encode()"""
    res = llm.encode(str)
    print(res)
    res = llm.decode(res)
    print(res)
    return (res)

if __name__ == "__main__":
    str = "What is the sum of 2 and 3?"
    ft_encode(str)
