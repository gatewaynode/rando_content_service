# from wagtail.api.v2.endpoints import PagesAPIEndpoint
from wagtail.api.v2.views import PagesAPIViewSet
# next unchanged
from wagtail.api.v2.router import WagtailAPIRouter
#from wagtail.images.api.v2.endpoints import ImagesAPIEndpoint
from wagtail.images.api.v2.views import ImagesAPIViewSet
#from wagtail.documents.api.v2.endpoints import DocumentsAPIEndpoint
from wagtail.documents.api.v2.views import DocumentsAPIViewSet

# Init
api_router = WagtailAPIRouter("wagtailapi")

# Router
api_router.register_endpoint('pages', PagesAPIViewSet)
api_router.register_endpoint('images', ImagesAPIViewSet)
api_router.register_endpoint('documents', DocumentsAPIViewSet)
