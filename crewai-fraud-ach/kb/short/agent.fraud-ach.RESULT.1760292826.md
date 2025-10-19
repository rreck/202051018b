```json
{
  "id": "915043f1718b26ad",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292826,
  "host_pid": "9e6742732c60:1",
  "hash": "feb8e99d0ea31f29c1db6cb296567c74dc1ed8f4d45e90b3a3725e66f774aea0",
  "cid": "QmV1feb8e99d0ea31f29c1db6cb296567c74dc1ed8f4",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292826,
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
      "evaluated_at": 1760292826
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
  "sig": "8cf3ace0bb48a66cd6c49ff78f90a48980af2d9dc3effd2b81c6b1157771d2c9"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100278631812
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 206, 'threshold': 50, 'total_amount': 39103332, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 205, 'first_seen': 1760285763, 'matching_hash': 'e154fa328ed40444'}}}