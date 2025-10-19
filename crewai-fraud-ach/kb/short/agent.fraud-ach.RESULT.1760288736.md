```json
{
  "id": "22c72220f2806a2e",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288736,
  "host_pid": "9e6742732c60:1",
  "hash": "bbb2e5361513133519151003449f23ccae8096095fd84d31c9062f95a4bd7bca",
  "cid": "QmV1bbb2e5361513133519151003449f23ccae809609",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288736,
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
      "evaluated_at": 1760288736
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
  "sig": "71785150ea50b50aae2219192f918e02fc74c11dc9317d9283bdabd4b2e7c925"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009591834365
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 102, 'threshold': 50, 'total_amount': 39545910, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 101, 'first_seen': 1760285765, 'matching_hash': 'c677ee5f465e30c5'}}}