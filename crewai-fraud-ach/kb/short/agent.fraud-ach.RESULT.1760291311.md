```json
{
  "id": "8cb1d7ef230f1f27",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291311,
  "host_pid": "9e6742732c60:1",
  "hash": "ed53c937c0a520953ecbaa019ce90e4b5ed245ac44dd291f9bda58390e557f9f",
  "cid": "QmV1ed53c937c0a520953ecbaa019ce90e4b5ed245ac",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291311,
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
      "evaluated_at": 1760291311
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
  "sig": "2ce8fdece134c8571cd162273359271643b9e50b9020203dbeab044b2c26c8a9"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100278619879
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 172, 'threshold': 50, 'total_amount': 58257604, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 171, 'first_seen': 1760285763, 'matching_hash': 'bfc334a18daf8fbf'}}}