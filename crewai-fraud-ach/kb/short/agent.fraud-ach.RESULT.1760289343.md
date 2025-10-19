```json
{
  "id": "30c5faf1e8599ace",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760289343,
  "host_pid": "9e6742732c60:1",
  "hash": "859901320166349c354a7a0c456a91c3053dfd9d177e93f649b2895c189da723",
  "cid": "QmV1859901320166349c354a7a0c456a91c3053dfd9d",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760289343,
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
      "evaluated_at": 1760289343
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
  "sig": "77f4282f34659220928e7b51e476838d9066f859c151fa19cebeafc272f7a982"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105156608425
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 120, 'threshold': 50, 'total_amount': 38189760, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 119, 'first_seen': 1760285765, 'matching_hash': '07039b94da8bf942'}}}