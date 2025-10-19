```json
{
  "id": "5084642b4461d462",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290422,
  "host_pid": "9e6742732c60:1",
  "hash": "30f3bb1dd426f88424d9695728faa004fba911a168c97d75d01d5ae03bcf7683",
  "cid": "QmV130f3bb1dd426f88424d9695728faa004fba911a1",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290422,
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
      "evaluated_at": 1760290422
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
  "sig": "76bac095f2cea72ff95cc30f73fba2f42947f170dc96edc8e28f10aff0902fc9"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009596116036
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 150, 'threshold': 50, 'total_amount': 37500000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 149, 'first_seen': 1760285763, 'matching_hash': 'e2bf4d89584c6445'}}}