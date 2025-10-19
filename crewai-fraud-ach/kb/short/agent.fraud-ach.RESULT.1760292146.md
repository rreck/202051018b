```json
{
  "id": "4303dda27f9cd3af",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292146,
  "host_pid": "9e6742732c60:1",
  "hash": "f3ea5bbf9bb4162777c78a8f0ba7062df84c284c1344a67fb0d0e98099891fb8",
  "cid": "QmV1f3ea5bbf9bb4162777c78a8f0ba7062df84c284c",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292146,
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
      "evaluated_at": 1760292146
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
  "sig": "70220036bfed2e19db9730e25e99777bacb5ae40cdbd2634b0da5f4934528237"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201465280061
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 191, 'threshold': 50, 'total_amount': 25402618, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 190, 'first_seen': 1760285763, 'matching_hash': '24e243e35a5cb5f6'}}}