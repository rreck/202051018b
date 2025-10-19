```json
{
  "id": "2cc646be0f00296d",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292874,
  "host_pid": "9e6742732c60:1",
  "hash": "5362837dad09ae703367d2367d92007944455e4da50c0fb864cec19b52d74860",
  "cid": "QmV15362837dad09ae703367d2367d92007944455e4d",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292874,
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
      "evaluated_at": 1760292874
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
  "sig": "fb3b70ec8207b393312295b4ac690d16ff2e6a8c0f94626b46b618158e889ebb"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000246128124
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 207, 'threshold': 50, 'total_amount': 51750000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 206, 'first_seen': 1760285763, 'matching_hash': 'd8f9033e4ee0a57f'}}}