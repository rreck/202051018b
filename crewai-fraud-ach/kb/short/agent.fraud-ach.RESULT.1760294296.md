```json
{
  "id": "728f9c9374647022",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294296,
  "host_pid": "9e6742732c60:1",
  "hash": "ba2ebe68a59d6e92c30aff73b19cd2d98d2fd68c9e25ef9f84bb60ee391d4940",
  "cid": "QmV1ba2ebe68a59d6e92c30aff73b19cd2d98d2fd68c",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294296,
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
      "evaluated_at": 1760294296
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
  "sig": "bd9924617571bdb76852472669441b332f92ca68f29882ec99395702e4aef544"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100271648434
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 235, 'threshold': 50, 'total_amount': 55625205, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 234, 'first_seen': 1760285763, 'matching_hash': '7a167e1c4ddc5d6e'}}}