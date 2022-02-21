from service.Validatefunction import validateParams
from service.main.redirect import redirectToLink
from swaggerConfig import api
from flask_restx import reqparse, Resource
from flask import redirect, request


main = api.namespace("/", description="Main API")
main_query_model = reqparse.RequestParser()
main_query_model.add_argument("link", type=str, required=True, help="Query", location="args")

@main.route("/")
class MoviePopular(Resource):
    @api.doc(responses={200: "OK"})
    @api.expect(main_query_model)
    def get(self):
        requestObj = validateParams(request.args, ["link"])
        output = redirectToLink(requestObj)
        return redirect(output)
