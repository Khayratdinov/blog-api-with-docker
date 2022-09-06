import pytest
from django.core.files.uploadedfile import SimpleUploadedFile
from apps.post.models import Blog, Category
from apps.users.models import User


@pytest.mark.django_db
def test_movie_model():
    user = User.objects.create(
                               username="Pistonshi",
                               email="pistonshi@mail.ru",
                               first_name="Pistonshi",
                               last_name="Palonshi",
                               confirmation_code="12345",
                               bio="Bu Pistonshi haqqida malumot",
                               )
    category = Category.objects.create(
                                       title="Programming",
                                       sub_title="Python Django",               
    )
    blog = Blog(
                 title="Bu test ushin blog title",
                 description="Bu description",
                 body="Bu toliq malumot",
                 author=user,
                 images="",
                 category=category,
                 )
    blog.save()
    assert blog.title == "Bu test ushin blog title"
    assert blog.description == "Bu description"
    assert blog.body == "Bu toliq malumot"
    assert blog.author == user
    assert blog.images == ""
    assert blog.category == category
    assert blog.data_pub
    assert blog.last_update
    assert str(blog) == blog.title