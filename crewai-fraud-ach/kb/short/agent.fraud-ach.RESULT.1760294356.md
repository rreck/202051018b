```json
{
  "id": "fd24e7240cb674b9",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294356,
  "host_pid": "9e6742732c60:1",
  "hash": "5dcf5ef5d9c7ad580b4d3b7e5a3b698d146a1085c50e8c14b49e930bc4f39765",
  "cid": "QmV15dcf5ef5d9c7ad580b4d3b7e5a3b698d146a1085",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294356,
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
      "evaluated_at": 1760294356
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
  "sig": "c2e5caff3d57e4e39a5a30a0e39e8e5f0f042427b20441b10286212354f9b6de"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000242075877
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 236, 'threshold': 50, 'total_amount': 29548380, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 235, 'first_seen': 1760285765, 'matching_hash': '7e39a816a4a44fcc'}}}