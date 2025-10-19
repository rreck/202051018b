```json
{
  "id": "23b9db1edb0288eb",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291110,
  "host_pid": "9e6742732c60:1",
  "hash": "ba0a39ddfd2d91daf30a2976634285ba8a1e26c0a4527e6bf2ef5b1b90e3d62d",
  "cid": "QmV1ba0a39ddfd2d91daf30a2976634285ba8a1e26c0",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291110,
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
      "evaluated_at": 1760291110
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
  "sig": "3b68689c5a0a14ad4670bad2def8797e829c722628901a2fd38ab16eb78d982c"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000243367348
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 167, 'threshold': 50, 'total_amount': 54242936, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 166, 'first_seen': 1760285765, 'matching_hash': 'a37b6eb1b4e3b31b'}}}