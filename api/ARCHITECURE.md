# Architecture d'une API 

Structuration d'une API

### Les méthodes

Les méthodes sont comme la grammaire de communication d'une API avec le reste du monde.  Lorsque l'on communique avec quelqu'un et qu'on souhaite recevoir quelque chose de cette personne, il faut précisier si on a besoin d'une information, qu'on veut lui transmettre quelque chose ou revenir sur ce qu'on s'est dit précédemment. 
Les méthodes nous permettent de faire cela avec les APIs:  
方法就像API与世界其他地方沟通的语法。 当你与某人沟通并想从他们那里得到一些东西时，你需要说明你是需要信息，想把一些东西转交给他们，还是想回到你之前所说的话。
这些方法允许我们用API做这件事。

- GET : permet de demander une ressource au serveur
- POST : permet d'envoyer et (souvent) de créer une ressource coté serveur
- PUT/PATCH: permettent de modifier tout ou partie d'une ressource
- DELETE : permet de supprimer une ressource

- GET：允许我们从服务器上请求一个资源
- POST：允许我们发送并（通常）在服务器端创建一个资源。
- PUT/PATCH：允许我们修改一个资源的全部或部分内容
- DELETE：允许你删除一个资源

FastAPI met à disposition des décorateurs qui permettent de définir ces méthodes.
提供装饰器来定义这些方法。

```python
@router.get("/{id}", tags=["posts"])
@router.post("/", tags=["posts"])
@router.put("/{id}", tags=["posts"])
@router.delete("/{id}", tags=["posts"])
```

La combinaison de ces méthodes avec le path des routes vers celles-ci permettent de structurer une API. 
这些方法与通往这些方法的路径的结合，使得一个API可以被结构化。

### Path

Le path est le chemin qui permet d'accéder à une ressource. Il est très important de bien structurer ce chemin d'accés pour garder une certaine cohérence et compréhension du fonctionnement. 
路径是允许访问一个资源的路径。构建这一路径以保持某种连贯性和对操作的理解是非常重要的。

Dans FastAPI c'est très simple il suffit de définir pour chaque méthode vu plus haut, la string permettant d'accéder aux ressources.
在FastAPI中，为上面看到的每个方法定义允许访问资源的字符串是非常简单的。

```python
@router.get("/users", tags=["users"])
```

permettrait de récupérer l'ensemble des utilisateurs.

```python
@router.get("/user/{user_id}")
```

permettrait de récupérer l'utilisateur spécifique correspondant à l'id. 

```python
@router.get("/user/{user_id}/posts/", tags=["posts"])
```

permettrait de récupérer l'ensemble des posts d'un utilisateur.
Et si on combine avec la méthode POST


```python
@router.post("/user/{user_id}/posts", tags=["posts"])
```

permettrait de créer un nouveau post pour cet utilisateur.

Ce chemin est équivalent au chemin utilisé par le navigateur web pour naviguer sur un site web. 

- https://www.lemonde.fr/ : La page de garde
- https://www.lemonde.fr/economie-mondiale/ : On accède à une catégorie spécifique du site. 
- https://www.lemonde.fr/argent/article/2021/09/06/bourse-est-ce-le-moment-d-investir-sur-les-marches-emergents-notamment-chinois_6093537_1657007.html : on accède à un a un article spécifique dans une catégorie déterminée. 

## Routes
Les routes représente la structure globale de l'api. Elles définissent l'interface de communication et l'interface d'interaction avec votre application. Ces routes utilisent les deux concepts vu plus haut, c'est la combinaisaon d'un chemin et d'une méthode.  
路由代表了api的全局结构。它们定义了与你的应用程序的通信接口和交互接口。这些路线使用上面看到的两个概念，它是一个路径和一个方法的组合。

Très souvent on peut retrouver des routes de base qui répondent au principe CRUD. 

