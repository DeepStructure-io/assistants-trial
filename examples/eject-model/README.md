# Assistants Example: Eject from OpenAI Models

This example demonstrates:

-   An existing Python application, derived from the OpenAI Cookbook, that uses the Assistants API to answer questions from a set of documents
-   Switching the application from the OpenAI backend to DeepStructure by changing one line of code
-   Switching the application's Assistant model from `gpt-4o` to other non-OpenAI models by changing one more line of code

## Setup

To make it easier to run this example outside of the dev container, you can use the Pixi project:

```sh
cd apps/assistants-demo/examples/eject-model
pixi install
pixi shell
```

Steps to run the example:

0. Ensure that you have provisioned:
    - `OPENAI_API_KEY` in local environment
    - a DeepStructure Assistants endpoint provisioned with `OPENAI_API_KEY` and `OPENROUTER_API_KEY`
1. Find the URL of Assistants endpoint. The `assistants-demo` app is at https://assistants-demo-deepstructure-io.deepstructure.app/workflows/assistants/api/ .
2. On your local machine, _outside of the devcontainer_, run `assistants.py` in a terminal with a suitable python environment like a conda or venv. You should see it print the answers to two questions about power tools.
3. Take the endpoint URL you found in step (1), and edit `assistants.py` to point at the DeepStructure Assistants implementation. Re-run the demo and you should see a similar results as in step (2) above.
4. Edit the `model` parameter in the `AssistantSpec` near line 30. Use the `anthropic/claude-3.5-sonnet` model to start. Re-run the demo and you should see a similar results as in step (2) above. Now your Assistant is using a state-of-the-art model!
5. Next, edit the `model` parameter of the Assistants run, near line 65. Use the `meta-llama/llama-3-8b`. Re-run the demo, and you will probably get a nonsense or not-very-useful result. That's OK! We'll show how to optimize a fast & cheap model in followup videos.
