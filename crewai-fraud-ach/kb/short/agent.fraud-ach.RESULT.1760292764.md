```json
{
  "id": "0772482224b2955c",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292764,
  "host_pid": "9e6742732c60:1",
  "hash": "7c193d4552ec8f90215c5cc4603301b584cc639899112331bd564bc23c7d8b5b",
  "cid": "QmV17c193d4552ec8f90215c5cc4603301b584cc6398",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292764,
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
      "evaluated_at": 1760292764
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
  "sig": "01fa38d05d966f18387e2b9bf51f77d6f5d31ffa68bb9866722eeed02a560260"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000241355402
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 204, 'threshold': 50, 'total_amount': 33234252, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 203, 'first_seen': 1760285765, 'matching_hash': '58524718dce63a85'}}}