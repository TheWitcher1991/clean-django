from rest_framework import generics, mixins, viewsets
from rest_framework.permissions import IsAuthenticated

from clean_django.shared.framework.mixins import AllowAnyMixin


class APIController(generics.GenericAPIView):
    pass


class APISetController(viewsets.ViewSetMixin, generics.GenericAPIView):
    pass


class AnonymousController(AllowAnyMixin, APIController):
    pass


class BaseController(APIController):
    permission_classes = (IsAuthenticated,)
    permission_types = ()


class BaseSetController(APISetController):
    permission_classes = (IsAuthenticated,)
    permission_types = ()


class ReadOnlyModelSetController(mixins.RetrieveModelMixin, mixins.ListModelMixin, BaseSetController):
    pass


class ModelSetBaseSetController(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    mixins.ListModelMixin,
    BaseSetController,
):
    pass


class CreateController(mixins.CreateModelMixin, BaseController):
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class ListController(mixins.ListModelMixin, BaseController):
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class RetrieveController(mixins.RetrieveModelMixin, BaseController):
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)


class DestroyController(mixins.DestroyModelMixin, BaseController):
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class UpdateController(mixins.UpdateModelMixin, BaseController):
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)


class ListCreateController(mixins.ListModelMixin, mixins.CreateModelMixin, BaseController):
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class RetrieveUpdateController(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, BaseController):
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)


class RetrieveDestroyController(mixins.RetrieveModelMixin, mixins.DestroyModelMixin, BaseController):
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


class RetrieveUpdateDestroyController(
    mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, BaseController
):
    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
