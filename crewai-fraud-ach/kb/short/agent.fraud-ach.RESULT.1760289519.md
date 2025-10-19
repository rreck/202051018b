```json
{
  "id": "ca3f4f7f8238b9a6",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289519,
  "host_pid": "9e6742732c60:1",
  "hash": "0ab8f48a687474a142dbd43fcd9041e12407d37652d155bf7e8c90056d356466",
  "cid": "QmV10ab8f48a687474a142dbd43fcd9041e12407d376",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289519,
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
      "evaluated_at": 1760289519
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
  "sig": "8152859a01359ccf09d4544e0ff2c081c706a7d297934e335225c66eb917c918"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105156608425
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 125, 'threshold': 50, 'total_amount': 39781000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 124, 'first_seen': 1760285765, 'matching_hash': '07039b94da8bf942'}}}