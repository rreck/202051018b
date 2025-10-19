```json
{
  "id": "ddd44b5789175374",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293000,
  "host_pid": "9e6742732c60:1",
  "hash": "622868a12826efecb2564f55ff01ba89891627230190c26b8061a48ffdbca08f",
  "cid": "QmV1622868a12826efecb2564f55ff01ba8989162723",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293000,
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
      "evaluated_at": 1760293000
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
  "sig": "78bd5c0b8ce488ba8acf2b4768ecf52d385f179d08572c0075da8fd08933f1fa"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105154242410
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 209, 'threshold': 50, 'total_amount': 12132241, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 208, 'first_seen': 1760285765, 'matching_hash': '26a9af32f02bfdfc'}}}