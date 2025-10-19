```json
{
  "id": "617e9d257f6bc16d",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287938,
  "host_pid": "9e6742732c60:1",
  "hash": "3b8135623b43e7713483df9ee6b84070ceebd1f6e5088ea38d28a517c6fbfd99",
  "cid": "QmV13b8135623b43e7713483df9ee6b84070ceebd1f6",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287938,
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
      "evaluated_at": 1760287938
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
  "sig": "e86528cc7536ff6a885320f073c687c246fe13d740c353d7d81f1a7ff4513961"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000025832040
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 77, 'threshold': 50, 'total_amount': 34525491, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 76, 'first_seen': 1760285764, 'matching_hash': '02af8ad93f509b45'}}}