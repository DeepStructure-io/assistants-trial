import json
import time


def pretty_print(messages):
    print("# Messages")
    for m in messages:
        print(f"{m.role}: {m.content[0].text.value}")
    print()


def show_json(obj):
    print(json.loads(obj.model_dump_json()))


def wait_on_run(client, run, thread):
    while run.status == "queued" or run.status == "in_progress":
        run = client.beta.threads.runs.retrieve(
            thread_id=thread.id,
            run_id=run.id,
        )
        time.sleep(0.5)
    return run


def vector_store_name_from_spec(spec):
    return spec.name + " files"


def ensure_vector_store(client, spec):
    name = vector_store_name_from_spec(spec)
    vector_stores = client.beta.vector_stores.list()
    for vs in vector_stores:
        if vs.name == name:
            return vs
    return create_vector_store(client, spec)


def create_vector_store(client, spec):
    name = vector_store_name_from_spec(spec)

    file_streams = [open(path, "rb") for path in spec.files]

    print(f"Creating new vector store for {spec.name} and files {spec.files}")
    vector_store = client.beta.vector_stores.create(name=name)

    file_batch = client.beta.vector_stores.file_batches.upload_and_poll(
        vector_store_id=vector_store.id, files=file_streams
    )
    if file_batch.status != "completed":
        raise Exception(f"Failed to upload files: {file_batch.status}")

    return vector_store
