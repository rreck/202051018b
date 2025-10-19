```json
{
  "id": "9ea1f8b46331f298",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287734,
  "host_pid": "9e6742732c60:1",
  "hash": "9f9ac66200180bd480f40781d3eb83e5c1cb453ce5bb0aebe6cf17fa37565ec7",
  "cid": "QmV19f9ac66200180bd480f40781d3eb83e5c1cb453c",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287734,
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
      "evaluated_at": 1760287734
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
  "sig": "8c05f9d3354faa71099c47d733bd0bce80b7a89fd794b206b925c998459df446"
}
```

Fraud detected: duplicate_transaction (score: 87)
Transaction: 021000025001530
Details: {'velocity': {'fraud_detected': True, 'risk_score': 90, 'details': {'transaction_count': 70, 'threshold': 50, 'total_amount': 16901780, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 69, 'first_seen': 1760285765, 'matching_hash': 'c7ad70870577ca51'}}}