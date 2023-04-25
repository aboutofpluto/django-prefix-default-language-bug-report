from django.urls import path
from django.http import HttpResponse
from django.utils.translation import gettext, gettext_lazy
from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from django.urls import translate_url

def about(request):
    content = [gettext("about")]
    for (code, name) in settings.LANGUAGES:
        href = translate_url(request.path, code)
        print(href)
        content.append(
            "<a href='{}'>{}</a>".format(href, name)
        )
    return HttpResponse(" | ".join(content))

urlpatterns = i18n_patterns(
    path(
        gettext_lazy("about/"),
        about,
        name="about",
    ),
    prefix_default_language=False,
)
