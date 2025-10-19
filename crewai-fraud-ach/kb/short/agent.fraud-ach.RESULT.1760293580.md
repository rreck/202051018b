```json
{
  "id": "a560ab041f46c7f7",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293580,
  "host_pid": "9e6742732c60:1",
  "hash": "5dd4b5291ffbb696741e6302c79007e97386c03ed68f594adce46006ff16506c",
  "cid": "QmV15dd4b5291ffbb696741e6302c79007e97386c03e",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293580,
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
      "evaluated_at": 1760293580
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
  "sig": "0c654e7fc6e8dc39495b102878a0affafcbb25018c4aeb2e3c8a1b83d7f11956"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000243277611
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 221, 'threshold': 50, 'total_amount': 31115474, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 220, 'first_seen': 1760285763, 'matching_hash': '2d64263c5765c58b'}}}