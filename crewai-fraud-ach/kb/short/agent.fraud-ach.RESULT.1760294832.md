```json
{
  "id": "34ebf5e2ce0721c8",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294832,
  "host_pid": "9e6742732c60:1",
  "hash": "347c548ebf3cc535255c9f81250602905a7a7c6311e22b56cefc169198bd7e1e",
  "cid": "QmV1347c548ebf3cc535255c9f81250602905a7a7c63",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294832,
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
      "evaluated_at": 1760294832
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
  "sig": "a784a29f1fb0937f88b8cc3d0c33464f435b6642d4a897e5cc20cfa632fbbe6d"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000021328085
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 321, 'threshold': 50, 'total_amount': 22175643, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 320, 'first_seen': 1760284979, 'matching_hash': 'f7c67db4baca4bf3'}}}}