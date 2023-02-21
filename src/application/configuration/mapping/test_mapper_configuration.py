from automapper import mapper

from domain.dto.list_test_dto import ListTestDto
from domain.model.list_test import ListTest


def test_mapper_config():
    mapper.add(ListTestDto, ListTest, fields_mapping={
               "company": "ListTestDto.enterprise"})