CRUD (create, read, update, delete) (créer, lire, mettre à jour, supprimer) est un acronyme pour les façons dont on peut fonctionner sur des données stockées. 
C'est un moyen mnémotechnique pour les quatre fonctions de base du stockage persistant. CRUD fait généralement référence aux opérations effectuées dans une base de données ou un magasin de données, mais peut également s'appliquer aux fonctions de niveau supérieur d'une application telles que les suppressions logicielles lorsque les données ne sont pas supprimées mais marquées comme supprimées via un état.

Ici on peut définir les routes permettant de réaliser ces opérations CRUD sur nos Posts.

很多时候，我们可以找到符合CRUD原则的基本路线。

CRUD（创建、读取、更新、删除）是人们对存储数据进行操作的方式的首字母缩写。它是持久性存储的四个基本功能的助记符。CRUD一般是指在数据库或数据商店中进行的操作，但也可以适用于应用程序的更高层次的功能，如软删除，即数据没有被删除，但通过报告标记为删除。

在这里，我们可以定义路由来对我们的帖子执行这些CRUD操作。

```python
@router.post("/posts", tags=["posts"])
async def create_post(**kwargs):
   pass  
```
Permet de créer un nouveau post grâce à la méthode POST

```python
@router.get("/posts", tags=["posts"])
async def get_posts(**kwargs):
    pass
```

Ici on utilise la méthode GET sur le même path qui nous permet de récupérer l'ensemble des posts.

```python
@router.get("/posts/{post_id}", tags=["posts"])
async def get_post_by_id(post_id: str, **kwargs):
    pass
```

Permet de récupérer le post précédemment créé grace à son id. Vous voyez aussi, que le template du path permet de récupérer l'id du post dans les paramètres de la fonction, et donc de l'utiliser directement dans le code. 
```python
@router.put("/posts/{post_id}", tags=["posts"])
async def update_post_by_id(post_id: str, **kwargs):
    pass
```

Permet de mettre à jour un post grâce son id.

```python
@router.delete("/{post_id}", tags=["posts"])
async def delete_post_by_id(post_id: str, **kwargs):
    pass
```

Et ici de le supprimer.

## La gestion des données

Afin de gérer la création, la consultation et la mise à jour des données il faut mettre en correspondance les routes à des méthodes permettant de récupérer et stocker les données. 

Il y a de nombreuses manières de communiquer de la données avec l'API. 

- Path parameters
- Query paramters
- Request Body
为了管理数据的创建、咨询和更新，有必要将路由映射到检索和存储数据的方法。

有许多方法可以与API进行数据通信。

路径参数
查询参数
请求机构


## Schemas
Les schémas sont un moyen de garantir la validité des données utilisées par l'application. Les données provenant des utilisateurs sont souvent incomplètes ou ne correspondent pas aux attentes de votre application. Les schémas de données sont utilisés pour valider le bon format, le bon remplissage des champs de vos objets. 
Vous pouvez par exemple :
- Que l'age est bien un nombre entier compris entre 18 et 99 ans 
- Valider une adresse email
- Valider une adresse postale
- Valider la longueur d'un mot de passe 
- Que le mot de passe et la confirmation sont identiques
- La taille d'une chaine de characteres (comme sur Twitter)
- La présence obligatoire de la date de naissance dans un formulaire
模式是一种确保应用程序所使用的数据的有效性的方法。来自用户的数据往往是不完整的，或者与你的应用程序的期望不一致。数据模式被用来验证正确的格式，正确地填写你的对象中的字段。
例如，你可以:
- 年龄是18岁至99岁之间的整数。
- 验证一个电子邮件地址
- 验证一个邮政地址
- 验证密码的长度 
- 密码和确认是相同的
- 一串字符的大小（如在Twitter上）。
- 表格中必须有出生日期


Toutes ces validations, permettent de garantir une cohérence des données échangées. Ce format d'échange de données entre le front (les utilisateurs) et le back (votre application) ou entre deux backs avec une application tierce.
  
