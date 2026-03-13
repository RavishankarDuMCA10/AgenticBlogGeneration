from src.states.blogstate import BlogState
from langchain_core.messages import SystemMessage, HumanMessage
from src.states.blogstate import Blog


class BlogNode:
    """
    A class to represent the blog node
    """

    def __init__(self, llm):
        self.llm = llm

    def title_creation(self, state: BlogState):
        """
        Create the title for the blog
        """

        if "topic" in state and state["topic"]:
            prompt = """
                    You are an expert blog content writer. Use Markdown formatting. Generate
                    a blog title for the {topic}. This title should be creative and SEO friendly.
                    Provide title only and don't add description of title.
                    """

            system_message = prompt.format(topic=state["topic"])
            response = self.llm.invoke(system_message)
            return {"blog": {"title": response.content}}

    def content_genration(self, state: BlogState):
        """
        Generate the content for the blog
        """

        if "topic" in state and state["topic"]:
            system_prompt = """
                    You are an expert blog content writer. Use Markdown formatting. Generate
                    a detailed blog content with detailed breakdown for the {topic}.
                    """

            system_message = system_prompt.format(topic=state["topic"])
            response = self.llm.invoke(system_message)
            return {
                "blog": {"title": state["blog"]["title"], "content": response.content}
            }

    def translation(self, state: BlogState):
        """
        Translate the content to the specified language.
        """
        translation_prompt = """
        Translate the following content into {current_language}.
        - Maintain the original tone, style, and formatting.
        - Adapt cultural references and idioms to be appropriate for {current_language}.
        Return the result strictly as a JSON object with two keys: 'title' and 'content'.

        ORIGINAL CONTENT:
        {blog_content}

        """

        # blog_content = state["blog"]["content"]
        blog_obj = state["blog"]
        blog_content = (
            blog_obj.content if hasattr(blog_obj, "content") else blog_obj["content"]
        )

        messages = [
            HumanMessage(
                translation_prompt.format(
                    current_language=state["current_language"],
                    blog_content=blog_content,
                )
            )
        ]

        translation_content = self.llm.with_structured_output(
            Blog, method="json_mode"
        ).invoke(messages)
        return {"blog": {"content": translation_content}}

    def route(self, state: BlogState):
        return {"current_language": state["current_language"]}

    def route_decision(self, state: BlogState):
        """
        Route the content to the respective translation function.
        """
        if state["current_language"] == "hindi":
            return "hindi"
        elif state["current_language"] == "french":
            return "french"
        else:
            return state["current_language"]
