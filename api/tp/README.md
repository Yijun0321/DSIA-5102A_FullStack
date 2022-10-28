# Tp API

Le but de ce TP est d'utiliser tout ce que vous avez vu en cours pour créer votre propre API.
## Exercices

1. Ajouter une route permettant de renvoyer la date actuelle
2. Créer un schéma d'un objet de votre choix
3. Ajouter le branchement avec la base de données.
4. Ajouter le modèle SQLAlchemy
5. Ajouter les routes CRUDs permettant de créer, modifier, supprimer un objet de votre choix
6. Créer des services permettant de réaliser toutes ces opérations
7. Remplacer le code dans les routes pour utiliser directement les services
8. Ajouter une route permettant de lire un header, realiser une requête sur votre API via votre navigateur préféré et renvoyer le header correspondant
 
1. 添加一条返回当前日期的路线
见fullstack-data-application\api\tp\app\main.py，线路/date1 和 /date2
2. 创建一个你选择的对象的模式
见fullstack-data-application\api\tp\app\main.py，线路/user
3. 添加到数据库的连接。

4. 添加SQLAlchemy模型
5. 添加CRUDs路线来创建、修改、删除你选择的对象
6. 创建服务来执行所有这些操作
7. 替换路线中的代码以直接使用服务
8. 添加一个路由来读取一个头，通过你喜欢的浏览器向你的API提出请求，并返回相应的头。

- 启动API：
docker-compose up -d

- 重启API：
docker-compose restart
