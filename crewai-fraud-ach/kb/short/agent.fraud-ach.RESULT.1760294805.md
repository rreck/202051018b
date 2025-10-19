```json
{
  "id": "4515428ff4f698b7",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294805,
  "host_pid": "9e6742732c60:1",
  "hash": "66c4e9de69f5bea6501c6d589f2a48a6b3367671f3c31e9daa7c1562260a8f24",
  "cid": "QmV166c4e9de69f5bea6501c6d589f2a48a6b3367671",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294805,
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
      "evaluated_at": 1760294805
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
  "sig": "1c122600cf97d0d55290840009e52ef552e44f7ea18804c57ed59f505ef8a8f4"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100271879965
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 245, 'threshold': 50, 'total_amount': 51964255, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 244, 'first_seen': 1760285763, 'matching_hash': '9c4837aa9a8e4a4a'}}}