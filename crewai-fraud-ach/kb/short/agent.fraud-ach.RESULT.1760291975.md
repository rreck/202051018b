```json
{
  "id": "f296ec118c9cf892",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291975,
  "host_pid": "9e6742732c60:1",
  "hash": "6486eccd2d8a20b8a9d3b07d863699b26596968da9bdc8ec539371fbf0e33351",
  "cid": "QmV16486eccd2d8a20b8a9d3b07d863699b26596968d",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291975,
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
      "evaluated_at": 1760291975
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
  "sig": "a5e894f0668982bb8963b08eba031b7e8fbb7fafc8eb616dfcb49d551c1f7a96"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000031910208
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 187, 'threshold': 50, 'total_amount': 71284774, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 186, 'first_seen': 1760285763, 'matching_hash': '8397d9ba38a9dfb7'}}}