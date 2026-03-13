from langgraph.graph import StateGraph, START, END
from src.llms.groqllm import GroqLLM
from src.states.blogstate import BlogState


class GraphBuilder:
    def __init__(self, llm):
        self.llm = llm
        self.graph = StateGraph(BlogState)

    def build_topic_graph(self):
        """
        Build a graph to generate bloges based on topic
        """

        ## Nodes
        self.graph.add_node("title_creation")
        self.graph.add_node("content_creation")

        ## Edges
        self.graph.add_edge(START, "title_creation")
        self.graph.add_edge("title_creation", "content_creation")
        self.graph.add_edge("content_creation", END)

        return self.graph
