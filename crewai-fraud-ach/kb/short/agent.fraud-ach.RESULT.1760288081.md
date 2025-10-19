```json
{
  "id": "0d886642b6cfc606",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288081,
  "host_pid": "9e6742732c60:1",
  "hash": "3b73ae4bf481e8b97a0907e0bd3e3ab09f4f3beb5e6623267945767d3d714db9",
  "cid": "QmV13b73ae4bf481e8b97a0907e0bd3e3ab09f4f3beb",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288081,
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
      "evaluated_at": 1760288081
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
  "sig": "d4f472c7fc72951637edc73ed49ffc5644c1eeb10386971fd9cd6bd202a60b16"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009596363200
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 82, 'threshold': 50, 'total_amount': 31300876, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 81, 'first_seen': 1760285764, 'matching_hash': 'b9f8fedd6c477a32'}}}