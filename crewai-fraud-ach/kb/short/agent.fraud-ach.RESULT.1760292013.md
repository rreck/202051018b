```json
{
  "id": "a615f4f5161dc541",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292013,
  "host_pid": "9e6742732c60:1",
  "hash": "d7dc048f9a0c393c08c5cdc6c067e132edbb6957299196e63c265add0224b831",
  "cid": "QmV1d7dc048f9a0c393c08c5cdc6c067e132edbb6957",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292013,
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
      "evaluated_at": 1760292013
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
  "sig": "acd77d93b1587f859f406887582432641637bb251bea94eba0ed5b6a9b28a854"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000030256978
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 264, 'threshold': 50, 'total_amount': 100202256, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 263, 'first_seen': 1760284979, 'matching_hash': 'a2caca18f22a9a3d'}}}