- Serialization (Load) : 
Permet de déterminer comment est ce que la donnée brute va être traitée par le schéma. La donnée brute est ingérée par le schéma, traitée par les règles définies et produit un objet Python utilisable. 
Certains champs ne pourront pas être modifié par l'utilisateur, par exemple l'identifiant géré par la base de données ou la date de création de l'objet seront souvent des champs qui seront impossible à modifier et qui seront ignorés par cette phase de serialisation.
- Deserialization (Dump)
La Déserialization permet de traduire un objet métier afin de le partager avec vos utilisateurs ou avec une application tierce. Cette phase permet de transformer des données pour les rendre interpretable par des utilisateurs exterieurs. 
Par exemple, cette phase est utilisée pour traduire des champs dans une certaine langue, transformer certains champs textuels pour les rendre plus propres, arrondir des nombres décimaux.
所有这些验证都保证了所交换的数据的一致性。这种格式用于在前台（用户）和后台（你的应用程序）之间或在两个后台与第三方应用程序之间交换数据。
  
- 序列化（加载）。
允许你决定原始数据将如何被模式处理。原始数据被模式摄取，被定义的规则处理，产生一个可用的Python对象。
有些字段不能被用户修改，例如数据库管理的标识符或对象的创建日期往往是不能修改的字段，将被这个序列化阶段所忽略。
- 反序列化（转储）。
反序列化允许你翻译一个业务对象，以便与你的用户或第三方应用程序分享它。这一阶段允许对数据进行转换，使其可被外部用户解释。
例如，这一阶段用于将字段翻译成某种语言，改造某些文本字段使其更加简洁，将小数点数字四舍五入。


```python
from typing import Optional
from datetime import datetime
from pydantic import BaseModel, Field
from uuid import uuid4
from typing_extensions import Annotated


class Post(BaseModel):
    id: Annotated[str, Field(default_factory=lambda: uuid4().hex)]
    title: str
    description: Optional[str]
    created_at: Annotated[datetime, Field(default_factory=lambda: datetime.now())]
    updated_at: Annotated[datetime, Field(default_factory=lambda: datetime.now())]

    class Config:
        orm_mode = True

 ```


## Base de données
Les différentes bases de données
- SQL 
Les principales bases de données SQL utilisées seront MySQL ou POSTGRESQL. Elles sont simples d'utilisation et les formats de données sont assez courant ce qui permet de trouver énormément de documentation sur la structuration des données. 
- NoSQL 
Les bases de données NoSQL sont très puissantes mais beaucoup plus complexes à gérer. Les modèles de données complexes sont plus fastidieux à mettre en place car elles utilisent des concepts différentes des habitudes de la plupart des gens. 

Pour créer les connexions à la base de données il faut : 
SQL 使用的主要SQL数据库将是MySQL或POSTGRESQL。它们很容易使用，而且数据格式相当普遍，这意味着有很多关于数据结构的文件。
NoSQL 
NoSQL数据库非常强大，但管理起来要复杂得多。复杂的数据模型设置起来比较繁琐，因为它们使用的概念与大多数人习惯的不同。
要创建数据库连接，你需要:

-> api/app/models/database.py
https://fastapi.tiangolo.com/tutorial/sql-databases/
```python
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os 


POSTGRES_USER = os.environ.get("POSTGRES_USER")
POSTGRES_PASSWORD = os.environ.get("POSTGRES_PASSWORD")
POSTGRES_DB = os.environ.get("POSTGRES_DB")


SQLALCHEMY_DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@postgres/{POSTGRES_DB}"
print(SQLALCHEMY_DATABASE_URL)

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)
SessionLocal = sessionmaker(autocommit=False, autoflush=True, bind=engine)

BaseSQL = declarative_base()

```

