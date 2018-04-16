import requests
import sys
import json


class Vep(object):
    def __init__(self):
        self.root_url = "https://rest.ensembl.org"
        self.hgvs_url = self.root_url + "/vep/human/hgvs/"
        self.rs_url = self.root_url + "/vep/human/id/"
        self.headers = {"Content-Type": "application/json"}

    def get_single_hgvs(self, hgvs):
        url = self.hgvs_url + hgvs
        r = requests.get(url, headers=self.headers)
        return self.turn_json(r)

    def get_single_rs(self, rs):
        url = self.rs_url + rs
        r = requests.get(url, headers=self.headers)
        return self.turn_json(r)

    @staticmethod
    def turn_json(r):
        if not r.ok:
            r.raise_for_status()
            sys.exit()
        else:
            return json.loads(r.text)[0]

    '''
    def get_multi_hgvs(self, *hgvs):
        headers = self.headers.copy()
        headers["Accept"] = "application/json"
        data = {
            "hgvs_notations": list(hgvs)
        }
        data = str(data)
        r = requests.post(self.hgvs_url, headers=headers, data=data)
        return r.text
    '''