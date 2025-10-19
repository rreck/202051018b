```json
{
  "id": "6a430407227378c5",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292686,
  "host_pid": "9e6742732c60:1",
  "hash": "69bb85248572c4b6509dae502ca88b8fa4bd2f33dc1b19e16d0bcc657fb7b3a3",
  "cid": "QmV169bb85248572c4b6509dae502ca88b8fa4bd2f33",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292686,
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
      "evaluated_at": 1760292686
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
  "sig": "bd0c3c31340b05b7918c2ef965e7042405772e71bbffe609c9aeb1ab70b37444"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100274851410
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 203, 'threshold': 50, 'total_amount': 25126934, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 202, 'first_seen': 1760285763, 'matching_hash': '05e1730ec720465d'}}}