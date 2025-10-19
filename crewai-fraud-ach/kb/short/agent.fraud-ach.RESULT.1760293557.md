```json
{
  "id": "7c36e9a2aa0a22d6",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293557,
  "host_pid": "9e6742732c60:1",
  "hash": "940d30841ca1fdb9e6461fd57e72130a64c82104b8353f053137e747cf09124c",
  "cid": "QmV1940d30841ca1fdb9e6461fd57e72130a64c82104",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293557,
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
      "evaluated_at": 1760293557
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
  "sig": "de11529ad4900b9c319ca563da6f594717365dc5c252841697b3289fff34fd4c"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105154437530
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 221, 'threshold': 50, 'total_amount': 76471746, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 220, 'first_seen': 1760285763, 'matching_hash': '1df4316d53c749d8'}}}