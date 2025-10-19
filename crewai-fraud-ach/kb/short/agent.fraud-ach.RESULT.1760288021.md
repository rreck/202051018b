```json
{
  "id": "7dfdba7a4daecdbe",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288021,
  "host_pid": "9e6742732c60:1",
  "hash": "8ad87963da0b819b07d3b08c6d61cb89d7b3247a771b63c8c64ed84f14cfc266",
  "cid": "QmV18ad87963da0b819b07d3b08c6d61cb89d7b3247a",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288021,
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
      "evaluated_at": 1760288021
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
  "sig": "617a1a944771ee5e7d42ec8bdf060af60ebd79777c8b454266642a3b732ebaaf"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009590136300
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 80, 'threshold': 50, 'total_amount': 39634160, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 79, 'first_seen': 1760285764, 'matching_hash': '2d6fc2065b3c1287'}}}