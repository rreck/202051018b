```json
{
  "id": "27cad05fa7dc27a4",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760285371,
  "host_pid": "9e6742732c60:1",
  "hash": "66f0fe9a1cbe9b19414ae177108fd24c3d84ee85f74d67125cd5d853b102813b",
  "cid": "QmV166f0fe9a1cbe9b19414ae177108fd24c3d84ee85",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760285371,
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
      "evaluated_at": 1760285371
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "duplicate_transaction",
    "risk_high"
  ],
  "sig": "f058bebdd67ff8c26e08ce4ebac6bbbae6477f09235abbeff6d1228ce24a8163"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 111000026203898
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 16434366, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 38, 'first_seen': 1760284979, 'matching_hash': '464b48f6c600a373'}}}