This DeepStructure has been bootstrapped with `create-deepstructure-app` and application runs 3 `HttpSource` workflows.

1. [Chat Completions Adapter](https://github.com/DeepStructure-io/DeepStructure/blob/617d735a63164bd90891547d03aeda257b2aa0a6/apps/assistants-chat-completions/src/workflows/chat-completions/index.ts#L8) for chat completions interface (`{{DOMAIN}}/workflows/assistants-chat/api`)
2. [Assistants API](https://github.com/DeepStructure-io/DeepStructure/blob/617d735a63164bd90891547d03aeda257b2aa0a6/apps/assistants-chat-completions/src/app.ts#L6) used to power chat completions adapter (`{{DOMAIN}}/workflows/assistants/api`)
3. [Evals Api](https://github.com/DeepStructure-io/DeepStructure/blob/617d735a63164bd90891547d03aeda257b2aa0a6/apps/assistants-chat-completions/src/workflows/assistants-evals-monitor/index.ts#L8) for serving data to the [assistants-evals-dashboard](https://github.com/DeepStructure-io/assistants-dashboard) (`{{DOMAIN}}/workflows/assistants-evals/api`)

You'll notice that the **api urls** follow a pattern of `{{DOMAIN}}/workflows/{{workflow-name}}/api`

## Quickstart

To run this app, you must:

1. Run `ds dev` when in project directory.
2. From the DeepStructure root, run `pixi run tika-start`. We use Tika for document parsing and text extraction for RAG purposes, see https://bookish-meme-8q2gl6e.pages.github.io/posts/using-tika/
3. Create an assistant with a `POST` request to [/assistants](https://platform.openai.com/docs/api-reference/assistants/createAssistant) endpoint with baseUrl `http://localhost/workflows/assistants/api`. This can be done either directly with curl, or by using [OpenAI's sdk](https://platform.openai.com/docs/api-reference/assistants/createAssistant?lang=node.js).

**Note:** There are some scripts under `apps/assistants/examples` folder that create assistants specialized for different use cases. For example, from `apps/assistants-demo/examples/eject-model` run `pixi shell` and from that shell run `python assistant.py`

The API url for the chat completions wrapper is:
http://localhost/workflows/assistants-chat/api

From here, you can use it with [ChatCraft](https://chatcraft.org) or any other chat LLM client that accepts a custom base url. To do so, you must:

1. **OPTIONAL**: Clone and launch ChatCraft locally (see their CONTRIBUTING.md) if you want to make `Mixed Content` requests
2. In the settings (top right) add a provider (NAME and API KEY can be anything)
3. Select the provider and the model (bottom right)
4. Interact!

For more information on how to run the app, supported endpoints, and integration with ChatCraft or other chat LLM clients, please refer to this blog post.
https://bookish-meme-8q2gl6e.pages.github.io/posts/assistants-powered-chat-completions.md/

## Testing

All the unit tests can be found under `/tests` directory with the files named in format `{{workflow-name}}.test.ts`

These can be run with:

```bash
pnpm test
```

or

```bash
vitest run
```

Tests for assistants api are [in the sdk](https://github.com/DeepStructure-io/DeepStructure/blob/617d735a63164bd90891547d03aeda257b2aa0a6/sdk/npm/test/smoke-tests/smoke.test.ts).
