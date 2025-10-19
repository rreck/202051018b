```json
{
  "id": "1e09b1b18d71d784",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760291316,
  "host_pid": "9e6742732c60:1",
  "hash": "706b5020f4b3af329cba4a05c8b369c6144f3d08bbfe11832125e0536df52a67",
  "cid": "QmV1706b5020f4b3af329cba4a05c8b369c6144f3d08",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760291316,
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
      "evaluated_at": 1760291316
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
  "sig": "f95f892a449b9da89883ab979f5c97ac4e886b67c3d0176223deb4fba57d61c2"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 122105154730054
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 172, 'threshold': 50, 'total_amount': 46312720, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 171, 'first_seen': 1760285763, 'matching_hash': '3072a79f51416ab8'}}}