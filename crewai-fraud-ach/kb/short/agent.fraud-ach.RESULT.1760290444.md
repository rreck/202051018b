```json
{
  "id": "b1411e8085847e6d",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760290444,
  "host_pid": "9e6742732c60:1",
  "hash": "2fd0e7c44f0ec91e247c67b6ca053455aa0d399cede51650d6c4c5272e63f436",
  "cid": "QmV12fd0e7c44f0ec91e247c67b6ca053455aa0d399c",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760290444,
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
      "evaluated_at": 1760290444
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
  "sig": "e1d273088a6909e934b1d82625eb6671a7b2641a1947e40df52c502764ce04bf"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 031201469832017
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 150, 'threshold': 50, 'total_amount': 46882650, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 149, 'first_seen': 1760285765, 'matching_hash': '99e095073411ccc4'}}}