```json
{
  "id": "6bc63ff906bc0c0d",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287350,
  "host_pid": "9e6742732c60:1",
  "hash": "73d5bfb1a256c7721183987f489f596b815f96d7587c3f5a5abf0051fd8807e7",
  "cid": "QmV173d5bfb1a256c7721183987f489f596b815f96d7",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287350,
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
      "evaluated_at": 1760287350
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
  "sig": "a4db4c83ac756b5ef78c5943fb4f5b173cc22009bd600f13443a221dcefa3875"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 111000024392225
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'transaction_count': 57, 'threshold': 50, 'total_amount': 25215774, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 56, 'first_seen': 1760285765, 'matching_hash': 'c2833deea8e214b7'}}}