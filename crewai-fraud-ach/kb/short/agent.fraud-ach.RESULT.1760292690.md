```json
{
  "id": "375006a8aa672ebb",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292690,
  "host_pid": "9e6742732c60:1",
  "hash": "3a21b5f9300c5b056fa9f1945f43410055aa8a23f11bbd263bbe61a1fcf813cf",
  "cid": "QmV13a21b5f9300c5b056fa9f1945f43410055aa8a23",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292690,
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
      "evaluated_at": 1760292690
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
  "sig": "80661f29207bd1631742c4ece2cb8b2068b040ad062a507bcdc8526911dc6ee7"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000249232395
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 203, 'threshold': 50, 'total_amount': 74102308, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 202, 'first_seen': 1760285764, 'matching_hash': '83f71011b8a0f970'}}}