```json
{
  "id": "b7dce3f2d771e242",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287668,
  "host_pid": "9e6742732c60:1",
  "hash": "1c9c78852b3509082da5042fba021c051fc16ff730fbab6e89d794fcacd1fe5e",
  "cid": "QmV11c9c78852b3509082da5042fba021c051fc16ff7",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287668,
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
      "evaluated_at": 1760287668
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
  "sig": "9744116d60853205e66d0f12f842231635be7731376ea9d1dd571ebd9d1c33ce"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 026009591362197
Details: {'velocity': {'fraud_detected': True, 'risk_score': 86, 'details': {'transaction_count': 68, 'threshold': 50, 'total_amount': 27381152, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 67, 'first_seen': 1760285763, 'matching_hash': 'b2660329f17701b7'}}}