# AgenticBlogGeneration

An agentic blog generation system built with LangGraph and Groq LLM. This project uses graph-based workflows to automatically generate blog posts with titles and content, with optional translation capabilities to Hindi and French.

## Features

- **Automated Blog Generation**: Generate complete blog posts from topics using AI
- **Multi-language Support**: Translate generated content to Hindi and French
- **Graph-based Architecture**: Built with LangGraph for structured, agentic workflows
- **FastAPI Integration**: RESTful API for easy integration
- **Groq LLM Integration**: Powered by Groq's fast inference models

## Project Structure

```
├── app.py                 # FastAPI application
├── main.py               # Simple entry point
├── langgraph.json        # LangGraph configuration
├── pyproject.toml        # Project dependencies and metadata
├── requirements.txt      # Python dependencies
├── request.json          # Example API requests
└── src/
    ├── graphs/
    │   └── graph_builder.py  # LangGraph workflow definitions
    ├── llms/
    │   └── groqllm.py        # Groq LLM integration
    ├── nodes/
    │   └── blog_node.py      # Blog generation and translation nodes
    └── states/
        └── blogstate.py      # State definitions for the graph
```

## Installation

1. **Clone the repository:**

   ```bash
   git clone <repository-url>
   cd AgenticBlogGeneration
   ```

2. **Set up Python environment:**

   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   # or using uv
   uv pip install -r requirements.txt
   ```

4. **Set up environment variables:**
   Create a `.env` file in the root directory with:
   ```
   GROQ_API_KEY=your_groq_api_key_here
   LANGSMITH_API_KEY=your_langsmith_api_key_here  # Optional, for tracing
   ```

## Usage

### Running the FastAPI Server

Start the development server:

```bash
python app.py
```

The API will be available at `http://localhost:8000`

### API Endpoints

#### Generate Blog (Topic Only)

```bash
POST /blogs
Content-Type: application/json

{
    "topic": "Agentic AI"
}
```

#### Generate Blog with Translation

```bash
POST /blogs
Content-Type: application/json

{
    "topic": "Agentic AI",
    "language": "hindi"
}
```

Supported languages: `hindi`, `french`

### Using LangGraph CLI

For development and testing with LangGraph Studio:

```bash
uvx --python 3.12 --from "langgraph-cli[inmem]" --with-editable . langgraph dev
```

## Architecture

The system uses a graph-based architecture with the following components:

1. **Graph Builder**: Defines workflows for blog generation and translation
2. **Blog Nodes**: Individual processing units for title creation, content generation, and translation
3. **State Management**: TypedDict-based state management for graph execution
4. **LLM Integration**: Groq LLM for content generation and translation

### Workflows

- **Topic-based Generation**: Creates title and content from a topic
- **Multi-language Generation**: Adds translation routing for Hindi and French

## Dependencies

- **LangGraph**: Graph-based workflow orchestration
- **LangChain**: LLM integration and prompt management
- **FastAPI**: RESTful API framework
- **Groq**: Fast LLM inference
- **Uvicorn**: ASGI server
- **Python-dotenv**: Environment variable management

## Development

### Running Tests

```bash
# Add test commands here
```

### Code Quality

```bash
# Add linting/formatting commands here
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests if applicable
5. Submit a pull request

## License

[Add license information here]

## Acknowledgments

- Built with [LangGraph](https://langchain-ai.github.io/langgraph/)
- Powered by [Groq](https://groq.com/)
- Inspired by agentic AI patterns
