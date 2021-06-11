## Para este proyecto que ido haciendo de manera autodidacta para aprender estas tecnologías :

	-SQLite
	-Django
	-ReactJs
	-pip

En este ejemplo me base completamente en un autor y en tres de sus grandes libros los cuales son muy claros de como usar el framework de django el cual estan muy sencilos sus ejemplos, ya que te llevan de la mano desde como instalar el entorno de desarrllo, el paquete djando y reframework, asi como la configuracion tanto endpoints, configuracion de el adminisitrador de django, asi como toda la configuracion necearia para crear tu api y son los siguientes:

- Django for Beginners William Vincent
- Django for Professionals William Vincent
- Django for APIs William Vincent



Previo
![alt preview](https://github.com/Eduardishion/todoAppEnDjangoReactJsSqLitePip/blob/master/preview.png)

1.-Recordar que debemos tener instaldo python

	python --version

En este caso se uso python 3.7

2.-Despues puedes consultar los entornos virtuales que tenemos
	
	pipenv --venv

Para activar el entorno virtual del proyecto 
	
	pipenv shell



3.-para ver la version de django 

	python -m django --version 


4.-Despues de que halla sido activado el entorno virtual entramos a carpeta:
	
	./app_tareas


5.-Esto es opcional, para poder ver los dependecias

	pip freeze

6.-Esto es opcional, Si fuera el caso de fallar instalemos las siguientes dependecias, con previamente activado el entorno virtual y no se instales de manera global, si ni en este entorno 

	pip install djangorestframework

7.-Esto es opcional,Para solucionar en el servidor 

Solicitud desde otro origen bloqueada: la política de mismo origen impide leer el recurso remoto en http://127.0.0.1:8000/api/tareas/ (razón: falta la cabecera CORS 'Access-Control-Allow-Origin').

Podriamos consultar esto:

	pip install django-cors-headers

Pero si no falla no son necesarios el paso 6 y 7



8.-Estando hay podemos iniciar el back-end desde CDM usando:


	python manage.py runserver


Puerto de acceso al back-end es,  falta agregar una platilla de bienvenida ya que no la coloque:

	http://127.0.0.1:8000/


Puerto de acceso a la api: 

	http://127.0.0.1:8000/api/tareas/


En este caso como se uso SQLite no hace falta 
instalar ninguna base de datos, se usa la que trae pro defecto Django. 


9.-Para instalar las librerias necesarias
del fronend 
	
	node install

10.-Para ejecutar el front-end
	
	npm start

11.-Si todo sale bien podemos hacer las operacones CRUD, crear, eliminar, leer y modificar

	-insertar
	-eliminar
	-actuliar 
	-mostrar

En esta version use Axios para las peticiones, lo cual me gusto mas que fetch
