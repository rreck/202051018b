```json
{
  "id": "3d5e0a5b13c09ab2",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293514,
  "host_pid": "9e6742732c60:1",
  "hash": "a4a205d11c6c22fd765a62b3813d331eb2b611220636db1707a1f85667d104d4",
  "cid": "QmV1a4a205d11c6c22fd765a62b3813d331eb2b61122",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293514,
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
      "evaluated_at": 1760293514
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
  "sig": "56cefa7bbbdec511ffa872e5d9bf8845e2b0115024408785962cb00db75b7695"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201467071616
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 220, 'threshold': 50, 'total_amount': 98943680, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 219, 'first_seen': 1760285764, 'matching_hash': 'cbd6f8586f75cfb9'}}}