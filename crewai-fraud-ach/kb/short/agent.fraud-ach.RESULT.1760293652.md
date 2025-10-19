```json
{
  "id": "de30db861e1a9352",
  "scope": "agent",
  "key": "RESULT",
  "epoch": 1760293652,
  "host_pid": "9e6742732c60:1",
  "hash": "3258ec760cb2ae068552e4e1da2522e4c151c50bd8a0580504291596dc956288",
  "cid": "QmV13258ec760cb2ae068552e4e1da2522e4c151c50b",
  "aicp": {
    "prov": {
      "issuer": "9e6742732c60:1",
      "created_at": 1760293652,
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
      "evaluated_at": 1760293652
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
  "sig": "be6b638e5d1b1158739de6a4532c77dff87cc6df8d267fabda557ebc25b53ffd"
}
```

Fraud detected: duplicate_transaction (score: 92)
Transaction: 026009594342556
Details: {'velocity': {'fraud_detected': True, 'risk_score': 100, 'details': {'transaction_count': 223, 'threshold': 50, 'total_amount': 48021266, 'amount_threshold': 10000000}}, 'duplicate': {'fraud_detected': True, 'risk_score': 85, 'details': {'duplicate_count': 222, 'first_seen': 1760285763, 'matching_hash': '530c0ede13f83176'}}}