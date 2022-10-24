'''Asset Critacality Priorization's Module'''

from typing import List
from promethee import Promethee, Criteria, UsualCurve, VShapeICurve

class AssetPriorization(Promethee):
    '''Asset Critacality Priorization'''
    def __init__(self, alternatives: List[str]):
        criterias = self.__set_criterias()
        super().__init__(alternatives, criterias)

    def __set_criterias(self) -> List[Criteria]:
        criterias = list()

        security_risk = Criteria(
            name='Security Risk',
            weight=0.06,
            goal='max',
            curve=UsualCurve()
        )
        criterias.append(security_risk)

        production_unavailability = Criteria(
            name='Production Unavailability',
            weight=0.03,
            goal='max',
            curve=VShapeICurve(p=71, q=23)
        )
        criterias.append(production_unavailability)

        quality_impact = Criteria(
            name='Quality Impact',
            weight=0.01,
            goal='max',
            curve=UsualCurve()
        )
        criterias.append(quality_impact)

        environmental_risk = Criteria(
            name='Environmental Risk',
            weight=0.01,
            goal='max',
            curve=UsualCurve()
        )
        criterias.append(environmental_risk)

        mttr = Criteria(
            name='MTTR',
            weight=0.73,
            goal='max',
            curve=VShapeICurve(p=1.2, q=0.4)
        )
        criterias.append(mttr)

        mtbf = Criteria(
            name='MTBF',
            weight=0.06,
            goal='min',
            curve=VShapeICurve(p=480, q=180)
        )
        criterias.append(mtbf)

        maintenance_cost = Criteria(
            name='Maintenance Cost',
            weight=0.11,
            goal='max',
            curve=VShapeICurve(p=926.93, q=1)
        )
        criterias.append(maintenance_cost)

        return criterias
