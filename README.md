# Welcome to Comments miner!


## 1. Package installation
    pip install git+https://github.com/Donvito-911/comments.git
- Debe tener instalado pip (ya sea a través de Anaconda o directamente)
- Si tiene anaconda abra la terminal (macOS) o anaconda prompt (Windows) y copie y corra el comando allí.

## 2. Guide
   1. [Twitter](#twitter) <br/>
   2. [Facebook](#facebook) <br/>
   3. [Ejemplos](#ejemplos) <br/>

## <center>Twitter <a id ="twitter"/> </center>
    from comments.twitter import Tweet, generate_twitter_db, set_twitter_token
El módulo de twitter cuenta con la clase `Tweet` y la función `generate_twitter_db`. Recuerde que antes de utilizar cualquier herramienta debe ingresar las credenciales(bearer token). Para esto se corre la función `set_twitter_token(<tu_bearer_token>)`.
### Tweet

Tweet es una clase que permite generar un dataframe con las respuestas que hicieron en el tweet (solo de primer nivel: se ignoran respuestas de respuestas) y características básicas de los usuarios.

#### Argumentos obligatorios<br/>
  <strong>tweet_id: </strong>(int, str) el id del tweet que se quiere analizar<br/>
  e.g. `Tweet(tweet_id)`

#### Argumentos opcionales (**kwargs)<br/>
  <strong>username: </strong> (str, default = None) el username de la persona que escribió el tweet<br/>
  <strong>max_replies: </strong> (int, str, default = 10) límite de la cantidad de comentarios del tweet (máximo 100 -si es en academic_mode hasta 500-)<br/>
  <strong>bearer_token: </strong> (str, default = BEARER_TOKEN establecido por set_twitter_token) si se quiere cambiar el bearer token del actual tweet<br/>
  <strong>academic_mode: </strong> (boolean, default = False) Si es False busca en "recent" (i.e. los últimos 7 días), si se pone True busca en "all", i.e., histórico de tweets (se debe tener un nivel de acceso de research academic que se valida a través del bearer_token)<br/>
  e.g. `Tweet(tweet_id, username = "AngelicaLozanoc", max_replies = 50, bearer_token = ...)`

<strong>Atributos</strong><br/>
<strong>replies: </strong> (list) Muestra la lista de respuestas del tweet <br/>
e.g. `Tweet(tweet_id).replies` <br/>
<strong>users: </strong> (list) Muestra la lista de usuarios que respondieron al tweet<br/>
e.g. `Tweet(tweet_id).users` <br/>

<strong>Métodos</strong><br/>
<strong>get_dataframe(): </strong> Retorna un pd.DataFrame con las respuestas al tweet <br/>
e.g. `Tweet(tweet_id).get_dataframe()` <br/>
Nota: Si no se agregó el argumento de username, el dataframe retorna None en la columna de original_tweet_username
## Facebook <a id ="facebook"/> 
En construcción
## Ejemplos <a id ="ejemplos"/> 
