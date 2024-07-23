# TencentBlueKing is pleased to support the open source community by making
# 蓝鲸智云 - PaaS 平台 (BlueKing - PaaS System) available.
# Copyright (C) 2017 THL A29 Limited, a Tencent company. All rights reserved.
# Licensed under the MIT License (the "License"); you may not use this file except
# in compliance with the License. You may obtain a copy of the License at
#
#     http://opensource.org/licenses/MIT
#
# Unless required by applicable law or agreed to in writing, software distributed under
# the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND,
# either express or implied. See the License for the specific language governing permissions and
# limitations under the License.
#
# We undertake not to change the open source license (MIT license) applicable
# to the current version of the project delivered to anyone in the future.
from setuptools import setup, find_packages

about = {}
with open("readme.md") as f:
    readme = f.read()

requires = [
    "grpcio>=1.60.0",
    "typing-extensions>=4.9.0",
    "protobuf>=4.25.2",
]

extras_dev_require = [
    "grpcio-tools>=1.60.0",
    "ruff>=0.1.13",
    "pytest>=7.4.4",
    "mypy>=0.910",
]

setup(
    name="bscp-python-sdk",
    packages=find_packages(),
    install_requires=requires,
    extras_require={
        "dev": extras_dev_require,
    },
    zip_safe=True,
    version="0.2.0",
    description="The Python SDK for blueking bscp project.",
    long_description=readme,
    long_description_content_type="text/markdown",
    author="blueking",
    author_email="blueking@tencent.com",
    url="https://github.com/TencentBlueKing/bscp-python-sdk",
    keywords=["python", "bscp"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
    ],
    python_requires=">=3.8",
)
