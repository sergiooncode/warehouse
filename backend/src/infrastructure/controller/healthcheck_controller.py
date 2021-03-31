from http import HTTPStatus

from flask_restx import Resource

from config.urls import HEALTH_CHECK
from src.infrastructure.controller.base import api


@api.route(HEALTH_CHECK)
class HealthCheckController(Resource):
    def get(self):
        return dict(
            status_code=HTTPStatus.OK,
            message="Warehouse API - Health Check",
        )
