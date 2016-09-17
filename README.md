# WebHook handler with Python and SashiDo

SashuDo supports Parse Server WebHooks :) With this, you can now specify any URL to receive a POST in response to triggers like beforeSave and afterSave on objects, as well as when a Cloud Function is called. You now have the freedom to write code in whatever language you want. As long as you have a server running it, your Cloud Code can integrate with it.

With this example we want to show you a simple implementation of webhook handler with Python.

# Run it locally

### 1. Clone this project on you computer.

```
git clone https://github.com/SashiDo/webhook-handler-example.git
cd webhook-handler-example/
```

### 2. Install Flask framework

```
pip install Flask
```

### 3. Run the app

With the following command you'll run the application server on your computer. 

```
python app.py
```

If everything is okey, the output of the command above should be something like:

```
* Running on http://0.0.0.0:8080/ (Press CTRL+C to quit)
```

### 3. Access your webhook from SashiDo.

If you want to access your webhook from SashiDo you have to install and use `ngrok`.  Ngrok is secure tunnels to localhost. In other words ... if you want to expose a local server behind a NAT or firewall to the internet.

Here you can find more info how `ngrok` works: https://ngrok.com/docs


In another `bash` shell/terminal run the follwoing command:

```
ngrok http 8080
```

If everything is okey, the output of the command above should be something like:

```
ngrok by @inconshreveable                                                                                                                     (Ctrl+C to quit)

Session Status                online
Version                       2.1.14
Region                        United States (us)
Web Interface                 http://127.0.0.1:4040
Forwarding                    http://89461962.ngrok.io -> localhost:8080
Forwarding                    https://89461962.ngrok.io -> localhost:8080

Connections                   ttl     opn     rt1     rt5     p50     p90
                              0       0       0.00    0.00    0.00    0.0
```

After that just use `https://89461962.ngrok.io/webhook` as a webhook URL in SashiDo.

# Fin

That's it! Happy coding!

# Requirements
- Git (https://git-scm.com/)
- Python 2.7 (https://www.python.org/)
- ngrok (https://ngrok.com/)
- Flask framework (http://flask.pocoo.org/)
