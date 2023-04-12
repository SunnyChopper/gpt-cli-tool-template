# Tool Template

This project is meant to serve as a template in order to create other GPT-powered tools that are focused on doing one thing very well. 

## Usage

In order to use this template effectively, you will have to follow these steps:

1. Whenever starting a new project for a GPT-powered tool, create a top-level folder and then copy everything in this template over there.

2. Create an `.env` file that contains a variable for `OPENAI_API_KEY` which you can acquire from the OpenAI dashboard. 

3. Run the following command in the terminal to install the dependencies for the template:

   ```bash
   $ pip install -r requirements.txt
   ```

4. In order to edit the initial prompt that kicks off the application, modify the `START_PROMPT` variable in the `init.py` file, which exists at the top-level of the template folder structure. 

## Components

There are several components to this template. Let's go over them:

1. **Models** - They hold the data that the chat application is working with in an organized fashion. The source code is not just throwing around random `dict` variables. This makes the code readable and maintainable. If there is ever a change in the structure of the data that OpenAI, we simply need to modify the corresponding model. 
2. **Constants** - Simply hold the labels for various things. As of now, there are constants for the various roles that can be taken on in ChatML and the different GPT models that you can use for running operations. 

## Future Work
| Task | Description |
| --- | --- |
| Add new models | Add more models to the `models.py` file. This can be beneficial for doing less complex tasks for a cheaper price. |
| Add GPT agents | Create a framework for adding GPT agents that can be used to perform specific tasks. The main agent can then use these agents to perform tasks. |
| Long-term memory | Add a long-term memory to the chat application. This can be done by using a database to store the data that the chat application is working with. Most likely will have to use a vector store like Pinecone or Chroma. |
| Chat history | Add a chat history to the chat application. This can be done by storing the chat history on the user's device in the form of a file. |