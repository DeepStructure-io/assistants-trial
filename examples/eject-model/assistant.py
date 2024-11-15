from dataclasses import dataclass
from openai import OpenAI

from util import ensure_vector_store, pretty_print, show_json, wait_on_run

# client = OpenAI()
client = OpenAI(
    api_key="sk-no-api-key-required",
    base_url="https://<your-deepstructure-endpoint>/workflows/assistants/api",
    default_headers={"Authorization": "Basic dXNlcjpwYXNzd29yZA=="},
)


@dataclass
class AssistantSpec:
    name: str
    instructions: str
    model: str
    files: list[str]


spec = AssistantSpec(
    name="ToolsBot",
    instructions="You are a helpful assistant.",
    #model="gpt-4o",
    model="anthropic/claude-3.5-sonnet",
    files=[
        "files/Bauer 6in Bench Grinder.docx",
        "files/Central Machinery 9in Bench Top Band Saw.pdf",
    ],
)


def test():
    assistant = ensure_assistant(client, spec)
    show_json(assistant)

    questions = [
        "How do I change the bandsaw blade?",
        "How do I replace the grinder wheel?",
    ]
    for q in questions:
        print(f"\n\nQuestion: {q}")
        messages = answer_question(assistant, q)
        pretty_print(messages)


def ensure_assistant(client, spec):
    assistants = client.beta.assistants.list()
    assistant = None
    for a in assistants:
        if a.name == spec.name and a.model == spec.model:
            assistant = a
            break
    else:
        print(f"Creating new assistant {spec.name} with model {spec.model}")

        vector_store = ensure_vector_store(client, spec)
        show_json(vector_store)

        assistant = client.beta.assistants.create(
            name=spec.name,
            instructions=spec.instructions,
            model=spec.model,
            tool_resources={"file_search": {"vector_store_ids": [vector_store.id]}},
        )
    return assistant


def answer_question(assistant, question):
    thread = client.beta.threads.create()
    show_json(thread)

    message = client.beta.threads.messages.create(
        thread_id=thread.id,
        role="user",
        content=question,
    )
    show_json(message)

    run = client.beta.threads.runs.create(
        thread_id=thread.id,
        assistant_id=assistant.id,
        # Uncomment me to demo ejecting for individual runs
        # model="...",
        tools=[{"type": "file_search"}],
        tool_choice={"type": "file_search"},
    )
    show_json(run)

    run = wait_on_run(client, run, thread)
    show_json(run)

    messages = client.beta.threads.messages.list(thread_id=thread.id, order="asc")
    show_json(messages)
    return messages


if __name__ == "__main__":
    test()
