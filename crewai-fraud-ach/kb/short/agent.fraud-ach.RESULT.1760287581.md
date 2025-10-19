```json
{
  "id": "86c7fc1618ccbba8",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287581,
  "host_pid": "9e6742732c60:1",
  "hash": "fa8a05a88f7fd8175f7b2cd6dfc385809f8c27848bc32300a85f04b0c09900a3",
  "cid": "QmV1fa8a05a88f7fd8175f7b2cd6dfc385809f8c2784",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287581,
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
      "evaluated_at": 1760287581
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
  "sig": "f84aaabb7fa7634454c0d52e55e1ac7a266ef55ef819d0b5f1b67248a79f4881"
}
```

Fraud detected: duplicate_transaction (score: 82)
Transaction: 044000031029200
Details: {'velocity': {'fraud_detected': True, 'risk_score': 80, 'details': {'transaction_count': 65, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 64, 'first_seen': 1760285763, 'matching_hash': '80e7fe619ff961e0'}}}