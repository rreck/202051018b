```json
{
  "id": "133443903c7c2fc4",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292972,
  "host_pid": "9e6742732c60:1",
  "hash": "16cb1cfe6780b506eabbb08fa944549e6b7d2e2d340d788c1c4f4a9ee029f838",
  "cid": "QmV116cb1cfe6780b506eabbb08fa944549e6b7d2e2d",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292972,
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
      "evaluated_at": 1760292972
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
  "sig": "daeb96792bbe7777707f41710a2333efe9581eb34d165f6364c069c41935dc3d"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000022959454
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 209, 'threshold': 50, 'total_amount': 31436526, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 208, 'first_seen': 1760285763, 'matching_hash': 'd9e1e1b77e5bc9b7'}}}