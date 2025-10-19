```json
{
  "id": "f36e271e42da7352",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293407,
  "host_pid": "9e6742732c60:1",
  "hash": "416625208195c544c761e171b36bf04ab63022c85479dbded6fccd794f078b02",
  "cid": "QmV1416625208195c544c761e171b36bf04ab63022c8",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293407,
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
      "evaluated_at": 1760293407
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
  "sig": "98242f912d18f667b3c3ac14de48fb0d0c051ec193d8c6fc4e3ea2619415780e"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000022696777
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 218, 'threshold': 50, 'total_amount': 106183876, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 217, 'first_seen': 1760285763, 'matching_hash': 'bb01014ea9b32f36'}}}