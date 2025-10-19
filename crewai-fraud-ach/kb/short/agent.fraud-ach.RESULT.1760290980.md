```json
{
  "id": "7feb32671d0ad3d9",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290980,
  "host_pid": "9e6742732c60:1",
  "hash": "66dcfee2ceb0d9d2e1c31bf52d420ff5db824e3170ad7a68a917b27e4236a87c",
  "cid": "QmV166dcfee2ceb0d9d2e1c31bf52d420ff5db824e31",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290980,
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
      "evaluated_at": 1760290980
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
  "sig": "614f4847bbb4854c400e7a9671ef779089892227f8c66259ae9fd818e1158a74"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000241012804
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 164, 'threshold': 50, 'total_amount': 45288600, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 163, 'first_seen': 1760285763, 'matching_hash': 'ba9ba43773b08e05'}}}