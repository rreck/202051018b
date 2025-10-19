```json
{
  "id": "1ab2e2472beeed11",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289188,
  "host_pid": "9e6742732c60:1",
  "hash": "3c6cbba3990679afc9abe8858d98317402832b78667e5594e9f4ae3dca641a51",
  "cid": "QmV13c6cbba3990679afc9abe8858d98317402832b78",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289188,
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
      "evaluated_at": 1760289188
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "round_amount_pattern",
    "risk_high"
  ],
  "sig": "33298d56d8f28f828aa0dc0e9184c4a1c0c410b6610ccd559e8bdf5bfbd2ef19"
}
```

Fraud detected: round_amount_pattern (score: 75)
Transaction: 121000240623413
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 116, 'threshold': 50, 'total_amount': 58000000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 115, 'first_seen': 1760285764, 'matching_hash': 'b41427cac750dd0e'}}, 'round_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 500000}}}