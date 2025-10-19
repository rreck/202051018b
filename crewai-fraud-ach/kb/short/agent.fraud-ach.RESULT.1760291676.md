```json
{
  "id": "fc0398a24cdd6288",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291676,
  "host_pid": "9e6742732c60:1",
  "hash": "32c3fcd18529d64daa077ea3a8835e1da3d9a88bc6549d565663a702e7b58f64",
  "cid": "QmV132c3fcd18529d64daa077ea3a8835e1da3d9a88b",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291676,
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
      "evaluated_at": 1760291676
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
  "sig": "4fc6cea493e5dd5a349114e3224d47cc04f8afa8af3d8b3ee84632f37d1ac9b9"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000025339678
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 180, 'threshold': 50, 'total_amount': 72650520, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 179, 'first_seen': 1760285765, 'matching_hash': '57e7473926bfe00b'}}}