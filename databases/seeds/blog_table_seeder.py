"""BlogTableSeeder Seeder."""

from masoniteorm.seeds import Seeder
from app.Blog import Blog


class BlogTableSeeder(Seeder):
    def run(self):
        Blog.create({"subject": "sports cars", "details": "drivind fast"})
        Blog.create({"subject": "family", "details": "fun of hanging with family"})
        Blog.create({"subject": "dinner", "details": "types of dinners"})