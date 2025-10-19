```json
{
  "id": "e4383d9142f2610b",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287792,
  "host_pid": "9e6742732c60:1",
  "hash": "2d363a0e73b6126bc2a742b5d719e82298b0e6bbcf37f0fe6d165359f07dfb00",
  "cid": "QmV12d363a0e73b6126bc2a742b5d719e82298b0e6bb",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287792,
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
      "evaluated_at": 1760287792
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
  "sig": "c35ae621ef057fac6918b72089dea5c0da29a8187df976ba04892cd2b449ce2e"
}
```

Fraud detected: duplicate_transaction (score: 89)
Transaction: 121000241265060
Details: {'velocity': {'fraud_detected': True, 'risk_score': 94, 'details': {'transaction_count': 72, 'threshold': 50, 'total_amount': 32857272, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 71, 'first_seen': 1760285765, 'matching_hash': '7bee400a4c5e15b1'}}}