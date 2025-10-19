```json
{
  "id": "912f4c2740e65024",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293601,
  "host_pid": "9e6742732c60:1",
  "hash": "444a62c7edca62a0441a48d26cf8286f841e8b8ea245e1e231a8e4ae30391f76",
  "cid": "QmV1444a62c7edca62a0441a48d26cf8286f841e8b8e",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293601,
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
      "evaluated_at": 1760293601
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
  "sig": "9d5b00de018f1ee145a549ffcc9b83683c4c07833a19edfce78ed9f7b1ea1f23"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100272156319
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 222, 'threshold': 50, 'total_amount': 17068248, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 221, 'first_seen': 1760285763, 'matching_hash': '6d26908715188c7a'}}}