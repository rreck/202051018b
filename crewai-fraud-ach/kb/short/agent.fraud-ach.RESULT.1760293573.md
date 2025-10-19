```json
{
  "id": "9d61061864fde838",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293573,
  "host_pid": "9e6742732c60:1",
  "hash": "716530e3e13f388c3deacecacae48634b318a35f53a7ba80448c3bd1e25e0a3e",
  "cid": "QmV1716530e3e13f388c3deacecacae48634b318a35f",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293573,
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
      "evaluated_at": 1760293573
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
  "sig": "88dcd2012461af2594e0241a2f2c4f0d5edfe499a7fb8229ee846ba6531cd0af"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009599908299
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 221, 'threshold': 50, 'total_amount': 97524206, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 220, 'first_seen': 1760285763, 'matching_hash': '494601c315920761'}}}