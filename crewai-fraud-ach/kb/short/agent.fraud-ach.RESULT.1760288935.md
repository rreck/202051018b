```json
{
  "id": "97b8f793e94438b9",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288935,
  "host_pid": "9e6742732c60:1",
  "hash": "a7afdf21b5749a552a6e1848d2c0a365d48945bfaeeda2f9d3e650b34c64d5fa",
  "cid": "QmV1a7afdf21b5749a552a6e1848d2c0a365d48945bf",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288935,
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
      "evaluated_at": 1760288935
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
  "sig": "1ce74364af63e55a3c211750105beaa827212ef23d80a342cef405394e2d9a2e"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100275178719
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 108, 'threshold': 50, 'total_amount': 17929836, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 107, 'first_seen': 1760285765, 'matching_hash': '267c9e50b53a1b99'}}}