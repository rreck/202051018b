```json
{
  "id": "8ea066b3d3aee4a8",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294414,
  "host_pid": "9e6742732c60:1",
  "hash": "c99fc56fa488d64320060456a8e14cdbeeda490d66ca82fd1ed576102a79c7fc",
  "cid": "QmV1c99fc56fa488d64320060456a8e14cdbeeda490d",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294414,
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
      "evaluated_at": 1760294414
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
  "sig": "4364045808990cfbe4adcd34c17d3edd8349851f4d132e2565406d0fe4d6208d"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000025198728
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 237, 'threshold': 50, 'total_amount': 22239606, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 236, 'first_seen': 1760285765, 'matching_hash': 'ff4b51392b1a88ca'}}}