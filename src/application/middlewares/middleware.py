from typing import Any
from abc import abstractmethod
from dataclasses import dataclass


@dataclass(frozen=True)
class HttpResponse:
    body: Any
    status: int


class Middleware:
    @abstractmethod
    async def handle(self, request: Any) -> HttpResponse:
        raise NotImplementedError

    def ok(self, data) -> HttpResponse:
        return HttpResponse(data, status=200)

    def forbidden(self, e: Exception) -> HttpResponse:
        return HttpResponse(e, 403)

    def no_content(self) -> HttpResponse:
        return HttpResponse("", 204)

    def server_error(self, err: Exception) -> HttpResponse:
        return HttpResponse(err, status=500)

    def bad_request(self, err: Exception) -> HttpResponse:
        return HttpResponse(err, status=400)
