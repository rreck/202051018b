```json
{
  "id": "ff27bcc1b4d9fb70",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289086,
  "host_pid": "9e6742732c60:1",
  "hash": "217c7d31ec8ffdbca71cf4c27fc2e24f1d8693c2eb6de467eb0bc4528d3fdaa3",
  "cid": "QmV1217c7d31ec8ffdbca71cf4c27fc2e24f1d8693c2",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289086,
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
      "evaluated_at": 1760289086
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
  "sig": "47249af1c598c58779da3896bc3c589253b0d9b466a9d1b58e3aaa0dcd5ab087"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201465523405
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 113, 'threshold': 50, 'total_amount': 33073179, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 112, 'first_seen': 1760285764, 'matching_hash': '5adc701fe9b49cb3'}}}