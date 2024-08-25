# LangChain Query Assistant

LangChain Query Assistant is a project designed to integrate LangChain with OpenAI to create an intelligent agent for interacting with SQLite databases. This assistant enables you to perform SQL operations, retrieve and describe database schema, and generate reports based on SQL queries.

## Features

- **LangChain Integration**: Utilizes LangChain's framework for building advanced query assistants.
- **OpenAI Integration**: Leverages OpenAI's language models to handle and interpret complex queries.
- **SQL Operations**: Includes tools for running SQL queries, listing tables, and describing table schemas.
- **Report Generation**: Creates and writes detailed HTML reports based on query results.

## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/langchain-query-assistant.git
    cd langchain-query-assistant
    ```

2. **Create a virtual environment**:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required packages**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Set up environment variables** by creating a `.env` file in the project root with the following content:
    ```plaintext
    OPENAI_API_KEY=your_openai_api_key
    ```

## Usage

### Running the Query Assistant

1. **Ensure environment variables are loaded**:
    ```bash
    source .env
    ```

2. **Execute the main script** to perform a query:
    ```bash
    python main.py
    ```

   This script initializes the LangChain agent, connects to the SQLite database, and executes a predefined query.

### Customizing Queries and Reports

1. **Modify the `input_text` dictionary** in `main.py` to change the query and report instructions.
2. **Run the script** again to execute the updated query and generate the new report:
    ```bash
    python main.py
    ```

## Project Structure

- **`main.py`**: Main script that sets up the LangChain agent, executes SQL queries, and generates reports.
- **`sql.py`**: Contains functions for interacting with the SQLite database, including listing tables, running queries, and describing table schemas.
- **`report.py`**: Defines the tool and schema for generating HTML reports.
- **`chat_model_start_handler.py`**: Manages interactions with the OpenAI chat model and formats output messages.

## Contributing

Contributions are welcome! Please fork this repository and submit a pull request with any improvements or bug fixes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [LangChain](https://github.com/langchain-ai/langchain)
- [OpenAI](https://openai.com)
- [SQLite](https://www.sqlite.org)
