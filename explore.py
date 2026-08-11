from llm_sdk import Small_LLM_Model

def init_model() -> None:
    """init model"""
    print("Model loading")
    llm = Small_LLM_Model() #init model
    print("Model ready")

if __name__ == "__main__":
    init_model()