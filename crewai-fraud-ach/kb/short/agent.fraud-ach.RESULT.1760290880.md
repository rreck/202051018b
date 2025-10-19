```json
{
  "id": "35a786dafd6f621d",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290880,
  "host_pid": "9e6742732c60:1",
  "hash": "aefc45e73e4978c3d005ab3bc4b80c9673939cd409f4a82b0ad03d2749ee2a98",
  "cid": "QmV1aefc45e73e4978c3d005ab3bc4b80c9673939cd4",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290880,
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
      "evaluated_at": 1760290880
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
  "sig": "27a2345a6a7a812b0e6df518b0c1aa73bcb7ba06b6161edde98df88d4b887b75"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105156608425
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 161, 'threshold': 50, 'total_amount': 51237928, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 160, 'first_seen': 1760285765, 'matching_hash': '07039b94da8bf942'}}}