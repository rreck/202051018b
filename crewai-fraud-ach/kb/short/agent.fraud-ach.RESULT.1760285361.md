```json
{
  "id": "1c3776cc0f119776",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760285361,
  "host_pid": "9e6742732c60:1",
  "hash": "3382cb9642ef28dae117b76eb5f7ad87817b75ef9ac049924c505fb9ce2d7268",
  "cid": "QmV13382cb9642ef28dae117b76eb5f7ad87817b75ef",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760285361,
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
      "evaluated_at": 1760285361
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
  "sig": "fea965611aa34d72d7fe54156dae4298ada1ec9ed8e96b1c924c8f7729c0046c"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 111000026203898
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 16012972, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 37, 'first_seen': 1760284979, 'matching_hash': '464b48f6c600a373'}}}