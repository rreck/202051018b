```json
{
  "id": "63379f93d527366e",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288265,
  "host_pid": "9e6742732c60:1",
  "hash": "50e95c49d727ed5f6e16fd48582bb8ff983e28de73a492ad9ced2e4fb87360bf",
  "cid": "QmV150e95c49d727ed5f6e16fd48582bb8ff983e28de",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288265,
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
      "evaluated_at": 1760288265
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
  "sig": "70a37c07db0908f319eafa46794d2a287eb2a4ee399cf10332e44f73aea24e39"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000242331672
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 88, 'threshold': 50, 'total_amount': 10182128, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 87, 'first_seen': 1760285763, 'matching_hash': '532e279550beef55'}}}