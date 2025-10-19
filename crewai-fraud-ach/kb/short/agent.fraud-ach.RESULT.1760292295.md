```json
{
  "id": "19401c46c48afa23",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292295,
  "host_pid": "9e6742732c60:1",
  "hash": "b637160c89b16aa6b54f1b4429a3609372a763db758d8ed4a13f03ae17c9cf7f",
  "cid": "QmV1b637160c89b16aa6b54f1b4429a3609372a763db",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292295,
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
      "evaluated_at": 1760292296
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
  "sig": "e2a734a6719e73bd90008ba5baa3beddde6623238d08a38d734e4a8935d93001"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000248581748
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 194, 'threshold': 50, 'total_amount': 37090278, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 193, 'first_seen': 1760285765, 'matching_hash': '6ba0c7e0a23e9d51'}}}