```json
{
  "id": "3c47ee65a2a621ee",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294110,
  "host_pid": "9e6742732c60:1",
  "hash": "6ba71de425721e11e5b16eecbfc822c54a0ecee27b437c77d1feec8fca315ebf",
  "cid": "QmV16ba71de425721e11e5b16eecbfc822c54a0ecee2",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294110,
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
      "evaluated_at": 1760294111
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
  "sig": "cc0519e34d0b2ed7f73d2417df3cf949ee06fd6bfdd72fa10f558ba3d8dbbfa5"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201464951398
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 232, 'threshold': 50, 'total_amount': 62656472, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 231, 'first_seen': 1760285763, 'matching_hash': '40dace0dcec07d54'}}}