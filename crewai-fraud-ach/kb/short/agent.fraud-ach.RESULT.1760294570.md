```json
{
  "id": "e0e2c1d1efec32a1",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294570,
  "host_pid": "9e6742732c60:1",
  "hash": "d8840b1d37aa7f249b0cbc50344b7c79a8966211b8355de99461ecb2bf653f88",
  "cid": "QmV1d8840b1d37aa7f249b0cbc50344b7c79a8966211",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294570,
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
      "evaluated_at": 1760294570
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
  "sig": "f1f8c1d43995f86799661a44e7849ba2d15168eed04eced7abef4f7cb8c689d8"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201464250877
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 240, 'threshold': 50, 'total_amount': 89514960, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 239, 'first_seen': 1760285765, 'matching_hash': '9a278d14d50dbff1'}}}