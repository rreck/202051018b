```json
{
  "id": "b035860d26f4ae4a",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289160,
  "host_pid": "9e6742732c60:1",
  "hash": "a56344fdacafd93a6b8da7ba3a3c9bb3aea9e41e7db845c6218d85cf0e655602",
  "cid": "QmV1a56344fdacafd93a6b8da7ba3a3c9bb3aea9e41e",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289160,
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
      "evaluated_at": 1760289160
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
  "sig": "1fcf356169dd9bd5ba262b266164a3aceac1a6e31f17aad2ff436f45f56e7859"
}
```

Fraud detected: round_amount_pattern (score: 75)
Transaction: 031201460873764
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 115, 'threshold': 50, 'total_amount': 57500000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 114, 'first_seen': 1760285763, 'matching_hash': '6dda2db9e90937c1'}}, 'round_amount': {'fraud_detected': True, 'risk_score': 40, 'details': {'pattern': 'exact_thousands', 'amount': 500000}}}