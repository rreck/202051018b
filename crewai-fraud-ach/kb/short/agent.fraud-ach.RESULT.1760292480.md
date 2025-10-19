```json
{
  "id": "325f24fa9efaeb37",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292480,
  "host_pid": "9e6742732c60:1",
  "hash": "896b6503e8738f84bcaa10256b022a7d2d7612ae33b78fda977e539b0c70b9ea",
  "cid": "QmV1896b6503e8738f84bcaa10256b022a7d2d7612ae",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292480,
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
      "evaluated_at": 1760292480
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
  "sig": "75948a183bdc77c000b763aac949d7a1a21cfc6c99197f01f0f0825861d21603"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105153937190
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 198, 'threshold': 50, 'total_amount': 95973174, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 197, 'first_seen': 1760285765, 'matching_hash': '8cf441fb6328957e'}}}