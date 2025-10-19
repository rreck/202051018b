```json
{
  "id": "1ecca13bb1947a53",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287764,
  "host_pid": "9e6742732c60:1",
  "hash": "6af60756f5956dd77b701de3c7c91f33e4b909d0e2bec9f0d5b28f142a6f9176",
  "cid": "QmV16af60756f5956dd77b701de3c7c91f33e4b909d0",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287764,
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
      "evaluated_at": 1760287764
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
  "sig": "552015bd9928b773ff8968e394a543a56c33097060cafcbf4ab9996f4638807d"
}
```

Fraud detected: duplicate_transaction (score: 88)
Transaction: 122105156608425
Details: {'velocity': {'fraud_detected': True, 'risk_score': 92, 'details': {'transaction_count': 71, 'threshold': 50, 'total_amount': 22595608, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 70, 'first_seen': 1760285765, 'matching_hash': '07039b94da8bf942'}}}