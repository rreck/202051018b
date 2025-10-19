```json
{
  "id": "dbcf35db99494f6f",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292596,
  "host_pid": "9e6742732c60:1",
  "hash": "11092d17fa5c1f2b00b3e599585ea697aac36d7eefaffbb7e8a9c72e6c94fa61",
  "cid": "QmV111092d17fa5c1f2b00b3e599585ea697aac36d7e",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292596,
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
      "evaluated_at": 1760292596
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
  "sig": "1fdef5437fb92504232e62f8c59e348a74d2752379b2c23ff805eec5db464b60"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100276330055
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 201, 'threshold': 50, 'total_amount': 90542058, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 200, 'first_seen': 1760285763, 'matching_hash': '5c86a9c2afef995d'}}}