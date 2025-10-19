```json
{
  "id": "ffcaf1d818d5f139",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294729,
  "host_pid": "9e6742732c60:1",
  "hash": "e14d5c0717b0e7c9fa6306ec1355bf5bb1f416d1e1840425f62fc1f60dc23ca8",
  "cid": "QmV1e14d5c0717b0e7c9fa6306ec1355bf5bb1f416d1",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294729,
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
      "evaluated_at": 1760294729
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
  "sig": "4409406c7b471a33b3aa36f6a6f4c42dbfbaba2c35c97d0a44a5ed9bcd9c1488"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201460501611
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 243, 'threshold': 50, 'total_amount': 41215473, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 242, 'first_seen': 1760285764, 'matching_hash': 'a26573d157351ea4'}}}