```json
{
  "id": "e87361524f0ec335",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294628,
  "host_pid": "9e6742732c60:1",
  "hash": "b4f360216532fabcf5f98339e97f106259dfaa269769e6de35bb82c899765355",
  "cid": "QmV1b4f360216532fabcf5f98339e97f106259dfaa26",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294628,
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
      "evaluated_at": 1760294628
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
  "sig": "486b281df6c3ee553e6836d274ba6b1d3510c0e278bffc1e196cbb0c7c133582"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105152240558
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 241, 'threshold': 50, 'total_amount': 100486637, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 240, 'first_seen': 1760285765, 'matching_hash': '0371944fd59dbf43'}}}