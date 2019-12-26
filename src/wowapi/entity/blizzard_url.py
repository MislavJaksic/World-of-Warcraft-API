import re


class BlizzardUrl(object):
    def __init__(self, region, api_path, namespace_type, locale_type="en_GB"):
        self.region = region
        self.api_path = api_path
        self.namespace_type = namespace_type

        uri = f"{region}.api.blizzard.com{api_path}"
        namespace = f"?namespace={namespace_type}-{region}"
        locale = f"locale={locale_type}"
        self.url = f"https://{uri}{namespace}&{locale}"

    def __str__(self):
        return self.url


def string_to_url(string):
    m = re.match(r"https://(?P<region>\w+).api.blizzard.com(?P<api_path>[-/\w]+)\?namespace=(?P<namespace_type>\w+)", string)
    dict = m.groupdict()
    region = dict["region"]
    api_path = dict["api_path"]
    namespace_type = dict["namespace_type"]
    return BlizzardUrl(region, api_path, namespace_type)
