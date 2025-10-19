```json
{
  "id": "847e9fe3a665dfc4",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293278,
  "host_pid": "9e6742732c60:1",
  "hash": "e27ac6649bf205a4ee929d6f76825b2846a91841f9ad68f996feb5d3513d33f6",
  "cid": "QmV1e27ac6649bf205a4ee929d6f76825b2846a91841",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293278,
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
      "evaluated_at": 1760293278
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
  "sig": "cabab89622de97f0644ec0cec0bbd30ddb7c16b02f125439e62a57c514ba850f"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000245569369
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 215, 'threshold': 50, 'total_amount': 51893045, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 214, 'first_seen': 1760285764, 'matching_hash': '9f2120bc546d4049'}}}