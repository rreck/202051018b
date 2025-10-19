```json
{
  "id": "d9ae5988aa69f3db",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292188,
  "host_pid": "9e6742732c60:1",
  "hash": "db17f452ab343c6540925fbb86cb955aaa87fbb059e546bbccbe8c89294a1bb5",
  "cid": "QmV1db17f452ab343c6540925fbb86cb955aaa87fbb0",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292188,
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
      "evaluated_at": 1760292188
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
  "sig": "54da333182b70fa845468c0122e8abf2de0c7f6e48f1d55ce4c823ce00f09eb0"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000242903308
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 192, 'threshold': 50, 'total_amount': 27173184, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 191, 'first_seen': 1760285764, 'matching_hash': '3fe1582345d32257'}}}