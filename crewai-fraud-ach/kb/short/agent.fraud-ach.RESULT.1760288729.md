```json
{
  "id": "cb9785997fddebcf",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288729,
  "host_pid": "9e6742732c60:1",
  "hash": "7dca1df485233f5d330b1cf6884b0946ae353edcacc1e68a174f75dfa53c7c18",
  "cid": "QmV17dca1df485233f5d330b1cf6884b0946ae353edc",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288729,
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
      "evaluated_at": 1760288729
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
  "sig": "ef22f93ca29fa24494c393a88a79925979a34650b2563247d0d2f4bfb7505dfa"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000241250323
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 102, 'threshold': 50, 'total_amount': 10097286, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 101, 'first_seen': 1760285763, 'matching_hash': 'd18939bbbb7c2a14'}}}