```json
{
  "id": "b58a0b366dd2595e",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288928,
  "host_pid": "9e6742732c60:1",
  "hash": "ae5c92814beb3638ca1d9977146358600ae08f6e41c9096a4c089513da3e3afd",
  "cid": "QmV1ae5c92814beb3638ca1d9977146358600ae08f6e",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288928,
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
      "evaluated_at": 1760288928
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
  "sig": "7db233ef2cac69428d597c7a2f0fddb70a03e45bbf848c4f41cae465e79fa1a4"
}
```

Fraud detected: round_amount_pattern (score: 75)
Transaction: 031201462455734
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 108, 'threshold': 50, 'total_amount': 54000000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 107, 'first_seen': 1760285763, 'matching_hash': '2de7efbdf08711e2'}}, 'round_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 500000}}}