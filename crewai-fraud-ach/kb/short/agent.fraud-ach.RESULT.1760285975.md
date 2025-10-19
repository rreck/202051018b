```json
{
  "id": "9a505bee6dc4b2d0",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760285975,
  "host_pid": "9e6742732c60:1",
  "hash": "a6734687fbd931ec7bc0cf6b3e4ab2eb0fad367d18d6664521a81852facb6eea",
  "cid": "QmV1a6734687fbd931ec7bc0cf6b3e4ab2eb0fad367d",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760285975,
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
      "evaluated_at": 1760285975
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
  "sig": "160ed758fd5440e1eb7816b13a8c393f757c3fc4f8185dd955fe2d309c992c49"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100275531952
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 86, 'threshold': 50}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 85, 'first_seen': 1760284979, 'matching_hash': '283eac5c65a068f4'}}}}}