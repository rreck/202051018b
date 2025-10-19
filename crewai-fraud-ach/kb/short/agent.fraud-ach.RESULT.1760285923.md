```json
{
  "id": "77b4a65c1bdc97be",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760285923,
  "host_pid": "9e6742732c60:1",
  "hash": "c1f1cba793b24ee1ceac00554f0a9fe9aba236cccf4bac83de62e8c4fb01a982",
  "cid": "QmV1c1f1cba793b24ee1ceac00554f0a9fe9aba236cc",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760285923,
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
      "evaluated_at": 1760285923
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
  "sig": "a690006a6f0166c2a99da47cb558803ddf76f2c624e785c13528c337ed467488"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 122105155748621
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 7, 'first_seen': 1760285764, 'matching_hash': 'df4db45348ec5c9a'}}}