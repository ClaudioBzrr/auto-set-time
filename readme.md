## Instalação

Use o "pip" para instalar as dependências necessárias do projeto

```bash
pip install requirements.txt
```

Ultilize o commando abaixo para gerar o arquivo executável que se encontrará na pasta "dist" :

```bash
pyinstaller --onefile --exclude-module _bootlocale -w -F timer.py
```

## Licença
[MIT](https://choosealicense.com/licenses/mit/)