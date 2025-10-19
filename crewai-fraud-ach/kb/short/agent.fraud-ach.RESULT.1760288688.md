```json
{
  "id": "c8cb8f4ae4112469",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760288688,
  "host_pid": "9e6742732c60:1",
  "hash": "59b5fe7521ae1eb371e7051626cf1150ebcd178e43039342e3b03fed74c674da",
  "cid": "QmV159b5fe7521ae1eb371e7051626cf1150ebcd178e",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760288688,
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
      "evaluated_at": 1760288688
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
  "sig": "749214a8f9e068e5817842cce9c3f754179b62d3b596854801791afa09cf8209"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 121000247026993
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 101, 'threshold': 50, 'total_amount': 44463533, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 100, 'first_seen': 1760285764, 'matching_hash': '7c7d13001f766fd7'}}}