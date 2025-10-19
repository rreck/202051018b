```json
{
  "id": "6e8c0dcc2d9890bc",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760292416,
  "host_pid": "9e6742732c60:1",
  "hash": "c0530a92262786228b0cfc35dfb05af2f86e9a18e2dcfedfc934247863df1248",
  "cid": "QmV1c0530a92262786228b0cfc35dfb05af2f86e9a18",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760292416,
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
      "evaluated_at": 1760292416
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
  "sig": "8c6b8c9762ecc4fb3d08de02b42b384e05a0ded38d400c3f3339562c3a12f7ab"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009591582850
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 197, 'threshold': 50, 'total_amount': 65124851, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 196, 'first_seen': 1760285763, 'matching_hash': '5102e2097242c74b'}}}