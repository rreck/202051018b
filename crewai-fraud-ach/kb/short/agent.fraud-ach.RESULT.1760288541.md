```json
{
  "id": "e8effcd3264e7c3d",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288541,
  "host_pid": "9e6742732c60:1",
  "hash": "ac277e7c4ca48db6a546ae92897a9b2521f91add847a0b4cf786396be995f3d8",
  "cid": "QmV1ac277e7c4ca48db6a546ae92897a9b2521f91add",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288541,
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
      "evaluated_at": 1760288541
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
  "sig": "22e93e8513880457367f7ada676dfb5263c5f2134c8279e9593f343c53caf4c0"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000241355402
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 96, 'threshold': 50, 'total_amount': 15639648, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 95, 'first_seen': 1760285765, 'matching_hash': '58524718dce63a85'}}}