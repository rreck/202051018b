```json
{
  "id": "fcd627deab947324",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286923,
  "host_pid": "9e6742732c60:1",
  "hash": "0c2da8534124eef9b6f1a212e4c21423da1834dbd89c0a0dc9a860ce932441ea",
  "cid": "QmV10c2da8534124eef9b6f1a212e4c21423da1834db",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286923,
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
      "evaluated_at": 1760286923
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
  "sig": "737f4915375775b6ef554604960cb8d1ccef5de5764c771028d4f82c7b374a30"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 044000031117260
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 41, 'first_seen': 1760285763, 'matching_hash': '467ec1c9bc787c3f'}}}