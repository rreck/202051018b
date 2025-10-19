```json
{
  "id": "9afdb53fcd9ddf8b",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286445,
  "host_pid": "9e6742732c60:1",
  "hash": "7996dca7542732fd279e81c363da767128e1ec45714383d1bd096b51913b0f6c",
  "cid": "QmV17996dca7542732fd279e81c363da767128e1ec45",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286445,
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
      "evaluated_at": 1760286445
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
  "sig": "be1f98aea125b8172e9972a22aaa14407265f590af0d987e0d0005360b0baa94"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 122105156608425
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 24, 'first_seen': 1760285765, 'matching_hash': '07039b94da8bf942'}}}