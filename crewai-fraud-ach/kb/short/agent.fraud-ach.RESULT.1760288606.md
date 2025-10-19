```json
{
  "id": "2959b702ce003dd9",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288606,
  "host_pid": "9e6742732c60:1",
  "hash": "24cdcb06e44597f9b8d0ccf7251ae5a4aa525a131431511048db189583836f4f",
  "cid": "QmV124cdcb06e44597f9b8d0ccf7251ae5a4aa525a13",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288606,
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
      "evaluated_at": 1760288606
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
  "sig": "8dbfb1d4ea6f7fa133580e35a47ee183c1a6de9c46f6471061d6c40413b709a4"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000039495479
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 98, 'threshold': 50, 'total_amount': 39939312, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 97, 'first_seen': 1760285765, 'matching_hash': 'bbfd7bc59c80a282'}}}