### Models
Le model est la structuration de la donnée d'un point de vue de la base de données. 
Les modèles sont plus ou moins figés ou complêtement dynamiques en fonction du type de base de données utilisé mais il reste un point essentiel pour structurer de manière méthodique les données qui vont être utilisées par l'application.
模型是指从数据库的角度对数据进行结构化。模型或多或少是固定的，或完全是动态的，这取决于所使用的数据库类型，但它仍然是有条不紊地构建将被应用程序使用的数据的一个基本点。


-> api/app/models/post.py
```python
from sqlalchemy import Column, String, DateTime
from sqlalchemy.dialects.postgresql import UUID
from .database import BaseSQL


class Post(BaseSQL):
    __tablename__ = "posts"

    id = Column(UUID(as_uuid=True), primary_key=True, index=True)
    title = Column(String)
    description = Column(String)
    created_at = Column(DateTime())
    updated_at = Column(DateTime())

```

Pour créer la connexion avec la base de données, il nous faut définir les points d'accès que FastAPI par le biais de SQLAlchemy va utiliser pour `discuter` avec votre base de données. Pour cela il nous faut définir l'URL de connexion ainsi que les paramètres d'authentification. On créé un engine et une session, c'est ce qui nous permettra d'intéragire avec notre BDD.
为了创建与数据库的连接，我们需要定义访问点，通过SQLAlchemy的FastAPI将用来与你的数据库对话。要做到这一点，我们需要定义连接URL和认证参数。我们创建一个引擎和一个会话，这将使我们能够与我们的数据库互动。

```python
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os 


POSTGRES_USER = os.environ.get("POSTGRES_USER")
POSTGRES_PASSWORD = os.environ.get("POSTGRES_PASSWORD")
POSTGRES_DB = os.environ.get("POSTGRES_DB")


SQLALCHEMY_DATABASE_URL = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@postgres/{POSTGRES_DB}"
print(SQLALCHEMY_DATABASE_URL)

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)
SessionLocal = sessionmaker(autocommit=False, autoflush=True, bind=engine)

BaseSQL = declarative_base()
```

Lors de la première synchronisation avec la base de données, SQLAlchemy doit pouvoir créer le schéma de données en base. C'est à dire créer les tables et les colonnes avec les types correspondants. Pour cela nous devons appeler une méthode à l'initiation de FastAPI.
当第一次与数据库同步时，SQLAlchemy必须能够创建基本的数据模式。也就是说，用相应的类型创建表和列。为此，我们需要在FastAPI的启动阶段调用一个方法。

```python
from .models import BaseSQL

@app.on_event("startup")
async def startup_event():
    BaseSQL.metadata.create_all(bind=engine)
```

Ici on utilise une méthode asynchrone qui est triggered avec un evenement `startup` envoyé par FastAPI à son instanciation. Cette méthode permet donc de créer si il n'existe pas le format de données dans la base de données PostgresSQL dans ce cas.
在这里，我们使用一个异步方法，它被FastAPI在其实例化时发送的 "启动 "事件所触发。因此，在这种情况下，如果数据格式在PostgresSQL数据库中不存在，这个方法就会创建。

### Les services

La structuration sous forme de service permet de décorréler la partie base de données et schemas (donc données brutes) de la partie routes. 
Les services font le lien entre la partie gestion métier et la structuration de l'API. 
服务形式的结构化允许数据库和模式部分（即原始数据）与路由部分解耦。
这些服务在业务管理部分和API的结构化之间建立了联系。

```python
from typing import List

from sqlalchemy.orm import Session
from fastapi import HTTPException
from datetime import datetime
from .. import models, schemas


def get_post_by_id(post_id: str, db: Session) -> models.Post:
    record = db.query(models.Post).filter(models.Post.id == post_id).first()
    if not record:
        raise HTTPException(status_code=404, detail="Not Found") 
    record.id = str(record.id)
    return record

``` 

