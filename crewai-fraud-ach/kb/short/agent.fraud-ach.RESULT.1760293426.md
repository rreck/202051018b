```json
{
  "id": "2a974096f12bc30b",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293426,
  "host_pid": "9e6742732c60:1",
  "hash": "db47942d50224d02607c87cf1cba793d28d1b1e9398207443df75d4e9829af10",
  "cid": "QmV1db47942d50224d02607c87cf1cba793d28d1b1e9",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293426,
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
      "evaluated_at": 1760293426
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
  "sig": "4ea9e94e80181eb1da1fbbe13b02a67af2e20fa30af5464016680cedcdbf31f1"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000034789126
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 294, 'threshold': 50, 'total_amount': 62933934, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 293, 'first_seen': 1760284979, 'matching_hash': '5ec025bcbfaa0fd9'}}}