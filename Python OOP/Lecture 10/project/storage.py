from project.category import Category
from project.document import Document
from project.topic import Topic


class Storage:
    def __init__(self):
        self.categories = []
        self.topics = []
        self.documents = []

    def add_category(self, category: Category):
        self.__add_entity(self.categories, category)

    def add_topic(self, topic: Topic):
        self.__add_entity(self.topics, topic)

    def add_document(self, document: Document):
        self.__add_entity(self.documents, document)

    def edit_category(self, category_id: int, new_name:str):
        category = self.__edit_entity(category_id, self.categories)
        category.edit(new_name)

    def edit_topic(self, topic_id: int, new_topic: str, new_storage_folder: str):
        topic = self.__edit_entity(topic_id, self.topics)
        topic.edit(new_topic, new_storage_folder)

    def edit_document(self, document_id: int, new_file_name: str):
        document = self.__edit_entity(document_id, self.documents)
        document.edit(new_file_name)

    def delete_category(self, category_id):
        category = self.__edit_entity(category_id, self.categories)
        self.categories.remove(category)

    def delete_topic(self, topic_id):
        topic = self.__edit_entity(topic_id, self.topics)
        self.topics.remove(topic)

    def delete_document(self, document_id):
        document = self.__edit_entity(document_id, self.documents)
        self.documents.remove(document)

    def get_document(self, document_id):
        document = self.__edit_entity(document_id, self.documents)
        return document

    def __repr__(self):
        result = ""
        for document in self.documents:
            result += f"{repr(document)}\n"
        return result

    def __add_entity(self, entities, entity):
        if entity not in entities:
            entities.append(entity)

    def __edit_entity(self, entity_id, entities):
        for entity in entities:
            if entity.id == entity_id:
                return entity

