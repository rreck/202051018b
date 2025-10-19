```json
{
  "id": "84e18a83d93da8d5",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293703,
  "host_pid": "9e6742732c60:1",
  "hash": "4a68a2da529aaf8af24443454963bfa9e7cb18affba3f86a8c41a709b161efba",
  "cid": "QmV14a68a2da529aaf8af24443454963bfa9e7cb18af",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293703,
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
      "evaluated_at": 1760293703
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
  "sig": "c635b242727ff9f6f111f4efd6490055725ddbddf0bcf33c76562a9b50a3089b"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000025759024
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 224, 'threshold': 50, 'total_amount': 85731744, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 223, 'first_seen': 1760285763, 'matching_hash': 'fa026da4c6071776'}}}