```json
{
  "id": "be36b5f0626206f7",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290473,
  "host_pid": "9e6742732c60:1",
  "hash": "1228305ddd2d56f6191b4780c091e8e3aa6ba64c28bb30b00e6e0f9c867b10a8",
  "cid": "QmV11228305ddd2d56f6191b4780c091e8e3aa6ba64c",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290473,
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
      "evaluated_at": 1760290473
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
  "sig": "96e9df80a1d67360b8d7660548d2d31f394ea6c60dae9be6f80b1e41358cecd2"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000027165618
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 151, 'threshold': 50, 'total_amount': 39470343, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 150, 'first_seen': 1760285763, 'matching_hash': '01e7bf5fcf2bbeec'}}}