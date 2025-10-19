```json
{
  "id": "d8f6428bfcbeb050",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291602,
  "host_pid": "9e6742732c60:1",
  "hash": "1a7a9c4fed8b627704bb17c3e3caf5af7501f4ebf74cfdfedabeac0275fc6dfa",
  "cid": "QmV11a7a9c4fed8b627704bb17c3e3caf5af7501f4eb",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291602,
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
      "evaluated_at": 1760291602
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
  "sig": "cd53baff44138e5d5067009577e6b25a4141042dde283031e5c8ef8275e6612e"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000248845664
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 179, 'threshold': 50, 'total_amount': 41996443, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 178, 'first_seen': 1760285763, 'matching_hash': 'd68dab2741390ae3'}}}