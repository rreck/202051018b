```json
{
  "id": "6bdb773966ad489f",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288564,
  "host_pid": "9e6742732c60:1",
  "hash": "4e93b021908a263bd6e0b7942ce432aed6b651d2c77d052a828b9b92e25ae5ef",
  "cid": "QmV14e93b021908a263bd6e0b7942ce432aed6b651d2",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288564,
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
      "evaluated_at": 1760288564
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
  "sig": "ddd4b3af830e7821a8c546cb0e31ad3936de042e09b9cbe61e68ee1f73c1cd33"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000026203898
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 173, 'threshold': 50, 'total_amount': 72901162, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 172, 'first_seen': 1760284979, 'matching_hash': '464b48f6c600a373'}}}fraud_detected': True, 'risk_score': 95, 'details': {'routing_number': '033505362', 'validation_error': 'Invalid routing number checksum'}}}