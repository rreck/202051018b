```json
{
  "id": "b1f0c11174c68781",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290745,
  "host_pid": "9e6742732c60:1",
  "hash": "a975a980ee4f98cce5561c80676bb22bd71b955f98b0ba43480bbf99d8a1b3f9",
  "cid": "QmV1a975a980ee4f98cce5561c80676bb22bd71b955f",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290745,
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
      "evaluated_at": 1760290745
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
  "sig": "d61c84a6d3d842b2d2b402393ae1752267c8623691d3a833a5b5af627347d961"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100279738088
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 158, 'threshold': 50, 'total_amount': 23473744, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 157, 'first_seen': 1760285763, 'matching_hash': '31a7269ac1c5c77d'}}}