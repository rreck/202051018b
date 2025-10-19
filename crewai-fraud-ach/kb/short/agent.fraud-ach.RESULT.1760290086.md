```json
{
  "id": "4e7f18c554b8e77a",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290086,
  "host_pid": "9e6742732c60:1",
  "hash": "d4386003be1bf925b7c40f802d6490226c8e895edba44ef2347acc704c91fafe",
  "cid": "QmV1d4386003be1bf925b7c40f802d6490226c8e895e",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290086,
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
      "evaluated_at": 1760290086
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
  "sig": "e64cd3e1fd8af942bb70ca974368b96334e2a0a26a93be3a31746b1bc44efd91"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000248226164
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 141, 'threshold': 50, 'total_amount': 41105448, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 140, 'first_seen': 1760285763, 'matching_hash': 'b7846971abb7164d'}}}