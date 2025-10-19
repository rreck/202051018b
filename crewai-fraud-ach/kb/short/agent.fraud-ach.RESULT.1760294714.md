```json
{
  "id": "c1d53b95e3ac31af",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294714,
  "host_pid": "9e6742732c60:1",
  "hash": "6e6decaa9d2972f561e9e15f15308d9d529187b99a0852d0e6c031c648cdeec4",
  "cid": "QmV16e6decaa9d2972f561e9e15f15308d9d529187b9",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294714,
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
      "evaluated_at": 1760294714
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
  "sig": "c513e815060ca0b95e5c53fe3c058a1b3be92ca6e6ca357d1e17bce0b3a1a758"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100271109324
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 243, 'threshold': 50, 'total_amount': 60750000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 242, 'first_seen': 1760285764, 'matching_hash': '28f72b559ab32ea0'}}}}