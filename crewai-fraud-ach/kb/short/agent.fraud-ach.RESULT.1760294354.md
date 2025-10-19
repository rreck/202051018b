```json
{
  "id": "95c6ab2e225af852",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294354,
  "host_pid": "9e6742732c60:1",
  "hash": "d6c632067fa09a21c908798d6ac81c4c0d5d41eaebfd52147688956cf286770c",
  "cid": "QmV1d6c632067fa09a21c908798d6ac81c4c0d5d41ea",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294354,
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
      "evaluated_at": 1760294354
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
  "sig": "661f8a70efce61b0b88401852b97b1bf5ac2b4f3247507ffd1475df0fcb822d1"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105156760115
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 236, 'threshold': 50, 'total_amount': 75702192, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 235, 'first_seen': 1760285764, 'matching_hash': '84a7174d04c2e814'}}}