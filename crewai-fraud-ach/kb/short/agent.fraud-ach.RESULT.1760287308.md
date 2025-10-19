```json
{
  "id": "d28d879a4d1978b9",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287308,
  "host_pid": "9e6742732c60:1",
  "hash": "3952b0ccce76ba662b4757339bf17a01e1dff819bcd2fda5c1e1039214ec238a",
  "cid": "QmV13952b0ccce76ba662b4757339bf17a01e1dff819",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287308,
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
      "evaluated_at": 1760287308
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
  "sig": "28d7b3dcdf61da054886abcbe618d8f4e0150e2b74290b0339ae2e801bb916ae"
}
```

Fraud detected: duplicate_transaction (score: 77)
Transaction: 122105156608425
Details: {'velocity': {'fraud_detected': True, 'risk_score': 70, 'details': {'transaction_count': 55, 'threshold': 50, 'total_amount': 17503640, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 54, 'first_seen': 1760285765, 'matching_hash': '07039b94da8bf942'}}}