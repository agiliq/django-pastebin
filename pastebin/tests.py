from django.test import TestCase, Client

from pastebin.models import CodePaste

class TestViews(TestCase):
	def setUp(self):
		self.c = Client()
		self.paste = CodePaste.objects.create(
			title = "Hello",
			text = "Hello World",
			language = "Text",

			)


	def test_index(self):
		resp = self.c.get("/")
		self.assertEqual(200, resp.status_code)

	def test_paste_detail(self):
		resp = self.c.get("/paste/%s/"%self.paste.pk)
		self.assertEqual(200, resp.status_code)
		self.assertContains(resp, "Hello World")

	def test_create_post(self):
		old_count = CodePaste.objects.count()
		resp = self.c.post("/", 
			{
			"text": "Hello World",
			"name": "Foo"
			},
			follow=True
			)
		self.assertContains(resp, "Hello World")
		self.assertEqual(old_count+1, CodePaste.objects.count())


