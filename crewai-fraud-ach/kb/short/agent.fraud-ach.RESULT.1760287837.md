```json
{
  "id": "eaa546feb9f35100",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287837,
  "host_pid": "9e6742732c60:1",
  "hash": "d145adf5abc639992e734658961fcb57f3cceab11674827cb1fee05b39aa3c77",
  "cid": "QmV1d145adf5abc639992e734658961fcb57f3cceab1",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287837,
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
      "evaluated_at": 1760287837
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
  "sig": "d4a569992cc9bffaef655b0a17648b404d0fec4f2c5976d459dfec8150ba6bc6"
}
```

Fraud detected: duplicate_transaction (score: 91)
Transaction: 044000033621272
Details: {'velocity': {'fraud_detected': True, 'risk_score': 98, 'details': {'transaction_count': 74, 'threshold': 50, 'total_amount': 11036508, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 73, 'first_seen': 1760285763, 'matching_hash': 'd5b1a20ced8a5769'}}}