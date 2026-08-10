from dotenv import load_dotenv
from gigachat import GigaChat

load_dotenv()

with GigaChat(verify_ssl_certs=False) as client:
    models = client.get_models()
    for model in models.data:
        print(model.id_)
