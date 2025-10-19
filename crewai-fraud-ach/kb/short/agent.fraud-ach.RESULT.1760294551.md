```json
{
  "id": "23cfd600008391b7",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294551,
  "host_pid": "9e6742732c60:1",
  "hash": "462fe532cdb1c6f93eefb53287afa2c9d23ac4c9572bf49f2c001bff890b5252",
  "cid": "QmV1462fe532cdb1c6f93eefb53287afa2c9d23ac4c9",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294551,
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
      "evaluated_at": 1760294551
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
  "sig": "5ae2df1def080ae5192b9346412ecd7e1da7f1dd5d465d9450cd340c7d3cb620"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000031287652
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 240, 'threshold': 50, 'total_amount': 66498480, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 239, 'first_seen': 1760285763, 'matching_hash': 'd2d8cdbc9df50106'}}}