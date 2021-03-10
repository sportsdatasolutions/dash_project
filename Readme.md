## Dash App (Template)

> Dash App ready to deploy to Heroku 💻 🐍 ⚡️ 🎉 🤝

![DashGuide](https://sportsdatasolutionsacademy.s3.eu-west-2.amazonaws.com/public/DashGuide.png)

## Getting Started

> Use this template to create a new personal Github repo.

1. **Click** `Use this Template`.

2. **Create** your new Personal Repository from this template.

## ```Running```

> Instructions for running the solution locally.

1. **Clone** your repo locally.

```bash
$ git clone <github_url> dash_template
$ cd dash_template
```

2. **Install** `Pipenv`.

```bash
$ pip install --user pipenv
```

3. **Install** project dependencies via `Pipfile`. Make sure you are in cloned project root.

```bash
$ pipenv install
```

4. **Serve** the App.

```bash
$ pipenv run python app.py
```

5. Finally, **visit** the local port that the app is serving on, via your browser: [http://127.0.0.1:8050/](http://127.0.0.1:8050/).

> :warning: **Quit Serving**
>
> It's good practice to **manually quit serving** things that are long running, e.g. when you serve the dash app, it will be running and listening on a local port until you stop serving it. If we quit the local server unexpectedly, it may block that port until we restart out machines. To **quit serving** simply use the **`control + C`** keys and you should see your **command prompt** return.

## Contributing

> See [```contributing.md```](./contributing.md)
