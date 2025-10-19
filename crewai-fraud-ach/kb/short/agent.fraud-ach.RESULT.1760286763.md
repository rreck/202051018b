```json
{
  "id": "ba2e409d5d4ff1ce",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760286763,
  "host_pid": "9e6742732c60:1",
  "hash": "2835639f9318f5b615a3489dff85955cd8b49f04e83d34c43de9f880c8977718",
  "cid": "QmV12835639f9318f5b615a3489dff85955cd8b49f04",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760286763,
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
      "evaluated_at": 1760286763
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
  "sig": "40c12ee77d6086006ed5ee1476bd8c284bfd8d9c0fa4134e49cb6be1095dd8d1"
}
```

Fraud detected: duplicate_transaction (score: 85)
Transaction: 021000020807792
Details: {'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 35, 'first_seen': 1760285764, 'matching_hash': '8390351bce6e669b'}}}