```json
{
  "id": "4240ad3867a1020f",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287914,
  "host_pid": "9e6742732c60:1",
  "hash": "ccba5905fdf654f374c418afa4b283f05c4ad7c1596d01c0fa57755ac6c8d0f1",
  "cid": "QmV1ccba5905fdf654f374c418afa4b283f05c4ad7c1",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287914,
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
      "evaluated_at": 1760287914
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
  "sig": "699de331c1ea2f033c009e5af53c2ca1d9108fa3846041459454d5fbb7359bae"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105156608425
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 76, 'threshold': 50, 'total_amount': 24186848, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 75, 'first_seen': 1760285765, 'matching_hash': '07039b94da8bf942'}}}