```json
{
  "id": "93f2f06e68681908",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289195,
  "host_pid": "9e6742732c60:1",
  "hash": "7f2af3d49e0aa5cba217e9b608b018282fd635566d6564849be97d8a8606ca7d",
  "cid": "QmV17f2af3d49e0aa5cba217e9b608b018282fd63556",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289195,
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
      "evaluated_at": 1760289195
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
  "sig": "a658d1a92563efd443ad45208b627481693784fe8261dcf17688cef534dbc4e0"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009596690593
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 192, 'threshold': 50, 'total_amount': 27063360, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 191, 'first_seen': 1760284979, 'matching_hash': 'a761076f0402b0d4'}}}