```json
{
  "id": "a580f8f4655ff3a9",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287381,
  "host_pid": "9e6742732c60:1",
  "hash": "00cbafab5a56dfa8a97f093a40cc44782aa881617028ef2ec010668c02648023",
  "cid": "QmV100cbafab5a56dfa8a97f093a40cc44782aa88161",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287381,
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
      "evaluated_at": 1760287381
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "duplicate_transaction",
    "risk_high"
  ],
  "sig": "ee8af22e088fd2a059a862e9ba0a441420ff5f905f9c4e387fc611c4e3aafff2"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 121000243367348
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'transaction_count': 58, 'threshold': 50, 'total_amount': 18838864, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 57, 'first_seen': 1760285765, 'matching_hash': 'a37b6eb1b4e3b31b'}}}