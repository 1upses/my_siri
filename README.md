# Initialisation

- éxécutez la commande ``pip install -r requirements.txt`` à la racine du repo
- créez un fichier ``.env`` à la racine du repo
- récupérez l'index du micro que vous allez utiliser avec la commande ``python show_input_devices_list.py``
- récupérer votre [clé d'API OpenAI](https://platform.openai.com/account/api-keys) (pensez à passer votre compte en "paid account")
- collez les informations que vous avez récupéré dans le fichier ``.env`` crée précédemment

```bash
OPENAI_API_KEY=sk-4E1VN3N1kXB9anSfFvK9a1jhD4N2EubeizL5VWyaBiK1Ya77
INPUT_DEVICE_INDEX=2
```

# Utilisation

- éxécutez la commande ``python main.py``
- appuyez sur 'e' pour enregistrer votre message
- attendez environ 30 secondes pour recevoir la réponse de l'assistant
- l'assistant se souvient de ce que vous lui avez dit précédemment