Ici on peut définir une méthode qui nous permet de récupérer un post grâce à son identifiant unique. 
On peut en définir un second qui permet de créer un post grace aux données fournies en entrée.
在这里，我们可以定义一个方法，使我们能够通过其独特的标识符来检索一个帖子。我们可以定义第二个方法，让我们根据提供的输入数据创建一个帖子。

```python
from typing import List

from sqlalchemy.orm import Session
from fastapi import HTTPException
from datetime import datetime
from .. import models, schemas

def create_post(db: Session, post: schemas.Post) -> models.Post:
    record = db.query(models.Post).filter(models.Post.id == post.id).first()
    if record:
        raise HTTPException(status_code=409, detail="Already exists")
    db_post = models.Post(**post.dict())
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    db_post.id = str(db_post.id)
    return db_post

```

On peut remarquer qu'ici l'entrée du service sera le schéma du Post envoyé par l'utilisateur. Ici le service récupère donc un objet Post déjà validé, propre et prêt à être utilisé. 
请注意，这里对服务的输入将是用户发送的Post的模式。在这里，服务得到一个已经验证过的、干净的、可以使用的Post对象。


### Headers

Les headers sont des informations complémentaires envoyés par le protocol http. Votre navigateur envoie des informations au serveur du site duquel vous essayez d'accéder.  Si vous allez dans la console de Google Chrome et que vous allez dans l'onglet Network vous pouvez choisir une requête réalisée par votre navigateur. Vous pouvez ensuite regarder dans les headers, vous verez que Chrome envoie un nombre incalculable d'autres informations. Cela permet au site de réagir de la meilleure manière.

Pour récupérer ces headers dans FastAPI c'est très simple, vous ajoutez un paramètre à la  fonction de votre route. FastAPI va se charger d'aller chercher ce header directement pour vous.  

头信息是由http协议发送的额外信息。你的浏览器会向你试图访问的网站的服务器发送信息。如果你进入谷歌浏览器控制台，进入网络标签，你可以选择浏览器提出的请求。然后你可以看一下标题，你会发现Chrome浏览器发送了很多其他信息。这使网站能够以最佳方式作出反应。

在FastAPI中检索这些头文件非常简单，你在你的路由函数中添加一个参数。FastAPI将直接为你获取这个头。


```python

@app.get("/api/headers")
def read_headers(x_userinfo: Optional[str] = Header(None), ):
    pass
```

Souvent les headers possèdent des tirets, pour que Python puisse utiliser cette variable il faut juste lui préciser de transformer ces tirets en underscores.
通常标题中都有破折号，所以为了让Python使用这个变量，你只需要告诉它把这些破折号变成下划线。

```python

@app.get("/api/headers")
def read_headers(x_userinfo: Optional[str] = Header(None,  convert_underscores=True), ):
    pass
```

### Les codes HTTP
#### Les succés
- 200 : OK - Requête traitée avec succès. La réponse dépendra de la méthode de requête utilisée. 
- 201 : CREATED - Requête traitée avec succès et création d’un document.
- 202 : ACCEPTED - Requête traitée, mais sans garantie de résultat.

Ces codes de succès peuvent être utilisés dans plusieurs cas différents. Pour la création d'un objet, sa mise à jour ou même le succès de sa suppression. 
Ces codes sont là pour communiquer de façon simple avec l'exterieur, ils permettent de savoir très rapidement si l'action qui vient d'être demandé à été exécuté avec succès. 

- 200: OK - 请求成功处理。响应将取决于所使用的请求方法。
- 201: CREATED - 请求成功处理，创建了一个文件。
- 202: ACCEPTED - 请求已处理，但不保证有结果。

这些成功代码可以在几种不同的情况下使用。对于一个对象的创建，它的更新，甚至它的成功删除。
这些代码的存在是为了以简单的方式与外界沟通，它们使人们能够很快知道刚刚被要求的行动是否成功执行。

#### Les erreurs
	
