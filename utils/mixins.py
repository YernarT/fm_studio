from django.contrib.auth.decorators import login_required

class LoginRequiredMixin:
    @classmethod
    def as_view(cls, **initkwargs):
        # Call the as_view of the parent class
        view = super(LoginRequiredMixin, cls).as_view(**initkwargs)

        return login_required(view)
