```json
{
  "id": "08423c8b802fe413",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289977,
  "host_pid": "9e6742732c60:1",
  "hash": "d9b882c78231f444942e45f0887e1f489c83af8917ca141344411cd7b53ec60d",
  "cid": "QmV1d9b882c78231f444942e45f0887e1f489c83af89",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289977,
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
      "evaluated_at": 1760289977
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
  "sig": "ad823a74ddc031a2c3e031414bc86aa53b3021515ae37bcc03486289f3afe4c8"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000024242004
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 138, 'threshold': 50, 'total_amount': 34500000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 137, 'first_seen': 1760285764, 'matching_hash': '99660a13145cb677'}}}