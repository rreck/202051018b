```json
{
  "id": "746f90ffdb11a1b3",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290117,
  "host_pid": "9e6742732c60:1",
  "hash": "ec7a729ff5e6a696d3b9a19f6b305e1dbc81936dd01ae33bb3f2a81ccfb03a6b",
  "cid": "QmV1ec7a729ff5e6a696d3b9a19f6b305e1dbc81936d",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290117,
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
      "evaluated_at": 1760290117
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "duplicate_transaction",
    "risk_critical"
  ],
  "sig": "b58df73ab2e8d18b6abb6cff03fe41927712a0972c35bf76fc9e2338e1729273"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000246132965
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 142, 'threshold': 50, 'total_amount': 62436122, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 141, 'first_seen': 1760285763, 'matching_hash': 'ed6ec2b6e100ea2c'}}}{'fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '041887155', 'validation_error': 'Invalid routing number checksum'}}}