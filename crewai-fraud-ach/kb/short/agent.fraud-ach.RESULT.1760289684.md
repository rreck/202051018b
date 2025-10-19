```json
{
  "id": "93087106067a79b6",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289684,
  "host_pid": "9e6742732c60:1",
  "hash": "3643d0aa3bf18f9ac726908ba7adb07c32c24abf550f10e2880a0248e9686345",
  "cid": "QmV13643d0aa3bf18f9ac726908ba7adb07c32c24abf",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289684,
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
      "evaluated_at": 1760289684
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
  "sig": "b362b2452ecb50d1d0d807bef6454b1e2ac6d870da6eceed8177552019dbff2c"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000027931714
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 130, 'threshold': 50, 'total_amount': 35371570, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 129, 'first_seen': 1760285764, 'matching_hash': 'e2e3d7aa40c6ad9f'}}}