```json
{
  "id": "7695beb6a7b72df7",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294218,
  "host_pid": "9e6742732c60:1",
  "hash": "bd83c500a3111400b5d6c281e7f1213f9f42ec422532f5b633eb284170ebdb7a",
  "cid": "QmV1bd83c500a3111400b5d6c281e7f1213f9f42ec42",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294218,
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
      "evaluated_at": 1760294218
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
  "sig": "fae6d4e7d23c86ce7088519e778ba975b5e2f5f515d227182ca1762dc90e16c0"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000025159939
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 234, 'threshold': 50, 'total_amount': 110408688, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 233, 'first_seen': 1760285763, 'matching_hash': 'bd88da65ef85df29'}}}