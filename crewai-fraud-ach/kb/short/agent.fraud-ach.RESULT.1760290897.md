```json
{
  "id": "b50e7f84e8980eb5",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290897,
  "host_pid": "9e6742732c60:1",
  "hash": "6bf0adaca2e535517ec0a187934c7d50fa7585a9bde30a94d65cebe726f22fd9",
  "cid": "QmV16bf0adaca2e535517ec0a187934c7d50fa7585a9",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290897,
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
      "evaluated_at": 1760290897
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
  "sig": "0e20096950d4ede6c8d9993eaa4789e6d7be9844329e31e9f49eb1134f5cd44a"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000028760265
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 162, 'threshold': 50, 'total_amount': 45024660, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 161, 'first_seen': 1760285763, 'matching_hash': 'ff1172b8afcaa4bc'}}}