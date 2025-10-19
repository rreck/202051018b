```json
{
  "id": "5fcfd146f3fcad49",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291140,
  "host_pid": "9e6742732c60:1",
  "hash": "d017ff3f51377fc3259fb19572dd6f3e09fd9bf9b74e0704d639dfaabb72bef1",
  "cid": "QmV1d017ff3f51377fc3259fb19572dd6f3e09fd9bf9",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291140,
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
      "evaluated_at": 1760291140
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
  "sig": "4e16b6ffd411c9d14ac58fbda2b7d6d67805600da9b434169724b3083474ffaf"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000240863608
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 168, 'threshold': 50, 'total_amount': 31179960, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 167, 'first_seen': 1760285763, 'matching_hash': '74bcaa5b0fcf4d77'}}}