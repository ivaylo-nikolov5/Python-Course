from project.category import Category
from project.document import Document
from project.topic import Topic


class Storage:
    def __init__(self):
        self.categories = []
        self.topics = []
        self.documents = []

    def add_category(self, category: Category):
        if category not in self.categories:
            self.categories.append(category)

    def add_topic(self, topic: Topic):
        if topic not in self.topics:
            self.topics.append(topic)

    def add_document(self, document: Document):
        if document not in self.documents:
            self.documents.append(document)

    def edit_category(self, category_id: int, new_name: str):
        category = self.find_by_id(category_id, self.categories)
        category.edit(new_name)

    def edit_topic(self, topic_id: int, new_topic: str, new_storage_folder: str):
        topic = self.find_by_id(topic_id, self.topics)
        topic.edit(new_topic, new_storage_folder)

    def edit_document(self, document_id: int, new_file_name: str):
        document = self.find_by_id(document_id, self.documents)
        document.edit(new_file_name)

    def delete_category(self, category_id):
        category = self.find_by_id(category_id, self.categories)
        self.categories.remove(category)

    def delete_topic(self, topic_id):
        topic = self.find_by_id(topic_id, self.topics)
        self.topics.remove(topic)

    def delete_document(self, document_id):
        document = self.find_by_id(document_id, self.documents)
        self.documents.remove(document)

    def get_document(self, document_id):
        document = self.find_by_id(document_id, self.documents)
        return document

    def __repr__(self):
        result = "\n".join(repr(doc) for doc in self.documents)
        return result

    @staticmethod
    def find_by_id(id, place):
        for item in place:
            if item.id == id:
                return item
