```json
{
  "id": "2dd3c43d76a42780",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291808,
  "host_pid": "9e6742732c60:1",
  "hash": "ff7009f3d35d7cd948f79c93d4d8aaffeea15d46db7867ec7b6a27d04a455d37",
  "cid": "QmV1ff7009f3d35d7cd948f79c93d4d8aaffeea15d46",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291808,
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
      "evaluated_at": 1760291808
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
  "sig": "2e66dc11a3c336aa18329852463cc252d77621d1f5f6dcee94963507beae4658"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105156608425
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 183, 'threshold': 50, 'total_amount': 58239384, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 182, 'first_seen': 1760285765, 'matching_hash': '07039b94da8bf942'}}}