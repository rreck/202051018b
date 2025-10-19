```json
{
  "id": "79b6dfdcc5359d81",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294558,
  "host_pid": "9e6742732c60:1",
  "hash": "8cbc20a10c3dad15c87e6e77146916a6e39ad5e930880fd6bd897817b7454ce0",
  "cid": "QmV18cbc20a10c3dad15c87e6e77146916a6e39ad5e9",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294558,
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
      "evaluated_at": 1760294558
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
  "sig": "c8a617eb0fb16b41fa4eec9b5a25c56165ea7f74decf149a1fa228c27eced300"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000032692891
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 316, 'threshold': 50, 'total_amount': 143646016, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 315, 'first_seen': 1760284979, 'matching_hash': '069830b10839223a'}}}