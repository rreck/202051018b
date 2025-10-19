```json
{
  "id": "0f5f274637bf5907",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289254,
  "host_pid": "9e6742732c60:1",
  "hash": "6e1f73c6a797bfd7a3960aebe9a39b7ef60ece94e46eacbe1da58434839d6ab1",
  "cid": "QmV16e1f73c6a797bfd7a3960aebe9a39b7ef60ece94",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289254,
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
      "evaluated_at": 1760289254
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
  "sig": "71fdcf7e2d3350707c8335953685efada00a18e785ade4479b52f50fc05e6190"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000028841300
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 118, 'threshold': 50, 'total_amount': 22058330, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 117, 'first_seen': 1760285763, 'matching_hash': 'f5bed59f6c250fae'}}}