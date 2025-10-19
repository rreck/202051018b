```json
{
  "id": "84c70e2a920b31f6",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286896,
  "host_pid": "9e6742732c60:1",
  "hash": "64bb25fab78d93736b42d1a49f7e6704828ca4d47f0c7291e4a70db7d5815d78",
  "cid": "QmV164bb25fab78d93736b42d1a49f7e6704828ca4d4",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286896,
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
      "evaluated_at": 1760286896
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
  "sig": "355e0d6e259b0b96d3908e0bdccb298e5b4fb6b57c69872494a4952622e74fb8"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 044000030474832
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 15686149, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 40, 'first_seen': 1760285763, 'matching_hash': 'bdea4d686a9b26f8'}}}