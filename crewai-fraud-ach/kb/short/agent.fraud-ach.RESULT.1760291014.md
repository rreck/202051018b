```json
{
  "id": "d2eb5c3e9058d4a2",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291014,
  "host_pid": "9e6742732c60:1",
  "hash": "4a5a397c6a3f77c9a3436dd9eb939f4a7e4e387c97930a73b7e83ab66f90010d",
  "cid": "QmV14a5a397c6a3f77c9a3436dd9eb939f4a7e4e387c",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291014,
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
      "evaluated_at": 1760291014
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
  "sig": "cf5a355e2f7c2b07ddbac0869968afc0dde8ae7fdd7009c7017f4a662defbd42"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009590857246
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 165, 'threshold': 50, 'total_amount': 58476990, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 164, 'first_seen': 1760285763, 'matching_hash': 'f091f96bdb04a5bf'}}}