```json
{
  "id": "333f770759a545bd",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287648,
  "host_pid": "9e6742732c60:1",
  "hash": "020ab646e33ef99037f08c90ae4eac0c932964f36cd495775f03e9d0a052bf1d",
  "cid": "QmV1020ab646e33ef99037f08c90ae4eac0c932964f3",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287648,
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
      "evaluated_at": 1760287648
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
  "sig": "47373d08de2735902f61aaf7157ec05f7e60c765348aec877addcdb3f356c5f2"
}
```

Fraud detected: duplicate_transaction (score: 84)
Transaction: 122105156608425
Details: {'velocity': {'fraud_detected': True, 'risk_score': 84, 'details': {'transaction_count': 67, 'threshold': 50, 'total_amount': 21322616, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 66, 'first_seen': 1760285765, 'matching_hash': '07039b94da8bf942'}}}