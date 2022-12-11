from django.shortcuts import redirect


class AccountOwnerRequiredMixin(object):
    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.username != self.request.user.username:
            return redirect('index')
        return super().dispatch(request, *args, **kwargs)


class PostAuthorRequiredMixin(object):
    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.user != self.request.user and not self.request.user.is_superuser:
            return redirect('index')
        return super().dispatch(request, *args, **kwargs)
