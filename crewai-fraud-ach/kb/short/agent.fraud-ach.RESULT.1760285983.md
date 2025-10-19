```json
{
  "id": "2cbf95db689d1da8",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760285983,
  "host_pid": "9e6742732c60:1",
  "hash": "708b58a7bf16660da2243cbe3356febc595ac60f2aeb9a2e797ed86d7f7d52f9",
  "cid": "QmV1708b58a7bf16660da2243cbe3356febc595ac60f",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760285983,
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
      "evaluated_at": 1760285983
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
  "sig": "7c95d3d6b6bce1e5dbb7c33f194df2e16276f17036f84dae368a7b69f4e050f2"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 111000022307864
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 9, 'first_seen': 1760285765, 'matching_hash': '183a325d3d521c29'}}}