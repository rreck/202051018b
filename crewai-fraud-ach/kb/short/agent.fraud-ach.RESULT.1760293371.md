```json
{
  "id": "f6be463edd6c1e1c",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293371,
  "host_pid": "9e6742732c60:1",
  "hash": "642791279cd7644a712fcf30e6e512a398431025a860138061b2932900dc5917",
  "cid": "QmV1642791279cd7644a712fcf30e6e512a398431025",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293371,
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
      "evaluated_at": 1760293371
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
  "sig": "b647779352c681c99731c7a6c9e92fa52cf08d96eebe475cf3fa08f492755f82"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 044000032539256
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 217, 'threshold': 50, 'total_amount': 107208850, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 216, 'first_seen': 1760285763, 'matching_hash': '34ea678ce834982a'}}}