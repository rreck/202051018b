```json
{
  "id": "4574a7f06b125570",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294118,
  "host_pid": "9e6742732c60:1",
  "hash": "37c0131d55d960675e208a19f07ce84cdf54eb7c0c2863de6d7a82db3fd80303",
  "cid": "QmV137c0131d55d960675e208a19f07ce84cdf54eb7c",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294118,
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
      "evaluated_at": 1760294118
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
  "sig": "60b91a868826011791bdb02585e717efff7c072513f469aa6a80693fb2723ea1"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000031117260
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 232, 'threshold': 50, 'total_amount': 19169000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 231, 'first_seen': 1760285763, 'matching_hash': '467ec1c9bc787c3f'}}}