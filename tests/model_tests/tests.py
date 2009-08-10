from models import Article, ArticleCreator, ArticleEditor
from django.contrib.auth.models import User
from threaded_multihost.threadlocals import get_current_user, set_current_user

__test__ = {'API_TESTS': """

>>> a = Article(text="Look at me any user")
>>> a.save()
>>> a.user is None
True

>>> u = User(username='user')
>>> u.save()
>>> a.user = u
>>> a.save()
>>> a.user is None
False

>>> a.user.pk == u.pk
True

>>> a.user
<User: user>

>>> u = User(username='creator')
>>> u.save()
>>> set_current_user(u)
>>> b = ArticleCreator(text="Look at me creator")
>>> b.save()
>>> b.user.pk == u.pk
True
>>> b.user
<User: creator>

>>> b = ArticleCreator.objects.get(pk=b.pk)
>>> b.user.pk == u.pk
True
>>> b.user
<User: creator>

>>> c = ArticleEditor(text="Look at me editor")
>>> c.save()
>>> c.user.pk == u.pk
True
>>> c.user
<User: creator>

>>> u = User(username='editor')
>>> u.save()
>>> set_current_user(u)
>>> c.text = "Changed from editor"
>>> c.save()
>>> c.user.pk == u.pk
True
>>> c.user
<User: editor>

>>> c = ArticleEditor.objects.get(pk=c.pk)
>>> c.user.pk == u.pk
True
>>> c.user
<User: editor>

"""}
