```json
{
  "id": "630facbb7238bd0f",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286734,
  "host_pid": "9e6742732c60:1",
  "hash": "e78e5a6a46b2cb979fdd68aaa1f3b3de5459dbbb3c0731959d7c420fb15e8643",
  "cid": "QmV1e78e5a6a46b2cb979fdd68aaa1f3b3de5459dbbb",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286734,
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
      "evaluated_at": 1760286734
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
  "sig": "7df0d2cc54ac5d011d2e9f8c64f602e89a3b25f29f513b9f00b3bb753cfbfc6d"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 121000245748791
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 34, 'first_seen': 1760285765, 'matching_hash': 'b01b0e655b1e1c55'}}}