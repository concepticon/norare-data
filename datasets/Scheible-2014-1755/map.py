import collections

from pynorare.dataset import NormDataSet
from csvw import Column

SCHEMA = '{"type":"object","patternProperties":{".+": {"type": "object", "required":["ANT","HYP","SYN"],"properties": {"ANT": {"type": "number"},"HYP": {"type": "number"}, "SYN": {"type": "number"}}}}}'


def compute_scored_relations(row):
    row['SCORED_RELATIONS'] = collections.defaultdict(dict)
    for name, reltype, score in zip(row['IDS_IN_SOURCE'], row['RELATION_TYPE'], row['SCORES']):
        row['SCORED_RELATIONS'][name.split(':')[1]][reltype] = float(score)
    return row

class Dataset(NormDataSet):
    id = "Scheible-2014-1755"

    def map(self, write_file=True):
        tg = self.concepticon.conceptlists[self.id].tg
        items = [compute_scored_relations(row) for row in tg.tables[0]]
        tg.tables[0].tableSchema.columns.append(Column.fromvalue(dict(
            name="SCORED_RELATIONS", 
            datatype={"base": "json", "format": SCHEMA})))
        tg.write(self.meta.norare_dsdir / self.mdname, **{self.fname: items})

