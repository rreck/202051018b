```json
{
  "id": "c54173c40cf3e2ca",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290756,
  "host_pid": "9e6742732c60:1",
  "hash": "1fc653a156661a2a449d22ca44cd343efc9918a3af69180fd97e47bd20ee4acf",
  "cid": "QmV11fc653a156661a2a449d22ca44cd343efc9918a3",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290756,
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
      "evaluated_at": 1760290756
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
  "sig": "041c37348609c77f947fd72a7835c46e25a48d9ba9bebf7d73341ac2c5187185"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201467876303
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 158, 'threshold': 50, 'total_amount': 69146172, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 157, 'first_seen': 1760285765, 'matching_hash': 'ffdb832f59bf640d'}}}