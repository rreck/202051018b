```json
{
  "id": "e3c928bed37d0cad",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291164,
  "host_pid": "9e6742732c60:1",
  "hash": "0c49171851bc82879d943f7b1894c60176673148c93f58e283dd3f67f71b3a37",
  "cid": "QmV10c49171851bc82879d943f7b1894c60176673148",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291164,
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
      "evaluated_at": 1760291164
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
  "sig": "7d1c44410accc094dd5e0c51e79609b2a0446c51284a0a690a4545ebaa5f21ca"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000022683015
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 168, 'threshold': 50, 'total_amount': 41107920, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 167, 'first_seen': 1760285765, 'matching_hash': 'a34aa564f21aebc1'}}}