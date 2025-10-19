```json
{
  "id": "94abd424a8ae1915",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288151,
  "host_pid": "9e6742732c60:1",
  "hash": "fad9230fed209dac341e516d504bcae16565837c7330a81a3300523bd06e2e7d",
  "cid": "QmV1fad9230fed209dac341e516d504bcae16565837c",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288151,
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
      "evaluated_at": 1760288151
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
  "sig": "8b6b382464074c03d424d39063911f470fa4a0b742065473ae6a99482a8cc807"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009591362197
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 84, 'threshold': 50, 'total_amount': 33823776, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 83, 'first_seen': 1760285763, 'matching_hash': 'b2660329f17701b7'}}}