import { Application, Assistants } from "@deepstructure/sdk";

export const application = new Application();

export const assistants = new Assistants({
    evalsApi: true,
    chatCompletionsApi: true,
});

application.addWorkflow(assistants.workflows());
