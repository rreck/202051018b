```json
{
  "id": "94ddce4d32902fa3",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294571,
  "host_pid": "9e6742732c60:1",
  "hash": "99fbf29a4e8e9cf0039fc1f38c9f7dab77b4d09749743a3de9a67177b8932e8f",
  "cid": "QmV199fbf29a4e8e9cf0039fc1f38c9f7dab77b4d097",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294571,
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
      "evaluated_at": 1760294571
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
  "sig": "bac129414d9ca073ab551ff6c2fedc381ff276ee64f306d99a062e3bc651e140"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000035733360
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 240, 'threshold': 50, 'total_amount': 78783840, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 239, 'first_seen': 1760285765, 'matching_hash': '19d9911872be19af'}}}