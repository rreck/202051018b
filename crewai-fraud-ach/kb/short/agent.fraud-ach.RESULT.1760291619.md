```json
{
  "id": "aefaa7db974378e9",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291619,
  "host_pid": "9e6742732c60:1",
  "hash": "ce2e71d5d991e1e41fd2eb2e70d8a9c5ccc62d19a03236d590705ea87ec00d97",
  "cid": "QmV1ce2e71d5d991e1e41fd2eb2e70d8a9c5ccc62d19",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291619,
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
      "evaluated_at": 1760291619
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
  "sig": "845a2e237fdd130eefb7eb049150bda885bd932e2f5bdc0e5b37a11334987050"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000024242004
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 179, 'threshold': 50, 'total_amount': 44750000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 178, 'first_seen': 1760285764, 'matching_hash': '99660a13145cb677'}}}