```json
{
  "id": "e5e605c9e1201d3c",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292595,
  "host_pid": "9e6742732c60:1",
  "hash": "c84e8934f9eea34f37e84da74d6c7a0c7fea7545b59035db03ae3cc1aa7d6f73",
  "cid": "QmV1c84e8934f9eea34f37e84da74d6c7a0c7fea7545",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292595,
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
      "evaluated_at": 1760292595
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
  "sig": "ef87cca38c7778f7161562d9f902528385507a2085a3ee7d39f5a1c8895024f9"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 111000021660163
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 201, 'threshold': 50, 'total_amount': 49389921, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 200, 'first_seen': 1760285763, 'matching_hash': '34e344aa40e60b39'}}}