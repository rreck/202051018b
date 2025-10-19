```json
{
  "id": "e90ecdb7fa0889a3",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294536,
  "host_pid": "9e6742732c60:1",
  "hash": "44e164b45a2229b0a1518936317b5c1694c0bc3b5365f5271fdd0a41d54214c2",
  "cid": "QmV144e164b45a2229b0a1518936317b5c1694c0bc3b",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294536,
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
      "evaluated_at": 1760294536
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
  "sig": "61e4ddc0e4541be9b0c00f5b518932a17c068650edaa3562b5f0d3bba40bd09d"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009590857246
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 240, 'threshold': 50, 'total_amount': 85057440, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 239, 'first_seen': 1760285763, 'matching_hash': 'f091f96bdb04a5bf'}}}