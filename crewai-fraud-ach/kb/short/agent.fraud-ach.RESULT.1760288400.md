```json
{
  "id": "31ad32dbc1749d57",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288400,
  "host_pid": "9e6742732c60:1",
  "hash": "c1128cf59824a89eac88698e5034aedc61ef49d32c8a363397e7162d1d8a09cb",
  "cid": "QmV1c1128cf59824a89eac88698e5034aedc61ef49d3",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288400,
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
      "evaluated_at": 1760288400
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
  "sig": "8e6d1e2aed883cc40ab2d5241b642a0013877af9a8a8f76290858b7b3ba8550d"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105158912506
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 92, 'threshold': 50, 'total_amount': 14155212, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 91, 'first_seen': 1760285765, 'matching_hash': 'bcd6f6796bd6b696'}}}