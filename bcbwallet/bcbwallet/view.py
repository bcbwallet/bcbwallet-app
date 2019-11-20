from django.http import HttpResponse
import json


def bcbpay(request):

    res = {
        "ver": 3,
        "appUISeg": {
            "title": "通用支付",
            "value": "0.1",
            "affCode": "",
            "referInfo": "进行支付操作",
            "defaultPayAddr": "",
            "symbol": "BCB"
        },
        "coinParams": {
            "note": "备注",
            "gasLimit": "25000",
            "calls": [
                {
                    "contract": "bcbLVgb3odTfKC9Y9GeFnNWL9wmR4pwWiqwe",
                    "method": "Transfer(types.Address,bn.Number)",
                    "params": [
                        "bcbL8BzfVfcxtqh9umN3dUhxBYNyEnV7GiSa",
                        "100000000"
                    ]
                }
            ]
        }
    }

    print(json.dumps(res))
    return HttpResponse(json.dumps(res))
