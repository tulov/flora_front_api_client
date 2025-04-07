import marshmallow_dataclass
from flora_front_api_client.presentations.products import (
    ProductResponse,
    ProductRequest,
    ProductsResponse,
    FeaturedProductsResponse,
    FeaturedProductsQuerystring,
    PreferredExecutorResponse,
    PreferredExecutorQuerystring,
    SuccessFeaturedProductsResponse,
    IdsFeaturedProductsQuerystring,
    Product,
    FeaturedProduct,
    FeaturedProductExecutor,
    DeliveryTimePeriodResponse,
    DeliveryTimePeriodRequest,
    CityWithProductCntResponse,
    FeaturedProductResponse,
)
from marshmallow import Schema, EXCLUDE

Schema.Meta.unknown = EXCLUDE


ProductResponseSchema = marshmallow_dataclass.class_schema(ProductResponse)
ProductsResponseSchema = marshmallow_dataclass.class_schema(ProductsResponse)
ProductRequestSchema = marshmallow_dataclass.class_schema(ProductRequest)
FeaturedProductsResponseSchema = marshmallow_dataclass.class_schema(
    FeaturedProductsResponse
)
CityWithProductCntResponseSchema = marshmallow_dataclass.class_schema(
    CityWithProductCntResponse
)
FeaturedProductsQuerystringSchema = marshmallow_dataclass.class_schema(
    FeaturedProductsQuerystring
)

PreferredExecutorResponseSchema = marshmallow_dataclass.class_schema(
    PreferredExecutorResponse
)

PreferredExecutorQuerystringSchema = marshmallow_dataclass.class_schema(
    PreferredExecutorQuerystring
)

SuccessFeaturedProductsResponseSchema = marshmallow_dataclass.class_schema(
    SuccessFeaturedProductsResponse
)


FeaturedProductResponseSchema = marshmallow_dataclass.class_schema(
    FeaturedProductResponse
)


IdsFeaturedProductsQuerystringSchema = marshmallow_dataclass.class_schema(
    IdsFeaturedProductsQuerystring
)

ProductSchema = marshmallow_dataclass.class_schema(Product)

FeaturedProductSchema = marshmallow_dataclass.class_schema(FeaturedProduct)

FeaturedProductExecutorSchema = marshmallow_dataclass.class_schema(
    FeaturedProductExecutor
)
DeliveryTimePeriodResponseSchema = marshmallow_dataclass.class_schema(
    DeliveryTimePeriodResponse
)
DeliveryTimePeriodRequestSchema = marshmallow_dataclass.class_schema(
    DeliveryTimePeriodRequest
)
