```json
{
  "id": "a1dde7fac2660756",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292591,
  "host_pid": "9e6742732c60:1",
  "hash": "182a246c4c9c4be5023900518b8dc6e498c2d59bba95d92ebc8889d0949ad105",
  "cid": "QmV1182a246c4c9c4be5023900518b8dc6e498c2d59b",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292591,
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
      "evaluated_at": 1760292591
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
  "sig": "e7f8574971e1292b870f263555720790cfec0c544cbf37845712caf8f9e80f78"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100271177223
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 201, 'threshold': 50, 'total_amount': 97215258, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 200, 'first_seen': 1760285763, 'matching_hash': 'bfc9cdfd9eceb164'}}}