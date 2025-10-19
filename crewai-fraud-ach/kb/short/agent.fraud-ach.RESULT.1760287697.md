```json
{
  "id": "3b72fe011258941a",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760287697,
  "host_pid": "9e6742732c60:1",
  "hash": "6e5597b74bd0732104e77eed1c870ad1ae30398817dd7f3d3b3fcabad90b3023",
  "cid": "QmV16e5597b74bd0732104e77eed1c870ad1ae303988",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760287697,
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
      "evaluated_at": 1760287697
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
  "sig": "acfd8dfd862399f3de2592ceb4487516d93f5cb7a3e103b8364c8e3f3b7b48b9"
}
```

Fraud detected: duplicate_transaction (score: 86)
Transaction: 021000021660412
Details: {'velocity': {'fraud_detected': True, 'risk_score': 88, 'details': {'transaction_count': 69, 'threshold': 50, 'total_amount': 22229799, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 68, 'first_seen': 1760285764, 'matching_hash': '19be1dcf8b4c513c'}}}