```json
{
  "id": "f87b8375149837f4",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294333,
  "host_pid": "9e6742732c60:1",
  "hash": "9aa1fbf9ac87a1272509ce8bf40d0615548f2d958949ed862899a9ae9f08b47a",
  "cid": "QmV19aa1fbf9ac87a1272509ce8bf40d0615548f2d95",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294333,
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
      "evaluated_at": 1760294333
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
  "sig": "108457021c52f67bf8a805eb9353d45ae9196868f51860130a7505e6d739fd41"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000021715081
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 236, 'threshold': 50, 'total_amount': 53932136, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 235, 'first_seen': 1760285764, 'matching_hash': '0ea9b1b5c7891ffe'}}}}