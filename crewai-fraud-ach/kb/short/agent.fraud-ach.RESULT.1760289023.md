```json
{
  "id": "a6a74bbefb65fef6",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289023,
  "host_pid": "9e6742732c60:1",
  "hash": "8cdde602616586ebbc6f6d576ae214091b6b600470ed8eda9e4a380e54190a17",
  "cid": "QmV18cdde602616586ebbc6f6d576ae214091b6b6004",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289023,
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
      "evaluated_at": 1760289023
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
  "sig": "8d4da336fa7d149e1787ff86e58679ec56f5f1183f8f2c8056fd82cba8eaedba"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000027329696
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 111, 'threshold': 50, 'total_amount': 50888727, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 110, 'first_seen': 1760285763, 'matching_hash': '9d5d387a3c2fb6f6'}}}