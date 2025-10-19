```json
{
  "id": "f68c4603bbae65cc",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292559,
  "host_pid": "9e6742732c60:1",
  "hash": "7f115b0b95ebd3b7c7065f43fb488806055c11545a5dc6831c3bb164418a7020",
  "cid": "QmV17f115b0b95ebd3b7c7065f43fb488806055c1154",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292559,
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
      "evaluated_at": 1760292559
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
  "sig": "745c5c721d872e2d7d6e4140be4b6fdec03d2c69329e54ee7a5fae5c15dc4906"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000024300942
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 200, 'threshold': 50, 'total_amount': 16145400, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 199, 'first_seen': 1760285763, 'matching_hash': '95903848ba405d51'}}}