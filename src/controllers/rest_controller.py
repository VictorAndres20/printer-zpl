from src.request.response import Response


class RestController:

    @staticmethod
    def build_ok_response() -> Response:
        return Response(ok=True, message='Process Finished')

    @staticmethod
    def build_ok_response_with_data(data) -> Response:
        return Response(ok=True, message='Process Finished', data=data)

    @staticmethod
    def build_error_response(error: str) -> Response:
        return Response(ok=False, error=error)
