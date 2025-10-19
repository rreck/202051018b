```json
{
  "id": "9814aee4570fb52f",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287132,
  "host_pid": "9e6742732c60:1",
  "hash": "e702cf0e05fac69604066385c555c4d8bc7803168f2866ece6e5baa6c0fecdbf",
  "cid": "QmV1e702cf0e05fac69604066385c555c4d8bc780316",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287132,
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
      "evaluated_at": 1760287132
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
  "sig": "38e71e7f363485cc920732f310b4aec1d4f817f93fa64696e49d39c85d4c5202"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 044000038907358
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 10597475, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 48, 'first_seen': 1760285764, 'matching_hash': '4f1b5532b664e41d'}}}