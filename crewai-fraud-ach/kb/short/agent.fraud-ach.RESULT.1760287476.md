```json
{
  "id": "c9a18b554aeb5a0d",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287476,
  "host_pid": "9e6742732c60:1",
  "hash": "b58affe16bfad1a06d04ebb191694704454353f2fd0a9f73948115be388c68ea",
  "cid": "QmV1b58affe16bfad1a06d04ebb191694704454353f2",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287476,
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
      "evaluated_at": 1760287476
    }
  },
  "sources": [],
  "edges": [],
  "metrics": {},
  "thresholds": {},
  "tags": [
    "fraud",
    "duplicate_transaction",
    "risk_high"
  ],
  "sig": "28171460b45c44b2385cdd9563e39adbf6b5ad7be996a5bcaf2c223df00d4093"
}
```

Fraud detected: duplicate_transaction (score: 78)
Transaction: 122105156608425
Details: {'velocity': {'fraud_detected': True, 'risk_score': 72, 'details': {'transaction_count': 61, 'threshold': 50, 'total_amount': 19413128, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 60, 'first_seen': 1760285765, 'matching_hash': '07039b94da8bf942'}}}