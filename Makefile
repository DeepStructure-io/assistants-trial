all: deploy

app-add:
	@pnpm ds app add

deploy:
	@pnpm ds deploy

build:
	@pnpm ds build

dev:
	@pnpm ds dev

clean:
	@rm -rf .ds/

.PHONY: app-add deploy build dev clean
