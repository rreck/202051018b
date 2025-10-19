```json
{
  "id": "085fb7df8414374c",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287631,
  "host_pid": "9e6742732c60:1",
  "hash": "97a9eb6760fc7e7231de58319dc1b3f71dc83921c331be8fe7bc24a2d4f3ed85",
  "cid": "QmV197a9eb6760fc7e7231de58319dc1b3f71dc83921",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287631,
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
      "evaluated_at": 1760287631
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
  "sig": "0a6bbe739b43ac2b2ef65044fa08874fe54878619650cbddd5d19648f62788cd"
}
```

Fraud detected: duplicate_transaction (score: 84)
Transaction: 044000031117260
Details: {'velocity': {'fraud_detected': True, 'risk_score': 84, 'details': {'transaction_count': 67, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 66, 'first_seen': 1760285763, 'matching_hash': '467ec1c9bc787c3f'}}}