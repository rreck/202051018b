```json
{
  "id": "114a20522a172317",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292402,
  "host_pid": "9e6742732c60:1",
  "hash": "d9e16696bb9ccd4fa4265171d5b3d23841ff9d697582984653dacf19303bfe59",
  "cid": "QmV1d9e16696bb9ccd4fa4265171d5b3d23841ff9d69",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292402,
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
      "evaluated_at": 1760292402
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
  "sig": "40ca6d4d3b9238bce76dbcf09f29f52067c347521121d1d6f60f012a765c6e7e"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000038073979
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 197, 'threshold': 50, 'total_amount': 18836746, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 196, 'first_seen': 1760285763, 'matching_hash': '05e8b4bb68b88ac5'}}}