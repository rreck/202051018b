```json
{
  "id": "4dd1220ac0277e3c",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287635,
  "host_pid": "9e6742732c60:1",
  "hash": "4f53be2298e50747915122a724d7ae0fbc79ccf40dc5e96f6df132e76ee3bb79",
  "cid": "QmV14f53be2298e50747915122a724d7ae0fbc79ccf4",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287635,
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
      "evaluated_at": 1760287635
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
  "sig": "4d22ef57fc03cafd522145ca4f261d658131d0a7279d2bfb25d0fa0ed0418f6d"
}
```

Fraud detected: duplicate_transaction (score: 84)
Transaction: 031201465310802
Details: {'velocity': {'fraud_detected': True, 'risk_score': 84, 'details': {'transaction_count': 67, 'threshold': 50, 'total_amount': 25059139, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 66, 'first_seen': 1760285763, 'matching_hash': '86dc5261411570c1'}}}