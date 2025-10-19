```json
{
  "id": "63fef43e364ffcfc",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293577,
  "host_pid": "9e6742732c60:1",
  "hash": "92d09197b43c7383d94d3283286f82e0cdd074badbddb8b9bfd90ee2cc1e67d9",
  "cid": "QmV192d09197b43c7383d94d3283286f82e0cdd074ba",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293577,
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
      "evaluated_at": 1760293577
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
  "sig": "5cf817b2d8d3bd375427c6d75a5e74f140d784b5188ba6e207e4c30888ee4bb1"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000028860438
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 221, 'threshold': 50, 'total_amount': 64865268, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 220, 'first_seen': 1760285763, 'matching_hash': '1ce58b471eab5597'}}}