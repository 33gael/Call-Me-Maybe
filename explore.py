from llm_sdk import Small_LLM_Model

def ft_encode(str):
    """try using encode()"""
    print("Model loading")
    llm = Small_LLM_Model() #init model
    print("Model ready")
    res = llm.encode(str)
    return (print(res))

if __name__ == "__main__":
    str = "What is the sum of 2 and 3?"
    ft_encode(str)
