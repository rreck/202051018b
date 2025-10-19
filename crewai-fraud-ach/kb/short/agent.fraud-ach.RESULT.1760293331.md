```json
{
  "id": "a924be26fd2ae3ab",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293331,
  "host_pid": "9e6742732c60:1",
  "hash": "c531cb6b90250b4fc3d4c35774cb3b73b32f25d9094fc633ea63764c1fedc7af",
  "cid": "QmV1c531cb6b90250b4fc3d4c35774cb3b73b32f25d9",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293331,
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
      "evaluated_at": 1760293331
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
  "sig": "8af656fdfcec71b8ddb4f2b69862123016fa5644f06853d6305cd689ed569ef1"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 063100272952668
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 216, 'threshold': 50, 'total_amount': 38240424, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 215, 'first_seen': 1760285763, 'matching_hash': 'e2aecc84b992b480'}}}