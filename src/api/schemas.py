from marshmallow import Schema, fields


class DataSchema(Schema):
    firstName = fields.String(required=True)
    secondName = fields.String(required=True)
    ageInYears = fields.Integer(required=True)
    address = fields.String(required=True)
    creditScore = fields.Float(required=True)


data_schema = DataSchema()
