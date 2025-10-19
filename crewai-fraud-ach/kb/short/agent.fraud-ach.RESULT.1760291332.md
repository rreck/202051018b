```json
{
  "id": "b7c3bedfed6329e0",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291332,
  "host_pid": "9e6742732c60:1",
  "hash": "e5a48d7b1c1dc9519c2491c5bae9ca63d946a0c61c237ddfabfad27fddc917bf",
  "cid": "QmV1e5a48d7b1c1dc9519c2491c5bae9ca63d946a0c6",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291332,
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
      "evaluated_at": 1760291332
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
  "sig": "5a5f7d30923f8706e4beb58cdccde2fe53e73312a503f9ffdda3ddf73b58d887"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000242521033
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 172, 'threshold': 50, 'total_amount': 11442988, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 171, 'first_seen': 1760285765, 'matching_hash': 'cfb80109aa92585a'}}}