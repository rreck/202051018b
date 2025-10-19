```json
{
  "id": "b2cd49f30f59168f",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292553,
  "host_pid": "9e6742732c60:1",
  "hash": "94ab5c3d53be6d7bb00c253b8567c7b02263a247fb237d9d8ebf9f5aea06bef3",
  "cid": "QmV194ab5c3d53be6d7bb00c253b8567c7b02263a247",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292553,
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
      "evaluated_at": 1760292553
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
  "sig": "a9baa7372b06198445707cb93c320ef787a6c1f39bde2fd14179df67bc34b390"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009592967123
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 200, 'threshold': 50, 'total_amount': 35254400, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 199, 'first_seen': 1760285763, 'matching_hash': 'c09be009c43e6bc8'}}}