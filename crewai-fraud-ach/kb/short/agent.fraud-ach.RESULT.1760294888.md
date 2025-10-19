```json
{
  "id": "c03506317ce4a674",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294888,
  "host_pid": "9e6742732c60:1",
  "hash": "30251ba91e02870ea2321dc998257905b7bbfe05084e9948faec6eacf4e20503",
  "cid": "QmV130251ba91e02870ea2321dc998257905b7bbfe05",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294888,
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
      "evaluated_at": 1760294888
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
  "sig": "3e8369415b83b2acea1bdc306bec1cabe0c9397cf2b68954dca072c228769bb6"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000034981344
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 246, 'threshold': 50, 'total_amount': 93429816, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 245, 'first_seen': 1760285765, 'matching_hash': '0030d58ae3a464b4'}}}