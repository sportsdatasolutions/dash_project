## Dash App (Template)

> Dash App ready to deploy to Heroku 💻 🐍 ⚡️ 🎉 🤝

![DashGuide](https://sportsdatasolutionsacademy.s3.eu-west-2.amazonaws.com/public/Links/DashSideBarTemplate.png)
> Credit [@amber-luzar](https://github.com/amber-luzar) - GB Hockey.

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

2. **Install** `Pipenv` (if you havn't already).

```bash
$ pip install --user pipenv
```

3. **Install** project dependencies via `requirements.txt`.

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

## `Deploying`

> Deploying your app to Heroku.

1. Get ready for production! First, we'll want to create a new `requirements.txt` file to reflect our current project's dependencies. So we'll remove the currrent one and get `pipenv` to generate a new one.

  ```bash
  $ rm requirements.txt
  $ pipenv lock -r > requirements.txt
  ```

2. Add `Procfile`...this file will tell **Heroku** how to ***start*** your Dash App with `gunicorn` (this should actually already be there).

  ```
  web: gunicorn app:server
  ```

3. Create a new **[Heroku App](https://dashboard.heroku.com/new-app)**. Give it a **name** and select a ***relevant*** **region** (one close to you or your client).

4. **Link** your Project's Github repo to your **Heroku App**. Be sure to **enable automatic deploys** once you link your Github repo. This way, every time you **push new commits** to your **Github** repo, **Heroku will automatically rebuild your app** with the changes.

  ![HerokuGithub](https://sportsdatasolutionsacademy.s3.eu-west-2.amazonaws.com/public/HerokuGithub.png)
  
  **Note**: You may optionally place your app in a development **pipeline**. To do so, simply click the `Choose a pipeline` dropdown and create a new one. Create a `staging` and a `production` app. Now everytime you make changes to your app, it will be deployed to the `staging` app where you can test and debug your changes. When you see all is well, you can simply **promote** the changes to your `production` app, which is the one everyone will be visiting.

  ![EnableCIHeroku](https://sportsdatasolutionsacademy.s3.eu-west-2.amazonaws.com/public/EnableCIHeroku.png)
  
> :warning: **Environment Variables**
> 
> If you are using **Dash Auth**, make sure you are following the correct procedures for using [environment variables locally](https://www.nylas.com/blog/making-use-of-environment-variables-in-python/) and adding [environment variables in Heroku](https://devcenter.heroku.com/articles/config-vars#using-the-heroku-dashboard). It's important you don't simply hard code the actual `VALID_USERNAME_PASSWORD_PAIRS` dictionary and rather get it from the Environment (wether it be locally or in Heroku)!


5. **Push your project to Github!**

  ```bash
  $ git add .
  $ git commit -m "mvp"
  $ git push
  ```

  **Note**: You can watch Heroku build your app, just click `view build`! Otherwise, click the overview tab and wait for a ***deployed*** message.


## Contributing

> See [```contributing.md```](./contributing.md)

