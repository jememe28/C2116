import requests

response_text = "<span>$123.45</span><span>$678.90</span>"

response_parts = response_text.split("<span>")

res_parse_list = []

for part in response_parts:
    if part.startswith("$"):
        value = part.split("</span>")[0]
        res_parse_list.append(value)
bitechin_exchange_rate = res_parse_list[0] if res_parse_list else None

print(bitechin_exchange_rate)