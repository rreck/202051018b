```json
{
  "id": "e9a6161c715c9097",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290097,
  "host_pid": "9e6742732c60:1",
  "hash": "fc2560d113a7ee2e93268ce22775a719ff86b3ea9fa57102fa4a1dfc2bb92b51",
  "cid": "QmV1fc2560d113a7ee2e93268ce22775a719ff86b3ea",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290097,
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
      "evaluated_at": 1760290097
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
  "sig": "12a65ec2397ecd0f975feb30fe41655d11bd3ce1f04f3d31879dfbdf48501812"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009593563572
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 141, 'threshold': 50, 'total_amount': 22751337, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 140, 'first_seen': 1760285765, 'matching_hash': 'b3bf50e818486c57'}}}