class Magazine:
    _magazines_table = []

    def __init__(self, id, name, category):
        self.id = id
        self.name = name
        self.category = category
        self.__class__._magazines_table.append({
            "id": self.id, "name": self.name, "category": self.category
        })

    @property
    def articles(self):
        associated_articles = [article for article in associated_articles._articles_table if article["magazine_id"] == self.id]
        return associated_articles

    @property
    def contributors(self):
        associated_articles = self.articles
        contributors = []
        for article in associated_articles:
            for author in author._authors_table:
                if author["id"] == article["author_id"]:
                    contributors.append(author)
        return contributors

    def article_titles(self):
        associated_articles = self.articles
        if not associated_articles:
            return None
        titles = [article["title"] for article in associated_articles]
        return titles

    def contributing_authors(self):
        associated_articles = self.articles
        if not associated_articles:
            return None

        author_article_count = {}
        for article in associated_articles:
            author_id = article["author_id"]
            if author_id not in author_article_count:
                author_article_count[author_id] = 0
            author_article_count[author_id] += 1

        contributing_authors = []
        for author_id, count in author_article_count.items():
            if count > 2:
                for author in author._authors_table:
                    if author["id"] == author_id:
                        contributing_authors.append(author)

        if not contributing_authors:
            return None

        return contributing_authors

    def __repr__(self):
        return f'<Magazine {self.name}, Category: {self.category}>'
