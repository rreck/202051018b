```json
{
  "id": "f38850ae28e4fe11",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293123,
  "host_pid": "9e6742732c60:1",
  "hash": "42eae13202b5294b0101c75ec135ec74767f970bd12cac8f7cbb327d363cde69",
  "cid": "QmV142eae13202b5294b0101c75ec135ec74767f970b",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293123,
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
      "evaluated_at": 1760293123
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
  "sig": "13e7a0b1cee945727e2842b0b3c9c8b0af2a20a92438c002bc780924dc413605"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100274968720
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 212, 'threshold': 50, 'total_amount': 79104408, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 211, 'first_seen': 1760285763, 'matching_hash': '69fe72c937d65071'}}}