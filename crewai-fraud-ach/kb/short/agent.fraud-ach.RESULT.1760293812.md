```json
{
  "id": "99d680d9b2cd269b",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293812,
  "host_pid": "9e6742732c60:1",
  "hash": "fc3a46ef1dbb2487644d951b156a0d4587e6ca6830d7b4088e1dbd934da8619d",
  "cid": "QmV1fc3a46ef1dbb2487644d951b156a0d4587e6ca68",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293812,
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
      "evaluated_at": 1760293812
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
  "sig": "5303eb14ed9797f2d33eb05033c5e5626b841e9f605b1d9130636a0ca1d09753"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000241012804
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 226, 'threshold': 50, 'total_amount': 62409900, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 225, 'first_seen': 1760285763, 'matching_hash': 'ba9ba43773b08e05'}}}