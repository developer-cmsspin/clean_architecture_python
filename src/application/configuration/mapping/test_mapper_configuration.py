from automapper import mapper

from src.domain.dto.test_dto import TestDto
from src.domain.model.test import Test


def test_mapper_config():
    mapper.add(TestDto, Test, fields_mapping={
               "company": "TestDto.enterprise"})

    mapper.add(Test, TestDto, fields_mapping={
               "enterprise": "Test.company"})
