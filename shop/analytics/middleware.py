from analytics.models import PageView


class PageViewMiddleware:
    """Records one PageView for every successful HTML page served."""

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        if (
            request.method == "GET"
            and response.status_code == 200
            and response.get("Content-Type", "").startswith("text/html")
        ):
            PageView.objects.create(
                path=request.path[:512],
                user_id=request.user.id if request.user.is_authenticated else None,
                session_key=request.session.session_key or "",
                referrer=request.META.get("HTTP_REFERER", "")[:512],
            )
        return response
