```json
{
  "id": "6e8c206a8121a67a",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293185,
  "host_pid": "9e6742732c60:1",
  "hash": "5bf0279ff3358a0ffc122e248d2c0aca4e2b4f764d4b5bb5124f1cee193cc06d",
  "cid": "QmV15bf0279ff3358a0ffc122e248d2c0aca4e2b4f76",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293185,
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
      "evaluated_at": 1760293185
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
  "sig": "7e884d3aff4e998533f9bf6c301d3141a7242961edc3e761baa74f4dc6b902a5"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000027165618
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 213, 'threshold': 50, 'total_amount': 55676709, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 212, 'first_seen': 1760285763, 'matching_hash': '01e7bf5fcf2bbeec'}}}