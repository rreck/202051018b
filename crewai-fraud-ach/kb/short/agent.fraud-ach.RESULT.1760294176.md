```json
{
  "id": "833b9f66533c77e0",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294176,
  "host_pid": "9e6742732c60:1",
  "hash": "73f9d8d591c9fbc6811c8f5ce3e299a5fa0c47896f3f0ee87c4b81000c480772",
  "cid": "QmV173f9d8d591c9fbc6811c8f5ce3e299a5fa0c4789",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294176,
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
      "evaluated_at": 1760294176
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
  "sig": "e0b776caaef9fbd830e397cbd9cb474a9a9d5bc2452a7a92ad06fb45a403f389"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000037688830
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 233, 'threshold': 50, 'total_amount': 59538956, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 232, 'first_seen': 1760285764, 'matching_hash': 'a1e0090e71bf48f4'}}}