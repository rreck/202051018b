```json
{
  "id": "5dcaee5e3b98f7fe",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294569,
  "host_pid": "9e6742732c60:1",
  "hash": "2d592ebbe19bdce2f55ddd2f4c9997c2ea260b076cec39777003d4c2dbc56462",
  "cid": "QmV12d592ebbe19bdce2f55ddd2f4c9997c2ea260b07",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294569,
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
      "evaluated_at": 1760294569
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
  "sig": "24420d1f5b45e885e731f3419913db1450818225ef730651a4220102d670adf5"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000248025724
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 240, 'threshold': 50, 'total_amount': 27210720, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 239, 'first_seen': 1760285764, 'matching_hash': 'cc12810353983743'}}}