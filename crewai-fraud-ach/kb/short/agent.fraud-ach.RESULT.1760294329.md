```json
{
  "id": "5c0f5cba2fd3ef7b",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294329,
  "host_pid": "9e6742732c60:1",
  "hash": "18b2d6b87fdc52ce58cd131ce6706057d0fe987eca0611ab949f917ad06baca5",
  "cid": "QmV118b2d6b87fdc52ce58cd131ce6706057d0fe987e",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294329,
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
      "evaluated_at": 1760294329
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
  "sig": "f9afb6ebc74976e2270ec63873d20d3977710791de3a4f9c7a5c3a2f760b78c9"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000025820321
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 236, 'threshold': 50, 'total_amount': 60845048, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 235, 'first_seen': 1760285763, 'matching_hash': 'cf65bb25527720c5'}}}