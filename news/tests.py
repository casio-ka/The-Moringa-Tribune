from django.test import TestCase
from .models import Editor, Article, tags

# Create your tests here
class TestEditor(TestCase):
    def setUP(self):
        self.editor = Editor(1, 'Wainaia', 'Syoks', 'syoks@gmail.com', 1111111111 )

        def test_save_editor(self):
            self.editor.save_editor()
            q_object =Editor.objects.get(first_name='Wainaina')
            self.assertEqual(q_object.first_name, 'Wainaina')
        
        def test_delete_delete_editor(self):
            self.editor.delete_editor()
            q_object =Editor.objects.all()
            self.assertEqual(len(q_object),0)

        

class TestArticle(TestCase):
    pass