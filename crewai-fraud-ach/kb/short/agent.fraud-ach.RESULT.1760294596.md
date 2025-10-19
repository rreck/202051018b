```json
{
  "id": "71d5e2873ae8e801",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294596,
  "host_pid": "9e6742732c60:1",
  "hash": "32864af06261dacc6cc9eac52034e4ff6306c957968614ad19c8c40bac44018e",
  "cid": "QmV132864af06261dacc6cc9eac52034e4ff6306c957",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294596,
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
      "evaluated_at": 1760294596
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
  "sig": "cb351b504813fef1acd2f08fa48e0894ea678fe8c50aa7455737ade0a19a8441"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000025664709
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 241, 'threshold': 50, 'total_amount': 24810227, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 240, 'first_seen': 1760285764, 'matching_hash': '5cc83e27ca9ca801'}}}}