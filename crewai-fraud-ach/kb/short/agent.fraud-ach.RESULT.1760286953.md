```json
{
  "id": "4df90930510e3c64",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286953,
  "host_pid": "9e6742732c60:1",
  "hash": "330e97cd47a7898e7b50b3194dbbb44e828f56d7275d2a72b66fb378936675bb",
  "cid": "QmV1330e97cd47a7898e7b50b3194dbbb44e828f56d7",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286953,
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
      "evaluated_at": 1760286953
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
  "sig": "f6492940993122c8d2330a1bc8f0103ea5539bbd7153a26f18c6cf617855c1ae"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 063100277276019
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'total_amount': 16253097, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 42, 'first_seen': 1760285763, 'matching_hash': '90b38bd8812494f9'}}}