```json
{
  "id": "b161c33b17192119",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288211,
  "host_pid": "9e6742732c60:1",
  "hash": "88627d5ad14f71096d84a78d150e40c6660860cb09c64eb58cd4baf7b73fc8ae",
  "cid": "QmV188627d5ad14f71096d84a78d150e40c6660860cb",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288211,
      "method": "automated_fraud_detection",
      "vc_type": "VerifiableCredential"
    },
    "ucon": {
      "usage_constraints": [
        "no_pii_export",
        "audit_required"
      ],
      "purpose": "fraud_detection_analysis",
      "enforcement": "mandatory"
    },
    "eval": {
      "confidence": 1.0,
      "evidence_count": 0,
      "review_status": "pending",
      "evaluated_at": 1760288211
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "invalid_routing",
    "risk_critical"
  ],
  "sig": "f278d872330ac1b1b7259ab2c93cc38f9f245ad5d435939669ae4e44e135b7c5"
}
```

Fraud detected: invalid_routing (score: 93)
Transaction: 676666911893287
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 86, 'threshold': 50, 'total_amount': 33536388, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 85, 'first_seen': 1760285763, 'matching_hash': '67218afda9e45d8d'}}, 'routing': {'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '676666915', 'validation_error': 'Invalid routing number checksum'}}}