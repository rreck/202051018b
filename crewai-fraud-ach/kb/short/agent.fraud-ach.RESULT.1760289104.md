```json
{
  "id": "5b736e03d2ee18fa",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289104,
  "host_pid": "9e6742732c60:1",
  "hash": "cf7bb8337955aaa6d0a00daa55079ca4e7a42c2f97b1b5870a0d815a6ebc7a28",
  "cid": "QmV1cf7bb8337955aaa6d0a00daa55079ca4e7a42c2f",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289104,
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
      "evaluated_at": 1760289104
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
  "sig": "7725985f7136722f4fd87fb156e95a00acd50d26a1bc74700840b9375f781f47"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105156608425
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 113, 'threshold': 50, 'total_amount': 35962024, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 112, 'first_seen': 1760285765, 'matching_hash': '07039b94da8bf942'}}}