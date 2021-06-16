from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from .models import Tv


class TVTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="tester", email="tester@email.com", password="pass"
        )

        self.tv = Tv.objects.create(
            brand="test tv", size='43 inch', purchaser=self.user,
        )

    def test_string_representation(self):
        self.assertEqual(str(self.tv), "test tv")

    def test_tv_content(self):
        self.assertEqual(f"{self.tv.brand}", "test tv")
        self.assertEqual(f"{self.tv.purchaser}", "tester@email.com")
        self.assertEqual(self.tv.size, '43 inch')

    def test_tv_list_view(self):
        response = self.client.get(reverse("tv_list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "test tv")
        self.assertTemplateUsed(response, "tv/tv-list.html")

    def test_tv_detail_view(self):
        response = self.client.get(reverse("tv_detail", args="1"))
        no_response = self.client.get("/100000/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(no_response.status_code, 404)
        self.assertContains(response, "Purchaser: tester")
        self.assertTemplateUsed(response, "tv/tv-detail.html")

    def test_tv_create_view(self):
        response = self.client.post(
            reverse("tv_create"),
            {
                "brand": "aiwa",
                "size": "55 inch",
                "purchaser": self.user.id,
            }, follow=True
        )

        self.assertRedirects(response, reverse("tv_detail", args="2"))



    def test_tv_update_view_redirect(self):
        response = self.client.post(
            reverse("tv_update", args="1"),
            {"brand": "Updated brand","size":"65 inch","purchaser":self.user.id}
        )

        self.assertRedirects(response, reverse("tv_detail", args="1"))

    def test_tv_delete_view(self):
        response = self.client.get(reverse("tv_delete", args="1"))
        self.assertEqual(response.status_code, 200)