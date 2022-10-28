# Backend

## Pourquoi ?

Pourquoi créer une API

![test](../docs/modern_web_app.png)

## Différents types

- REST
- WebSocket
- GraphQL

### REST
表现层状态转换（英语：Representational State Transfer)

REST est un ensemble de contraintes architecturales. Il ne s'agit ni d'un protocole, ni d'une norme. Les développeurs d'API peuvent mettre en œuvre REST de nombreuses manières.
REST是一套架构上的限制。它既不是一个协议，也不是一个标准。API开发者可以用很多方式实现REST。

Lorsqu'une application émet une requête par le biais d'une API RESTful, celle-ci se charge de partager l'état actuel de la ressource demandée.
Cette information, ou représentation, est fournie via le protocole HTTP souvent au format JSON  (JavaScript Object Notation), cat il ne dépend pas d'un langage et peut être lu aussi bien par les humains que par les machines.
当一个应用程序通过RESTful API发出请求时，API会负责分享所请求资源的当前状态。这种信息或表示法是通过HTTP协议提供的，通常是JSON（JavaScript对象符号）格式，因为它与语言无关，人类和机器都可以读取。

Autre point à retenir : les en-têtes (headers) et paramètres jouent également un rôle majeur dans les d'une requête HTTP d'API REST. Il peuvent contenir de nombreuses informations importantes :
另一点要记住的是，头文件和参数在REST API的HTTP请求中也起着重要作用。它们可以包含很多重要的信息:

- métadonnées
- autorisation
- URI
- mise en cache
- cookies
- etc.
元数据
许可证
URI
缓存
饼干
等。

Il existe des en-têtes de requête et des en-têtes de réponse. Chacun dispose de ses propres informations de connexion HTTP.

Une API RESTful doit remplir les critères suivants :

- Une architecture client-serveur constituée de clients, de serveurs et de ressources, avec des requêtes gérées via HTTP
- Des communications client-serveur stateless, c'est-à-dire que les informations du client ne sont jamais stockées entre les requêtes GET, qui doivent être traitées séparément, de manière totalement indépendante. Le serveur ne doit pas garder de notion d'état ou de statut dans le temps.
- La possibilité de mettre en cache des données afin de rationaliser les interactions client-serveur
- Une interface uniforme entre les composants qui permet un transfert standardisé des informations Cela implique que :
  - les ressources demandées soient identifiables et séparées des représentations envoyées au client ;
  - les ressources puissent être manipulées par le client au moyen de la représentation reçue, qui contient suffisamment d'informations ;
  - les messages autodescriptifs renvoyés au client contiennent assez de détails pour décrire la manière dont celui-ci doit traiter les informations ;
  - l'API possède un hypertexte/hypermédia, qui permet au client d'utiliser des hyperliens pour connaître toutes les autres actions disponibles après avoir accédé à une ressource.
