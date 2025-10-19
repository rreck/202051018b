```json
{
  "id": "b150804718d2c023",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291447,
  "host_pid": "9e6742732c60:1",
  "hash": "b4899023859ed83c34bfd5648551c96ddfc77cd3ec4c7c8e81802439d5e3a6cc",
  "cid": "QmV1b4899023859ed83c34bfd5648551c96ddfc77cd3",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291447,
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
      "evaluated_at": 1760291448
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
  "sig": "4f3b660b531638ab1378d66d7c52ba6f2ca71bd34d54985143ba243aa0d0ff9c"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009590785424
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 175, 'threshold': 50, 'total_amount': 11855025, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 174, 'first_seen': 1760285763, 'matching_hash': 'b02577e012abfee0'}}}