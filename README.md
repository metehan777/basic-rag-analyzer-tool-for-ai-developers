# RAG Analysis Tool

A powerful and interactive tool for AI/ML developers to experiment with Retrieval-Augmented Generation (RAG) analysis. This application allows users to upload documents, process them using OpenAI embeddings, and perform similarity-based searches with interactive visualizations. Created by Metehan. Follow @metehan777 on X

## Features

- **Document Upload and Processing**
  - Support for multiple document formats (TXT, MD, PDF)
  - Automatic text chunking with configurable size and overlap
  - Efficient document processing using LangChain's text splitter

- **Similarity Search using OpenAI Embeddings**
  - Integration with OpenAI's text-embedding-ada-002 model
  - Fast and accurate similarity search using FAISS vector store
  - Configurable number of results (top-k)

- **Interactive Query Interface**
  - Clean and intuitive Streamlit-based web interface
  - Real-time search results with expandable content
  - Adjustable search parameters

- **Visualization of Similarity Scores**
  - Interactive bar charts using Plotly
  - Visual representation of similarity scores
  - Easy-to-interpret search result rankings

## Prerequisites

- Python 3.8+
- OpenAI API key (Get one from [OpenAI Platform](https://platform.openai.com))

## Installation Instructions

1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/rag-analysis-tool.git
   cd rag-analysis-tool
   ```

2. **Install Dependencies**
   ```bash
   pip install streamlit openai faiss-cpu langchain plotly
   ```

3. **Set up OpenAI API Key**
   - Create a `.env` file in the project root
   - Add your OpenAI API key:
     ```
     OPENAI_API_KEY=your_api_key_here
     ```

## Usage Guide

1. **Running the Application**
   ```bash
   streamlit run main.py
   ```
   The application will be available at `http://localhost:5000`

2. **Uploading Documents**
   - Click on the file upload section
   - Select one or multiple documents (TXT, MD, PDF)
   - Wait for the processing confirmation

3. **Querying the System**
   - Enter your search query in the text input field
   - Adjust the number of results using the slider
   - Click "Search" to retrieve similar passages

4. **Understanding the Results**
   - Results are displayed in expandable sections
   - Each result shows:
     - The matched text passage
     - A similarity score (0-1, higher is better)
   - The bar chart visualizes similarity scores across results

## Technologies Used

- **Streamlit**: Web interface and interactive components
- **OpenAI API**: Document and query embedding generation
- **FAISS**: Efficient similarity search and vector storage
- **LangChain**: Document processing and text splitting
- **Plotly**: Interactive visualization of search results

## Contributing

Feel free to open issues or submit pull requests. We welcome contributions from the community!

## License

MIT License - feel free to use this tool for your projects!