- Un système à couches, invisible pour le client, qui permet de hiérarchiser les différents types de serveurs (pour la sécurité, l'équilibrage de charge, etc.) impliqués dans la récupération des informations demandées

Bien que l'API REST doive répondre à l'ensemble de ces critères, elle est considérée comme étant plus simple à utiliser qu'un protocole tel que SOAP (Simple Object Access Protocol), qui est soumis à des contraintes spécifiques, dont la messagerie XML, la sécurité intégrée et la conformité des transactions, ce qui le rend plus lourd et moins rapide.
尽管REST API必须满足所有这些标准，但它被认为比SOAP（简单对象访问协议）等协议更容易使用，后者受到特定的限制，包括XML消息传递、内置安全和交易合规性，使其更重更慢。

### WebSocket

L'API WebSocket est une technologie évoluée qui permet d'ouvrir un canal de communication bidirectionnelle entre un navigateur (côté client) et un serveur. Avec cette API vous pouvez envoyer des messages à un serveur et recevoir ses réponses de manière événementielle sans avoir à aller consulter le serveur pour obtenir une réponse.
WebSocket API是一种先进的技术，它在浏览器（客户端）和服务器之间打开了一个双向的通信通道。有了这个API，你可以向服务器发送消息，并以事件驱动的方式接收其响应，而不必去服务器上获得响应。

### GraphQL

GraphQL est un langage de requête pour les API  qui permet de répondre à des requêtes sur les données existantes. GraphQL fournit une description complète et compréhensible des données de votre API, donne aux clients le pouvoir de demander exactement ce dont ils ont besoin et rien de plus. GraphQL permet aussi de faciliter l'évolution des APIs au fil du temps.
GraphQL是一种用于API的查询语言，允许你回答对现有数据的查询。GraphQL为你的API中的数据提供了完整的、可理解的描述，使客户能够准确地要求他们所需要的东西，而不是其他。GraphQL也使得随着时间的推移，API的发展变得容易。

## Les frameworks

Les frameworks sont des outils, ou plutôt des environnements logiciels utilisés pour faciliter et accélérer le développement de certaines briques. Ici nous verrons plusieurs framework web permettant aux developpeurs de créer des API ou des applications Web très facilement sans avoir besoin de tout recoder à la main. Ces frameworks sont souvent accompagnés de modules développés par la communauté et disponible très facilement.
Nous allons voir quelques frameworks les plus connus et ensuite nous concentrer sur celui que nous allons détailler dans le cours : FastAPI.
框架是工具，或者说是软件环境，用于促进和加速某些砖块的开发。在这里，我们将看到几个网络框架，允许开发人员非常容易地创建API或网络应用，而不必手工重新编码一切。这些框架往往伴随着社区开发的模块，而且非常容易获得。
我们将看看一些最流行的框架，然后集中讨论我们将在课程中详细讨论的一个框架：FastAPI。

### Django

Django est un framework python Open Source permettant de créer des API et des sites web. Il a été initialement développé par Adrian Holovaty et Simon Willison en 2003. Django est basé sur le pattern Model Vue Template.
Django est très populaire dans les entreprises pour sa robustesse et sa complétude. Il est utilisé par de nombreux géants américains comme Instagram ou  Youtube mais aussi par de nombreuses entreprises françaises comme Drivy, Blablacar ou encore Deezer.
Django是一个开源的python框架，用于构建API和网站。它最初是由Adrian Holovaty和Simon Willison在2003年开发的。Django是基于Model Vue Template模式的。
Django因其稳健性和完整性在企业中非常受欢迎。许多美国巨头，如Instagram或Youtube，以及许多法国公司，如Drivy、Blablacar或Deezer，都在使用它。

#### Avantages

- La structure d'un projet Django est très complète, très bien découpée et modulaire, cela permet très facilement d'ajouter ou d'enlever des ensembles de fonctionnalités.
- En plus de la partie purement web, Django propose une solution DRF (Django Rest Framework) qui permet assez facilement de générer des APIs. Comme pour la partie web, la partie REST de Django est très modulaire.
- Django propose aussi par défaut une interface de sécurité qui peut protéger les sites web d'injections SQL par exemple.
- Django项目的结构是非常完整的，非常好的分解和模块化，这使得它非常容易添加或删除功能集。
- 除了纯粹的Web部分，Django还提供了一个DRF（Django Rest Framework）解决方案，使得生成API相当容易。至于网络部分，Django的REST部分是非常模块化的。
- Django还默认提供了一个安全接口，可以保护网站免受SQL注入等。

#### Inconvénients

- La complexité de la structure et la grande taille  d'un projet Django peuvent entrainer des lenteurs de développement. L'utilisation des modules nécessite de faire très attention aux non-régressions.
- Django est très peu flexible, il est très dépendant des bases SQL, et ne permet pas facilement d'utiliser d'autres types de stockage. 
- Django项目结构的复杂性和庞大的规模会导致开发缓慢。使用模块需要仔细注意不退步的问题。
- Django不是很灵活，它非常依赖SQL数据库，而且不容易允许使用其他类型的存储。

### Flask

 Flask a été créé par Armin Ronacher, c’ est aussi un framework web écrit en Python, on appelle ça un micro-framework par sa légèreté et sa facilité d'utilisation. Flask permet de développer très facilement et rapidement des applications Web, que ce soit des sites ou des APIs. 
Flask possède une grande communauté et de nombreux packages sont développés par celle-ci. Ces packages permettent de gérer des bases de données, l'authentification, etc.
 Flask是由Armin Ronacher创建的，它也是一个用Python编写的网络框架，它被称为微框架，因为它很轻，很容易使用。Flask允许非常容易和快速地开发网络应用，无论是网站还是API。
Flask有一个庞大的社区，许多软件包都是由它开发的。这些包允许管理数据库、认证等。

#### Avantages

- Flask est très simple à comprendre et permet très facilement même pour des débutants  de créer des applications web sans efforts.
- Flask est flexible, ce qui lui permet, contrairement à Django, de changer et d’itérer très facilement. 
- Flask非常简单易懂，即使是初学者也能非常容易地创建网络应用。
- Flask很灵活，这使得它与Django不同，可以非常容易地改变和迭代。

#### Inconvénients

- Flask utilise de nombreux modules développés par des personnes tiers, ce qui peut engendrer des failles de sécurité. 
- Flask est un framework synchrone qui va dépiler les requêtes les unes après les autres. Cela peut entraîner des longueurs importantes lorsque des opérations sont longues. 
- Flask使用了许多由第三方开发的模块，这可能导致安全漏洞。
- Flask是一个同步框架，会一个接一个地解压请求。当操作时间较长时，这可能会导致运行时间过长。

#### Example

 ```python

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return {"message": "Hello World"}

```

### FasAPI

Fast API est un tout nouveau framework web Python, open source et très performant.
Fast API是一个全新的、开源的、高性能的Python网络框架。

#### Avantages

- Il est basé uniquement sur des standars comme JsonSchema (pour la validation des modèles), OAuth2 (pour l’authentification) ou Open API (pour la définition d’interfaces)
- Fast API met en place des méthodes de validation très poussées.
- FastAPI permet aussi de créer des API GraphQL très facilement. 
- Il permet aussi de générer de la documentation technique automatiquement. 
它完全基于JsonSchema（用于模型验证）、OAuth2（用于认证）或Open API（用于接口定义）等标准。
快速API实现了非常先进的验证方法。
FastAPI还允许你非常容易地创建GraphQL APIs。
它还允许自动生成技术文件。

#### Inconvénients

- La jeunesse de ce nouveau framework fait que la communauté est assez récente et assez jeune. Il existe donc que très peu de cours ou tutoriels.
这个新框架的年轻化意味着社区是相当新的，而且相当年轻。因此，很少有课程或辅导班。

#### Example

```python

from fastapi import FastAPI
app = FastAPI()   
@app.get("/") 
async def root():
     return {"message": "Hello World"}

```

### Tornado

Tornado est aussi un framework web mais aussi une librairie de gestion réseau asynchrone. Tornado permet de gérer un très grand nombre de connexions simultanées, contrairement à Flask par exemple. Tornado est donc utilisé quand on développe des applications très grosses qui ont besoin de grossir très rapidement. 
Tornado也是一个网络框架，但也是一个异步的网络管理库。Tornado允许管理非常多的同时连接，这与Flask等不同。因此，Tornado在开发需要快速增长的非常大的应用程序时被使用。

#### Example 

```python

import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello, world")

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()


```

## [Suite](ARCHITECURE.md)
