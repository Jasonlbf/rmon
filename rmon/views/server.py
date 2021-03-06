from flask import request, g
from rmon.common.rest import RestView
from rmon.models import Server, ServerSchema

class ServerList(RestView):
    def get(self):
        servers = Server.query.all()
        return ServerSchema().dump(servers,many=True).data

    def post(self):
        data = request.get_json()
        server, erros = ServerSchema().load(data)
        if errors:
            return errors, 400
        server.ping()
        server.save()
        return('ok':True},201

class ServerDetail(RestView):

    method_decorators = (ObjectMustBeExist(server),)

    def get(self,object_id):
        data, _ = ServerSchema().dump(g.instance)
        return data

    def put(self,object_id):
        schema = ServerSchema(context={'instance':g.instance})
        data = request.get_json()
        server, errors = schema.load(data,partial=True)
        if errors:
            return errors,400
        server.save()
        return {'ok':True}

    def delete(self,object_id):
        g.instance.delete()
        return {'ok':True}, 204
