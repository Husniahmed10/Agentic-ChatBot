from src.langgraphagenticai.state.state import State 

class ChatbotWithToolNode:
    """ 
    Chatbot logic enhanced with tool integration
    """

    def __init__(self, model):
        self.llm = model 


    
    def create_chatbot(self, tools):
        """ 
        ChatBot logic for processingg the input and returning a response
        """
        llm_with_tools = self.llm.bind_tools(tools)

        def chatbot_node(state:State):
            """ 
            Chatbot logic for processing the input state and returning a response
            """

            return{"messages":[llm_with_tools.invoke(state['messages'])]}
        
        return chatbot_node