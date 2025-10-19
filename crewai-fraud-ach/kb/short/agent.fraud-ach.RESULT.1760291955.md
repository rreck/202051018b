```json
{
  "id": "0a16a5949a801bee",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291955,
  "host_pid": "9e6742732c60:1",
  "hash": "64286e7bc43294eca387def51399254f84808037872c6d299a75be7603b798fc",
  "cid": "QmV164286e7bc43294eca387def51399254f84808037",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291955,
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
      "evaluated_at": 1760291955
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
  "sig": "5f21e515b64990932b174ff0555eb96ebf7ceaff981005462a0db7879aa87f29"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000249881393
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 187, 'threshold': 50, 'total_amount': 75664875, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 186, 'first_seen': 1760285763, 'matching_hash': '72e20928773d23d6'}}}