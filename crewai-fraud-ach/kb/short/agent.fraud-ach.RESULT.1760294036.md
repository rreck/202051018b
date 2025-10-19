```json
{
  "id": "86c33f31913cb82c",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294036,
  "host_pid": "9e6742732c60:1",
  "hash": "0148bda34e07795d82bb9efea764b830419fc6be9b166e7a4f984796ffda1570",
  "cid": "QmV10148bda34e07795d82bb9efea764b830419fc6be",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294036,
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
      "evaluated_at": 1760294036
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
  "sig": "82cc8f583b1594e9296a2c273025a79eac0595ab04636fab2d10a1264fca6438"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201469927048
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 230, 'threshold': 50, 'total_amount': 68522290, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 229, 'first_seen': 1760285763, 'matching_hash': '982ed2d64f96a5b2'}}}