# flask_crud

# Deploy

* No console bash do pythonanywhere digite:

* git clone https://github.com/CaroliAgro/flask_crud.git
* cd flask_crud

* virtualenv --python=python3.7 myvenv

* source myvenv/bin/activate

* pip install flask

* pip install Flask-SQLAlchemy

## Na aba web escolha add a new app

Escolha Next, Manual configuration, Python 3.7, Next nessa ordem

Configure o path para o Source code como segue: /home/Carolina/flask_crud

Configure o path para a virtualenv como segue: /home/Carolinaflask_crud/myvenv

Configure os estáticos colocando URL /static/ e Directory /Carolina/flask_crud/static

Substitua o conte ́udo do arquivo wsgi por:

import sys

path = 'home/flask_crud/flask_crud'

if path not in sys.path:
  
  sys.path.append(path)
from app import app as application

Salve as alterações

Volte para aba web

Clique em reload

Seu website estará no ar em SEUNICK.pythonanywhere.com
