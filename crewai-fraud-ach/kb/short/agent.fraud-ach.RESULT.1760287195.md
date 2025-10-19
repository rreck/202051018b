```json
{
  "id": "1e13a5331a2907b6",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287195,
  "host_pid": "9e6742732c60:1",
  "hash": "f016ff76c005d7881c72cc41f4dc6968462b1a5fe62b7278a52ae296f9d04f96",
  "cid": "QmV1f016ff76c005d7881c72cc41f4dc6968462b1a5f",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287195,
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
      "evaluated_at": 1760287195
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
  "sig": "bf82b9f9481a7486459376c4e7d04574f7da8e12636a6786adf1c8d5222f0fc0"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 031201462224628
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'transaction_count': 51, 'threshold': 50, 'total_amount': 11882490, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 50, 'first_seen': 1760285765, 'matching_hash': '4ca3be34af08dccb'}}}