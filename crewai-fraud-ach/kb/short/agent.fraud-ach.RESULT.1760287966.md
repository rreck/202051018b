```json
{
  "id": "2aa21813cfd9c571",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287966,
  "host_pid": "9e6742732c60:1",
  "hash": "fe2cbe0958fba581aa1dbf6a6932372afbbffc630fce6c6b6d0a3a23d14f9b33",
  "cid": "QmV1fe2cbe0958fba581aa1dbf6a6932372afbbffc63",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287966,
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
      "evaluated_at": 1760287966
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
  "sig": "f34a26c786fe39dc32ad37e74cacc5339d0f9c40bccd7be56e40ff3bd8195764"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000027276119
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 78, 'threshold': 50, 'total_amount': 21752640, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 77, 'first_seen': 1760285763, 'matching_hash': 'ec114b5b29b7d5ae'}}}