```json
{
  "id": "cd49e76682538c0e",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289938,
  "host_pid": "9e6742732c60:1",
  "hash": "2f0f6f225630e565c3557062afbbf3702573dde25b4623ae6ab635478e33bfca",
  "cid": "QmV12f0f6f225630e565c3557062afbbf3702573dde2",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289938,
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
      "evaluated_at": 1760289938
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
  "sig": "5bfbc42131977ab7fc950ab10903e08d7550722b7a4aa7c1bb7a2b1c3961b44d"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000039536800
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 137, 'threshold': 50, 'total_amount': 24479434, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 136, 'first_seen': 1760285763, 'matching_hash': '37ca22243c3304cf'}}}aly': {'fraud_detected': True, 'risk_score': 60, 'details': {'iqr_bounds': {'lower': -193126.0, 'upper': 787386.0}, 'amount': 5105266}}}