```json
{
  "id": "1d318a7b60223b46",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290359,
  "host_pid": "9e6742732c60:1",
  "hash": "a1e443a91e18180052699361e8284bdb0871cf80d89f5ae08359ab76244ae090",
  "cid": "QmV1a1e443a91e18180052699361e8284bdb0871cf80",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290359,
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
      "evaluated_at": 1760290359
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
  "sig": "fb981289e9e903778a8243c57106f2cd6836810b03bb155cff04229a27cd1f75"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 021000020048209
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 148, 'threshold': 50, 'total_amount': 12306940, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 147, 'first_seen': 1760285765, 'matching_hash': '08bd6998776e568a'}}}