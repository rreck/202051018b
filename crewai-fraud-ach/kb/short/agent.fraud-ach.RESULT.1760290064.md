```json
{
  "id": "01bdaa15b1c3cfe4",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290064,
  "host_pid": "9e6742732c60:1",
  "hash": "34b3adf21a73f8ea092fcb8f480c2a71f2b6153ed3c25a29f488346cda553ff4",
  "cid": "QmV134b3adf21a73f8ea092fcb8f480c2a71f2b6153e",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290064,
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
      "evaluated_at": 1760290064
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
  "sig": "5ec01b5b01526834b37eee52431da0bfbc10735cfcba84fb632a0519e4e30f7d"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105151005829
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 140, 'threshold': 50, 'total_amount': 37880360, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 139, 'first_seen': 1760285765, 'matching_hash': 'ea26f24e3d1967f5'}}}