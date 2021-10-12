from typing import Any
from abc import abstractmethod
from dataclasses import dataclass


@dataclass(frozen=True)
class HttpResponse:
    body: Any
    status: int


class Middleware:
    @abstractmethod
    async def perform(self, request: Any) -> HttpResponse:
        raise NotImplementedError

    async def handle(self, request: Any) -> HttpResponse:
        try:
            return await self.perform(request)
        except Exception as e:
            return self.server_error(e)

    def ok(self, data) -> HttpResponse:
        return HttpResponse(data, status=200)

    def forbidden(self) -> HttpResponse:
        return HttpResponse(dict(message="Access Denied"), 403)

    def no_content(self) -> HttpResponse:
        return HttpResponse("", 204)

    def server_error(self, err: Exception) -> HttpResponse:
        return HttpResponse(err, status=500)

    def bad_request(self, err: Exception) -> HttpResponse:
        return HttpResponse(err, status=400)
