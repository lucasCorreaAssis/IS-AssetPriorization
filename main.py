import numpy as np
from asset_priorization import AssetPriorization

alternatives = [
    'Robotics Station',
    'Transport System',
    'AS/RS',
    'T/F Station'
]

asset_priorization = AssetPriorization(alternatives)

security_risk_values = [4,1,2,5]
production_unavailability_values = [240,180,150,200]
quality_impact_values = [5,1,1,5]
environmental_risk_values = [1,2,3,1]
mttr_values = [4,3,2.5,3.3]
mtbf_values = [720,360,720,240]
maintenance_cost_values = [2000,1500,2000,1000]

values = np.array([
    security_risk_values,
    production_unavailability_values,
    quality_impact_values,
    environmental_risk_values,
    mttr_values,
    mtbf_values,
    maintenance_cost_values
])

output = asset_priorization.prioritize(values)

for i, unicriteria_phi in enumerate(output.unicriteria_phi):
    print(f'{i}- {unicriteria_phi}\n')
