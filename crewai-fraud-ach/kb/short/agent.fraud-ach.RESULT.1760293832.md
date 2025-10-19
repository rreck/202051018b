```json
{
  "id": "7a75a9c363a16ff6",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293832,
  "host_pid": "9e6742732c60:1",
  "hash": "b0edd9b32e528c333c195968f2f4062977b86c310fd3cba2e0f0ff1a11409974",
  "cid": "QmV1b0edd9b32e528c333c195968f2f4062977b86c31",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293832,
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
      "evaluated_at": 1760293832
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
  "sig": "a9154194ff1d13e7be61c420bcc4135232b074a8f72c67675b4fa879eb1054aa"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105159548599
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 226, 'threshold': 50, 'total_amount': 22600000, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 225, 'first_seen': 1760285764, 'matching_hash': '3450667ce2814f1a'}}}