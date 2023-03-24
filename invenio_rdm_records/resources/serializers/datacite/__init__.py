# -*- coding: utf-8 -*-
#
# Copyright (C) 2021 CERN.
#
# Invenio-RDM-Records is free software; you can redistribute it and/or modify
# it under the terms of the MIT License; see LICENSE file for more details.

"""DataCite Serializers for Invenio RDM Records."""
from datacite import schema43
from flask_resources import BaseListSchema, MarshmallowSerializer
from flask_resources.serializers import JSONSerializer, SimpleSerializer

from invenio_rdm_records.contrib.journal.custom_fields import JournalDataciteDumper

from .schema import DataCite43Schema

# Order matters
datacite_dump_dumpers = [JournalDataciteDumper()]


class DataCite43JSONSerializer(MarshmallowSerializer):
    """Marshmallow based DataCite serializer for records."""

    def __init__(self, **options):
        """Constructor."""
        super().__init__(
            format_serializer_cls=JSONSerializer,
            object_schema_cls=DataCite43Schema,
            list_schema_cls=BaseListSchema,
            schema_kwargs={"dumpers": datacite_dump_dumpers},
            **options
        )


class DataCite43XMLSerializer(MarshmallowSerializer):
    """JSON based DataCite XML serializer for records."""

    def __init__(self, **options):
        """Constructor."""
        encoder = options.get("encoder", schema43.tostring)
        super().__init__(
            format_serializer_cls=SimpleSerializer,
            object_schema_cls=DataCite43Schema,
            list_schema_cls=BaseListSchema,
            schema_kwargs={"dumpers": datacite_dump_dumpers},
            encoder=encoder,
        )
