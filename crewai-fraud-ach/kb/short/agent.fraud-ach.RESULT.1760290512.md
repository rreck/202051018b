```json
{
  "id": "f227c25fe882fa73",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290512,
  "host_pid": "9e6742732c60:1",
  "hash": "b6ea72cd0128e06d3d81bc51132510e558a3ca18303e1f90240a931895cff903",
  "cid": "QmV1b6ea72cd0128e06d3d81bc51132510e558a3ca18",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290512,
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
      "evaluated_at": 1760290512
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
  "sig": "1daa96d62f1c72889f5a2baa4eef780b80598dedb14f312840298b3bb8867a2e"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000027165618
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 152, 'threshold': 50, 'total_amount': 39731736, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 151, 'first_seen': 1760285763, 'matching_hash': '01e7bf5fcf2bbeec'}}}