- 400 : Bad Request - La syntaxe de la requête est erronée.
Par exemple il manque des données dans le formulaire, le schéma après sa validation va renvoyer directement une erreur 400 car les données sont éronées. 
- 401 : Unauthorized - Une authentification est nécessaire pour accéder à la ressource.
Si l'utilisateur essaye d'accéder à une ressource sans être connecté. 
- 402 : Payment Required - Paiement requis pour accéder à la ressource.
Si l'utilisateur essaye d'accéder à une ressource payant de votre application
- 403 : Forbidden - Le serveur a compris la requête, mais refuse de l'exécuter.
Si l'utilisateur essaye d'accéder à une ressource qu'il n'a pas le droit de modifier ou de consulter.
- 404 : Not Found -	Ressource non trouvée.
Cette erreur est la plus connue, elle permet de déterminer qu'une ressource n'est pas disponible, cela peut arriver pour plusieurs raisons. La page demandée n'existe pas ou à été supprimée, l'item demandé peut être en rupture ou plus disponible sur un site e-commerce.  
- 405 : Method Not Allowed - Méthode de requête non autorisée. 
Quand on essaye de réaliser une méthode spécifique qui n'est pas autorisée. Par exemple un DELETE sur une route qui n'accepte que les GET ou les POST, le serveur renverra une erreur 405. Le serveur accepte les demandes à cette adresse mais pas ce type de demandes. 
- 408 :	Request Time-out - Temps d’attente d’une requête du client, écoulé côté serveur.
- 409 : Conflict - La requête ne peut être traitée en l’état actuel. 
Ces erreurs peuvent survenir quand un item existe déjà par exemple. 

Avec FastAPI c'est très simple de renvoyer une erreur spécifique en fonction de ce que l'on souhaite communiquer. Il suffit de raise une erreur Python avec le code et le détail. 

- 400: 错误的请求 - 请求的语法是错误的。
例如，表单缺少数据，模式在验证后会返回一个400错误，因为数据是错误的。
- 401: 未授权 - 访问该资源需要认证。
如果用户试图在没有登录的情况下访问一个资源。
- 402: 需要付款 - 访问该资源需要付款。
如果用户试图访问你的应用程序中的一个付费资源
- 403: 禁止 - 服务器已理解该请求，但拒绝执行该请求。
如果用户试图访问一个他们无权修改或查看的资源。
- 404: 未找到 - 未找到资源。
这个错误是最常见的，它确定一个资源是不可用的，这可能发生在几个原因。所请求的页面不存在或已被删除，所请求的项目可能已经缺货或在电子商务网站上不再有。 
- 405: 不允许使用的方法。
当试图执行一个不允许的特定方法时。例如，在一个只接受GET或POST的路由上进行DELETE，服务器将返回一个405错误。服务器接受对这个地址的请求，但不接受这种类型的请求。
- 408: 请求超时 - 来自客户端的请求在服务器端经过了多少时间。
- 409: 冲突 - 该请求在其当前状态下无法被处理。
例如，当一个项目已经存在时，就会出现这些错误。

使用FastAPI，根据你想交流的内容，很容易返回一个特定的错误。只要提出一个带有代码和细节的Python错误。

```python
from fastapi import HTTPException

already_exists = True 

if already_exists:
    raise HTTPException(status_code=409, detail="Already exists")
else:
    raise HTTPException(status_code=404, detail="Not Found")
```

https://fastapi.tiangolo.com/tutorial/handling-errors/

### Middlewares

https://fastapi.tiangolo.com/tutorial/middleware/

Les Middlewares sont des briques logicielles utilisées pour effectuer des opérations en entrée ou en sortie de l'API. Ils permettent de gérer les erreurs, de gérer l'authentification des utilisateurs, d'empecher des intrusions. 

### Background Tasks

https://fastapi.tiangolo.com/tutorial/background-tasks/
Les backgrounds tasks permettent de réaliser des tâches gourmandes en ressources qui peuvent attendre.