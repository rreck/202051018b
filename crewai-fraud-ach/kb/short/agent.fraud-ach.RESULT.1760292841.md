```json
{
  "id": "148ab56b7e3c07eb",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292841,
  "host_pid": "9e6742732c60:1",
  "hash": "4d84c347c25a5cda829516723fa61de92e7dfd43442885e409f33ab4fefdbfff",
  "cid": "QmV14d84c347c25a5cda829516723fa61de92e7dfd43",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292841,
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
      "evaluated_at": 1760292841
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
  "sig": "88e5f7100ff702092465ff3331379b69657cc06bdb60341fe786a21ec6cfca38"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000032306947
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 206, 'threshold': 50, 'total_amount': 15883630, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 205, 'first_seen': 1760285763, 'matching_hash': '0095d1181b74b3e8'}}}