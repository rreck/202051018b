```json
{
  "id": "bc6cc065c724b900",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760294090,
  "host_pid": "9e6742732c60:1",
  "hash": "0ca2f1aa0c0c5cca43a4259acafd96d8cd10089454ae908a99c3f1e1e06d316a",
  "cid": "QmV10ca2f1aa0c0c5cca43a4259acafd96d8cd100894",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760294090,
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
      "evaluated_at": 1760294090
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
  "sig": "9644846d224f691f1acd164153f1ef66d45409127a8d38f70188852fde9da932"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000023546405
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 231, 'threshold': 50, 'total_amount': 99544137, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 230, 'first_seen': 1760285763, 'matching_hash': '22f38bfa79b47563'}}}