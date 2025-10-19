```json
{
  "id": "1b07438bcf41136e",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291191,
  "host_pid": "9e6742732c60:1",
  "hash": "8ce66a704f73d3459eace9964c42f8b186933c7a81ba0829e2542b36c79c2f6d",
  "cid": "QmV18ce66a704f73d3459eace9964c42f8b186933c7a",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291191,
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
      "evaluated_at": 1760291191
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
  "sig": "2097523524e1755a4a4fde1e5245e31c1534b41b90e593e6628abd5908aa41e9"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000242680908
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 169, 'threshold': 50, 'total_amount': 58264102, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 168, 'first_seen': 1760285764, 'matching_hash': '8e78dc9e18bacaa7'}}}aly': {'fraud_detected': True, 'risk_score': 60, 'details': {'iqr_bounds': {'lower': -193126.0, 'upper': 787386.0}, 'amount': 5105266}}}