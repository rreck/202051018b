```json
{
  "id": "b2ecca86f0425462",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288097,
  "host_pid": "9e6742732c60:1",
  "hash": "2312f2383feaef47c39b7cbe94aa8aa8c653ba29009ae5f0efc4002170e43b02",
  "cid": "QmV12312f2383feaef47c39b7cbe94aa8aa8c653ba29",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288097,
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
      "evaluated_at": 1760288097
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
  "sig": "9c21ff9dc06ca1c12d65809db11fcc55af84ee647662cf26e36d8fb821e0d762"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105156608425
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 82, 'threshold': 50, 'total_amount': 26096336, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 81, 'first_seen': 1760285765, 'matching_hash': '07039b94da8bf942'}}}